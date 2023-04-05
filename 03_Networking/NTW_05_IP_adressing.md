# 
An IP address is a unique address that identifies a device on the internet or a local network. IP stands for "Internet Protocol," which is the set of rules governing the format of data sent via the internet or local network.

## Key terminology

- IPv4 - Internet Protocol version 4 is the fourth version of the Internet Protocol (IP). It is one of the core protocols of standards-based internetworking methods in the Internet and other packet-switched networks.

- IPv6 -  the most recent version of the Internet Protocol, was developed by the Internet Engineering Task Force (IETF) to deal with the long-anticipated problem of IPv4 address exhaustion, and is intended to replace IPv4.

- Public IP adress - is an IP address that can be accessed directly over the internet and is assigned to your network router by your internet service provider.

- Private IP adress - a range of non-internet facing IP addresses used in an internal network. Private IP addresses are provided by network devices, such as routers, using network address translation. Internet Protocol (IP) addresses identify a device on either the internet or a local network.

- NAT (Network address translation) is a method of mapping an IP address space into another by modifying network address information in the IP header of packets while they are in transit across a traffic routing device.

- Static address - an address that doesn't change. Once your device is assigned a static IP address, that number typically stays the same until the device is decommissioned or your network architecture changes. Static IP addresses generally are used by servers or other important equipment.

- Dynamic address- a temporary address for devices connected to a network that continually changes over time. 

- DHCP (Dynamic Host Configuration Protocol) - a network protocol or server that automatically configures IP addresses for any device on the network.

- ISP - Internet Service Provider. 

## Exercise

- Ontdek wat je publieke IP adres is van je laptop en mobiel op wifi.

- Zijn de adressen hetzelfde of niet? Leg uit waarom.

- Ontdek wat je privé IP adres is van je laptop en mobiel op wifi.

- Zijn de adressen hetzelfde of niet? Leg uit waarom.

- Verander het privé IP adres van je mobiel naar dat van je laptop. Wat gebeurt er dan?

- Probeer het privé IP adres van je mobiel te veranderen naar een adres buiten je netwerk. Wat gebeurt er dan?


### Sources
[https://www.kaspersky.com/resource-center/definitions/what-is-an-ip-address](https://www.kaspersky.com/resource-center/definitions/what-is-an-ip-address)

[https://en.wikipedia.org/wiki/IPv4](https://en.wikipedia.org/wiki/IPv4)

[https://en.wikipedia.org/wiki/IPv6](https://en.wikipedia.org/wiki/IPv6)

[https://www.avast.com/c-ip-address-public-vs-private#:~:text=A%20public%20IP%20address%20is,through%20your%20router's%20public%20IP.](https://www.avast.com/c-ip-address-public-vs-private#:~:text=A%20public%20IP%20address%20is,through%20your%20router's%20public%20IP.)

[https://www.techtarget.com/whatis/definition/private-IP-address#:~:text=A%20private%20IP%20address%20is,internet%20or%20a%20local%20network.](https://www.techtarget.com/whatis/definition/private-IP-address#:~:text=A%20private%20IP%20address%20is,internet%20or%20a%20local%20network.)

[https://en.wikipedia.org/wiki/Network_address_translation](https://en.wikipedia.org/wiki/Network_address_translation)

[https://www.techtarget.com/whatis/definition/dynamic-IP-address](https://www.techtarget.com/whatis/definition/dynamic-IP-address)

[https://www.avast.com/c-static-vs-dynamic-ip-addresses#:~:text=A%20static%20IP%20address%20is,servers%20or%20other%20important%20equipment.](https://www.avast.com/c-static-vs-dynamic-ip-addresses#:~:text=A%20static%20IP%20address%20is,servers%20or%20other%20important%20equipment.)

****

### Overcome challenges


### Results

My public IP address:

of my phone:

![image](/00_includes/networking_05_1_screenshot.png)

of my laptop:

![image](/00_includes/networking_05_2_screenshot.png)

The modem connects the public Internet to my network.  Requests from my internal network are sent to the modem, which routes them to the Internet.  Thus, only one public IP address is needed for all of my devices to communicate with the Internet.

Private IP adresses are not the same because each device connected to the router/modem has it's own private IP address within the network.

I changed the private IP of my phone to the one of my laptop and I get an IP conflict. (At first I didn't recognize the error because the phone automatically connected to IPv6 and google page was working but I decided to try to open the site https://www.funda.nl/ and got an error: "Safari cannot open the page because the server cannot be found"). This means one of the two devices would not be able to communicate with the router.

When I changed the IP address from my phone to an IP address outside of my network I received the same error.