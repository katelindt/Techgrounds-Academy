# Subnetting

Subnetting is the strategy used to partition a single physical network into more than one smaller logical sub-networks (subnets).


## Key terminology

- A network is a group of two or more computers or other electronic devices that are interconnected for the purpose of exchanging data and sharing resources.  

- A subnet, or subnetwork, is a network inside a network. Subnets make networks more efficient. 

- A local area network (LAN) is a collection of devices connected together in one physical location

- A subnet mask is a 32-bit number created by setting host bits to all 0s and setting network bits to all 1s. In this way, the subnet mask separates the IP address into the network and host addresses.

Subnet masks are used when subnetting, which is when you break a network up into smaller networks. By adjusting the subnet mask, you can set the number of available IP addresses within a network.

- CIDR notation (Classless Inter-Domain Routing) is a compact representation of an IP address and its associated network mask.


- What is the difference between private and public subnet?

The instances in the public subnet can send outbound traffic directly to the internet, whereas the instances in the private subnet can't. Instead, the instances in the private subnet can access the internet by using a network address translation (NAT) gateway that resides in the public subnet.

- Network address translation (NAT) is a method of mapping an IP address space into another by modifying network address information in the IP header of packets while they are in transit across a traffic routing device

- Internet Gateway (IGW) allows instances with public IPs to access the internet. 

- NAT Gateway (NGW) allows instances with no public IPs to access the internet.

## Exercise

Maak een netwerkarchitectuur die voldoet aan de volgende eisen:
- 1 private subnet dat alleen van binnen het LAN bereikbaar is. Dit subnet moet minimaal 15 hosts kunnen plaatsen.  

- 1 private subnet dat internet toegang heeft via een NAT gateway.  
Dit subnet moet minimaal 30 hosts kunnen plaatsen (de 30 hosts is exclusief de NAT gateway).  

- 1 public subnet met een internet gateway. Dit subnet moet minimaal 5 hosts kunnen plaatsen (de 5 hosts is exclusief de internet gateway).  

- Plaats de architectuur die je hebt gemaakt inclusief een korte uitleg in de Github repository die je met de learning coach hebt gedeeld.



### Sources

[https://en.wikipedia.org/wiki/Subnetwork](https://en.wikipedia.org/wiki/Subnetwork)

[https://www.freecodecamp.org/news/subnet-mask-definition/#:~:text=A%20subnet%20mask%20defines%20the,network%20up%20into%20smaller%20networks.](https://www.freecodecamp.org/news/subnet-mask-definition/#:~:text=A%20subnet%20mask%20defines%20the,network%20up%20into%20smaller%20networks.)

[https://avinetworks.com/glossary/subnet-mask/](https://avinetworks.com/glossary/subnet-mask/)

[https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-subnet/](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-subnet/)

[https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)

[https://en.wikipedia.org/wiki/Network_address_translation](https://en.wikipedia.org/wiki/Network_address_translation)

[https://www.techtarget.com/searchnetworking/definition/subnet](https://www.techtarget.com/searchnetworking/definition/subnet)


### Overcome challenges


### Results


![image](/00_includes/networking_03_screenshot.png)

