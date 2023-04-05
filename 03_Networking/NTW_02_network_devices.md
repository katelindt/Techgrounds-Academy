# Network Devices
Network devices are physical devices that are required for communication and interaction between hardware on a computer network.

## Key terminology
- Hub - the most basic networking device that connects multiple computers or other network devices. Unlike a network switch or router, a network hub has no routing tables or intelligence on where to send information and broadcasts all network data across each connection. Most hubs can detect basic network errors, such as collisions, but having all information broadcast to multiple ports is a security risk and causes bottlenecks. In the past, network hubs were popular because they were cheaper than a switch or router. Today, switches do not cost much more than a hub and are a better solution for any network.

- Switch - is networking hardware that connects devices on a computer network by using packet switching to receive and forward data to the destination device.
Unlike repeater hubs, which broadcast the same data out of each port and let the devices pick out the data addressed to them, a network switch learns the identities of connected devices and then only forwards data to the port connected to the device to which it is addressed.

- Router - a device that connects two or more packet-switched networks or subnetworks. It serves two primary functions: managing traffic between these networks by forwarding data packets to their intended IP addresses, and allowing multiple devices to use the same Internet connection.

- Bridge - a computer networking device that creates a single, aggregate network from multiple communication networks or network segments. This function is called network bridging. Bridging is distinct from routing. Routing allows multiple networks to communicate independently and yet remain separate, whereas bridging connects two separate networks as if they were a single network.

- Gateway - a piece of networking hardware or software used in telecommunications networks that allows data to flow from one discrete network to another. Gateways are distinct from routers or switches in that they communicate using more than one protocol to connect multiple networks and can operate at any of the seven layers of the open systems interconnection model (OSI).

- Modem (modulator-demodulator) - a computer hardware device that converts data from a digital format into a format suitable for an analog transmission medium such as telephone or radio. A modem transmits data by modulating one or more carrier wave signals to encode digital information, while the receiver demodulates the signal to recreate the original digital information. The goal is to produce a signal that can be transmitted easily and decoded reliably.

- Repeater -  operates at the physical layer. Its job is to regenerate the signal over the same network before the signal becomes too weak or corrupted so as to extend the length to which the signal can be transmitted over the same network. An important point to be noted about repeaters is that they do not amplify the signal. When the signal becomes weak, they copy the signal bit by bit and regenerate it at the original strength. It is a 2 port device. 

- Access Point - an object that serves as a connection or medium for other devices to gain access to the Internet or to other devices in the network.

- Media converter - a networking device that transparently converts Ethernet or other communication protocols from one cable type to another type, usually copper CATx/UTP to fibre.

## Exercise
- Name and describe the functions of common network equipment.
- Most routers have an overview of all connected devices, find this list. What other information does the router have about connected equipment?
- Where is your DHCP server located on your network? What are the configurations of this?


### Sources

[https://blog.netwrix.com/2019/01/08/network-devices-explained/](https://blog.netwrix.com/2019/01/08/network-devices-explained/)

[https://en.wikipedia.org/wiki/Network_switch](https://en.wikipedia.org/wiki/Network_switch)

[https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-router/](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-router/)

[https://en.wikipedia.org/wiki/Network_bridge](https://en.wikipedia.org/wiki/Network_bridge)

[https://en.wikipedia.org/wiki/Gateway_(telecommunications)](https://en.wikipedia.org/wiki/Gateway_(telecommunications))

[https://www.geeksforgeeks.org/network-devices-hub-repeater-bridge-switch-router-gateways/](https://www.geeksforgeeks.org/network-devices-hub-repeater-bridge-switch-router-gateways/)

[https://www.blackbox.be/en-be/page/45973/Resources/Technical-Resources/Black-Box-Explains/lan/What-is-a-Media-Converter#:~:text=A%20media%20converter%20is%20a,copper%20CATx%2FUTP%20to%20fibre.](https://www.blackbox.be/en-be/page/45973/Resources/Technical-Resources/Black-Box-Explains/lan/What-is-a-Media-Converter#:~:text=A%20media%20converter%20is%20a,copper%20CATx%2FUTP%20to%20fibre.)

[https://www.easytechjunkie.com/what-is-an-access-point.htm](https://www.easytechjunkie.com/what-is-an-access-point.htm)

****

### Overcome challenges


### Results

My router's client list:

![image](/00_includes/networking_02_1_screenshot.png)

It is possible to add port forwarding rule, add device in DMZ, see what kind of permissions the client has, how much data the device is using.

Configurations of my DHCP server:

![image](/00_includes/networking_02_2_screenshot.png)