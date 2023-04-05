# Identity and Access Management

Identity and access management (IAM) is the practice of making sure that people and entities with digital identities have the right level of access to enterprise resources like networks and databases. User roles and access privileges are defined and managed through an IAM system.

## Key terminology
- Authentification - the act of proving an assertion, such as the identity of a computer system user. 

- Authorization - the function of specifying access rights/privileges to resources, which is related to general information security and computer security, and to access control in particular.

- MFA (Multi-factor Authentication) is an authentication method that requires the user to provide two or more verification factors to gain access to a resource such as an application, online account, or a VPN. MFA is a core component of a strong identity and access management (IAM) policy.

- The principle of least privilege

## Exercise

Study
- The difference between authentication and authorization.
- The three factors of authentication and how MFA improves security.
- What the principle of least privilege is and how it improves security.



### Sources

[https://www.cisco.com/c/en/us/products/security/identity-services-engine/what-is-identity-access-management.html](https://www.cisco.com/c/en/us/products/security/identity-services-engine/what-is-identity-access-management.html)

[https://www.onelogin.com/learn/iam](https://www.onelogin.com/learn/iam)

[https://en.wikipedia.org/wiki/Principle_of_least_privilege#:~:text=The%20principle%20of%20least%20privilege%20forces%20code%20to%20run%20with,perform%20malicious%20or%20undesirable%20processes.](https://en.wikipedia.org/wiki/Principle_of_least_privilege#:~:text=The%20principle%20of%20least%20privilege%20forces%20code%20to%20run%20with,perform%20malicious%20or%20undesirable%20processes.)

[https://www.onelogin.com/learn/authentication-vs-authorization#:~:text=Authentication%20and%20authorization%20are%20two,authorization%20determines%20their%20access%20rights.](https://www.onelogin.com/learn/authentication-vs-authorization#:~:text=Authentication%20and%20authorization%20are%20two,authorization%20determines%20their%20access%20rights.)

[https://rublon.com/blog/what-are-the-three-authentication-factors/#:~:text=The%20three%20authentication%20factors%20are,something%20you%20are%2C%20e.g.%2C%20fingerprint](https://rublon.com/blog/what-are-the-three-authentication-factors/#:~:text=The%20three%20authentication%20factors%20are,something%20you%20are%2C%20e.g.%2C%20fingerprint)

[https://www.copado.com/devops-hub/blog/what-are-the-benefits-of-principle-of-least-privilege-polp-for-my-organization](https://www.copado.com/devops-hub/blog/what-are-the-benefits-of-principle-of-least-privilege-polp-for-my-organization)

****

### Overcome challenges


### Results

- ### The difference between authentication and authorization.

Authentication and authorization are two vital information security processes that administrators use to protect systems and information. Authentication verifies the identity of a user or service, and authorization determines their access rights.

The best way to illustrate the differences between the two terms is with a simple example. Let's say you decide to go and visit a friend's home. On arrival, you knock on the door, and your friend opens it. She recognizes you (authentication) and greets you. As your friend has authenticated you, she is now comfortable letting you into her home. However, based on your relationship, there are certain things you can do and others you cannot (authorization). For example, you may enter the kitchen area, but you cannot go into her private office. In other words, you have the authorization to enter the kitchen, but access to her private office is prohibited.

 - ### The three authentication factors are:

    - Knowledge Factor – something you know, e.g., password
    - Possession Factor – something you have, e.g., mobile phone
    - Inherence Factor – something you are, e.g., fingerprint

![image](/00_includes/sec_03.png)
    
The primary objective of multi-factor authentication is to reduce the risk of account takeovers and provide additional security for users and their accounts. Since over 80% of cyber breaches happen due to weak or stolen passwords, MFA can provide added layers of security necessary to protect users and their data.

- ### What the principle of least privilege is and how it improves security:

The principle of least privilege (PoLP), also known as the principle of minimal privilege (PoMP) or the principle of least authority (PoLA). The principle means giving a user account or process only those privileges which are essential to perform its intended function.

It prevents the spread of malware on your network. An administrator or superuser with access to a lot of other network resources and infrastructure could potentially spread malware to all those other systems.