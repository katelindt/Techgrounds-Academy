from constructs import Construct
from aws_cdk.aws_events import Schedule
from requests import get
from aws_cdk import (
    Duration,
    RemovalPolicy,
    CfnOutput,
    Stack,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_backup as backup,
    aws_s3 as S3,
    aws_s3_deployment as s3deploy,
    aws_s3_assets as Asset,
    aws_kms as kms,
    aws_events as event,
    aws_elasticloadbalancingv2 as elb,
    aws_autoscaling as autoscaling,
    aws_certificatemanager as acm,
)
# first run the following command: "pip install requests" or use simple admin_IP
admin_IP = get("https://api.ipify.org").text + "/32"
# admin_IP = "31.187.199.151/32"


class TechgroundsProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

# created web and admin servers

        vpc_web = ec2.Vpc(
            self, "Webserver",
            ip_addresses=ec2.IpAddresses.cidr("10.10.10.0/24"),
            availability_zones=["eu-central-1a", "eu-central-1b"],
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public",
                    cidr_mask=26,
                    subnet_type=ec2.SubnetType.PUBLIC),
                ec2.SubnetConfiguration(
                    name="private",
                    cidr_mask=26,
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
            ]
        )

        vpc_admin = ec2.Vpc(
            self, "Adminserver",
            ip_addresses=ec2.IpAddresses.cidr("10.20.20.0/24"),
            availability_zones=["eu-central-1a", "eu-central-1b"],
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public",
                    cidr_mask=25,
                    subnet_type=ec2.SubnetType.PUBLIC),
            ]
        )

# created VPC Peering Connection

        VPC_peering_connection = ec2.CfnVPCPeeringConnection(
            self, "vpc peering connection",
            peer_vpc_id=vpc_admin.vpc_id,
            vpc_id=vpc_web.vpc_id,
        )
# route table for webserver

        for subnet in vpc_web.private_subnets:
            print(subnet.node.id)
            ec2.CfnRoute(
                self,
                id=f"{subnet.node.id} Webserver Route Table",
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block="10.20.20.0/24",
                vpc_peering_connection_id=VPC_peering_connection.ref,
            )
# route table for adminserver

        for subnet in vpc_admin.public_subnets:
            ec2.CfnRoute(
                self,
                id=f"{subnet.node.id} Adminserver Route Table",
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block="10.10.10.0/24",
                vpc_peering_connection_id=VPC_peering_connection.ref,
            )

# created NACL for webserver

        web_nacl = ec2.NetworkAcl(
            self, "Web NACL",
            vpc=vpc_web,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )

# added inbound and outbound rules for the webserver NACL

        web_nacl.add_entry(
            id="Allow all inbound HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_nacl.add_entry(
            id="Allow all outbound HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_nacl.add_entry(
            id="Allow all inbound HTTPS",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_nacl.add_entry(
            id="Allow all outbound HTTPS",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_nacl.add_entry(
            id="Allow Ephemeral inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_nacl.add_entry(
            id="Allow Ephemeral outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_nacl_private = ec2.NetworkAcl(
            self, "Web Private NACL",
            vpc=vpc_web,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            )
        )

        web_nacl_private.add_entry(
            id="Allow SSH inbound from Admin VPC",
            cidr=ec2.AclCidr.ipv4(vpc_admin.vpc_cidr_block),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_nacl_private.add_entry(
            id=f"Allow HTTP inside VPC NACL",
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_nacl_private.add_entry(
            id=f"Allow ephemeral from Internet NACL",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_nacl_private.add_entry(
            id="Allow HTTP to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_nacl_private.add_entry(
            id="Allow HTTPS to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        web_nacl_private.add_entry(
            id="Allow ephemeral to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

# created NACL for admin server

        admin_nacl = ec2.NetworkAcl(
            self, "Admin NACL",
            vpc=vpc_admin,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )

        admin_nacl.add_entry(
            id="Allow SSH inbound from admin pc",
            cidr=ec2.AclCidr.ipv4(admin_IP),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_nacl.add_entry(
            id="Allow SSH outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_nacl.add_entry(
            id="Allow Ephemeral inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=210,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_nacl.add_entry(
            id="Allow Ephemeral outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=210,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_nacl.add_entry(
            id="Allow RDP inbound",
            cidr=ec2.AclCidr.ipv4(admin_IP),
            rule_number=220,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_nacl.add_entry(
            id="Allow RDP outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=220,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_nacl.add_entry(
            id="Allow HTTP inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=230,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_nacl.add_entry(
            id="Allow HTTP outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=230,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_nacl.add_entry(
            id="Allow HTTPS inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=240,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        admin_nacl.add_entry(
            id="Allow HTTPS outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=240,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

# created webserver Security Group
        web_sg = ec2.SecurityGroup(
            self, "web_sg",
            vpc=vpc_web,
            allow_all_outbound=True,
        )

        web_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow all HTTP traffic from anywhere",
        )

        web_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="Allow all HTTPS traffic from anywhere",
        )

# added rule to allow inbound SSH from only admin server
        web_sg.connections.allow_from(
            ec2.Peer.ipv4("10.20.20.0/24"),
            ec2.Port.tcp(22)
        )

        instance_sg = ec2.SecurityGroup(
            self, "instance_sg",
            vpc=vpc_web,
            allow_all_outbound=True,
        )

        instance_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4(vpc_web.vpc_cidr_block),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP from ALB",
        )

        instance_sg.connections.allow_from(
            ec2.Peer.ipv4("10.20.20.0/24"),
            ec2.Port.tcp(22)
        )


# created adminserver Security Group

        admin_sg = ec2.SecurityGroup(
            self, "admin_sg",
            vpc=vpc_admin,
            allow_all_outbound=True,
        )

# add inbound rules for the adminserver SG

        admin_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4(admin_IP),
            connection=ec2.Port.tcp(22),
            description="Allow SSH traffic from admin IP",
        )

        admin_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4(admin_IP),
            connection=ec2.Port.tcp(3389),
            description="Allow RDP traffic from admin IP",
        )

        admin_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow all HTTP traffic from anywhere",
        )

        admin_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="Allow all HTTPS traffic from anywhere",
        )


# KMS Module

        admin_KMS_key = kms.Key(
            self, "Admin Server Key",
            enable_key_rotation=True,
            pending_window=Duration.days(7),
            alias="admin_KMS_key",
            removal_policy=RemovalPolicy.DESTROY)

        # Web KMS key policy
        # statements=[
        #     iam.PolicyStatement(
        #         actions=[
        #             "kms:Encrypt",
        #             "kms:Decrypt",
        #             "kms:ReEncrypt*",
        #             "kms:GenerateDataKey*",
        #             "kms:DescribeKey"
        #         ],
        #         principals=[iam.ArnPrincipal(
        #             f"arn:aws:iam::{self.account}:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling")],
        #         resources=["*"]
        #     ),
        #         iam.PolicyStatement(
        #             actions=[
        #                 "kms:CreateGrant",
        #             ],
        #             principals=[iam.ArnPrincipal(
        #                 f"arn:aws:iam::{self.account}:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling")],
        #             resources=["*"],
        #             conditions=[
        #                 {
        #                     "Bool": {
        #                         "kms:GrantIsForAWSResource": "true"
        #                     }
        #                 }
        #             ]
        #         )
        #     ]
        # )

        kms_policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": f"arn:aws:iam::{self.account}:root"
                    },
                    "Action": "kms:*",
                    "Resource": "*"
                },
                {
                    "Sid": "Allow service-linked role use of the customer managed key",
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": f"arn:aws:iam::{self.account}:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling"
                    },
                    "Action": [
                        "kms:Encrypt",
                        "kms:Decrypt",
                        "kms:ReEncrypt*",
                        "kms:GenerateDataKey*",
                        "kms:DescribeKey"
                    ],
                    "Resource": "*"
                },
                {
                    "Sid": "Allow attachment of persistent resources",
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": f"arn:aws:iam::{self.account}:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling"
                    },
                    "Action": "kms:CreateGrant",
                    "Resource": "*",
                    "Condition": {
                        "Bool": {
                            "kms:GrantIsForAWSResource": "true"
                        }
                    }
                }
            ]
        }

        web_kms_asg_policy = iam.PolicyDocument.from_json(kms_policy_document)

        web_KMS_key = kms.Key(
            self, "Web Server Key",
            enable_key_rotation=True,
            pending_window=Duration.days(7),
            alias="web_KMS_key",
            removal_policy=RemovalPolicy.DESTROY,
            policy=web_kms_asg_policy)


# S3 User Bucket

        Bucket = S3.Bucket(
            self, "bucket_with_scripts",
            bucket_name="bucket-with-userdata",
            removal_policy=RemovalPolicy.DESTROY,
            encryption=S3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            auto_delete_objects=True
        )

        # Upload userdata to the bucket
        s3deploy.BucketDeployment(
            self, "DeployBucket",
            sources=[s3deploy.Source.asset(
                "techgrounds_project/user_data")],
            destination_bucket=Bucket,
        )

        # created Linux AMI for the WEB server
        ami_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )

        # This is where the user data for the webserver is downloaded.
        userdata_webserver = ec2.UserData.for_linux()
        file_script_path = userdata_webserver.add_s3_download_command(
            bucket=Bucket,
            bucket_key="user_data.sh",
        )

        userdata_webserver.add_s3_download_command(
            bucket=Bucket,
            bucket_key="index.html",
            local_file="/var/www/html/index.html",
        )

        userdata_webserver.add_execute_file_command(file_path=file_script_path)
        userdata_webserver.add_commands("chmod 755 -R /var/www/html/")

        # created Windows AMI for the Admin server
        ami_windows = ec2.MachineImage.latest_windows(
            version=ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE
        )

        web_instance_profile = iam.Role(
            self,
            "Web Instance Profile",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        )

        # Create a launch template for web server
        web_launch_template = ec2.LaunchTemplate(
            self, "Web server template",
            launch_template_name="web_instance_template",
            instance_type=ec2.InstanceType("t2.micro"),
            key_name="web_key_pair",
            machine_image=ami_linux,
            user_data=userdata_webserver,
            security_group=instance_sg,
            role=web_instance_profile,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        kms_key=web_KMS_key,
                        delete_on_termination=True,)
                )
            ]
        )

        # Create an Autoscaling Group for web server
        web_autoscaling_group = autoscaling.AutoScalingGroup(
            self, "AutoScaling Group",
            vpc=vpc_web,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            launch_template=web_launch_template,
            min_capacity=1,
            max_capacity=3,
            health_check=autoscaling.HealthCheck.elb(
                grace=Duration.minutes(5)),
        )

        # scaling policy
        web_autoscaling_group.scale_on_cpu_utilization(
            "CPU Autoscaling",
            target_utilization_percent=65,
        )

        web_ALB = elb.ApplicationLoadBalancer(
            self, "Application Load Balancer",
            vpc=vpc_web,
            internet_facing=True,
            security_group=instance_sg
        )

        web_ALB.add_redirect()

        ssl_certificate = acm.Certificate.from_certificate_arn(
            self, "SSL Certificate", f"arn:aws:acm:{self.region}:{self.account}:certificate/8a1db990-5656-4418-8b40-45781818a548")

        https_listener = web_ALB.add_listener(
            "HTTPS listener",
            port=443,
            open=True,
            certificates=[ssl_certificate]
        )

        https_listener.add_targets(
            "ASG webserver",
            port=80,
            targets=[web_autoscaling_group],
            health_check=elb.HealthCheck(
                enabled=True,
            )
        )

        # created EC2 - Adminserver
        admin_server = ec2.Instance(
            self,
            "admin_ec2",
            vpc=vpc_admin,
            availability_zone="eu-central-1b",
            machine_image=ami_windows,
            security_group=admin_sg,
            key_name="admin_key_pair",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2,
                ec2.InstanceSize.MICRO),
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        kms_key=admin_KMS_key,
                        delete_on_termination=True,)
                )
            ]
        )
        Bucket.grant_read(web_launch_template.role)

        # Backup
        # backup_vault = backup.BackupVault(
        #     self, "BackupVault",
        #     backup_vault_name="BackupVault",
        # )

        # # Backup Plan
        # backup_plan = backup.BackupPlan(
        #     self, "BackupPlan",
        #     backup_vault=backup_vault
        # )

        # backup_vault.apply_removal_policy(RemovalPolicy.DESTROY)
        # backup_plan.apply_removal_policy(RemovalPolicy.DESTROY)

        # Backup Resources
        # backup_plan.add_selection(
        #     "BackupSelection",
        #     resources=[
        #         backup.BackupResource.from_ec2_instance(admin_server),],
        #     allow_restores=True,
        # )

        # Add backup rules
        # backup_plan.add_rule(backup.BackupPlanRule(
        #     enable_continuous_backup=True,
        #     delete_after=Duration.days(7),
        #     schedule_expression=event.Schedule.cron(
        #         day="*",
        #         hour="0",
        #         minute="0",
        #         month="*",
        #         year="*",)
        # )
        # )
