# Protocols

In networking, a protocol is a standardized set of rules for formatting and processing data. Protocols enable computers to communicate with one another.

## Key terminology

Wireshark -  network protocol analyzer, or an application that captures packets from a network connection, such as from your computer to your home office or the internet. Packet is the name given to a discrete unit of data in a typical Ethernet network.

UDP - (the User Datagram Protocol) is one of the core communication protocols of the Internet protocol suite used to send messages (transported as datagrams in packets) to other hosts on an Internet Protocol (IP) network. UDP is used in applications where speed is more important such as video conferencing, live streaming, and online gaming.

DNS - (The Domain Name System) is the hierarchical and decentralized naming system used to identify computers reachable through the Internet or other Internet Protocol (IP) networks.

Three-way handshake - is a process which is used in a TCP/IP network to make a connection between the server and client. It is a three-step process that requires both the client and server to exchange synchronization and acknowledgment packets before the real data communication process starts.

## Exercise

- Identify several other protocols and their associated OSI layer. Name at least one for each layer.
- Figure out who determines what protocols we use and what is needed to introduce your own protocol.
- Look into wireshark and install this program. Try and capture a bit of your own network data. Search for a protocol you know and try to understand how it functions.


### Sources
 [https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-protocol/](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-protocol/)

[https://docs.oracle.com/cd/E19683-01/806-4075/ipov-10/index.html](https://docs.oracle.com/cd/E19683-01/806-4075/ipov-10/index.html)

[https://en.wikipedia.org/wiki/List_of_network_protocols_(OSI_model)](https://en.wikipedia.org/wiki/List_of_network_protocols_(OSI_model))

[https://www.guru99.com/tcp-3-way-handshake.html](https://www.guru99.com/tcp-3-way-handshake.html)

[https://en.wikipedia.org/wiki/User_Datagram_Protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol)

[https://www.vpnmentor.com/blog/tcp-vs-udp/](https://www.vpnmentor.com/blog/tcp-vs-udp/)

[https://www.internetx.com/en/news-detailview/who-creates-the-standards-and-protocols-for-the-internet](https://www.internetx.com/en/news-detailview/who-creates-the-standards-and-protocols-for-the-internet)

[https://networkencyclopedia.com/request-for-comments-rfc/](https://networkencyclopedia.com/request-for-comments-rfc/)

[https://www.wireshark.org/docs/wsug_html_chunked/](https://www.wireshark.org/docs/wsug_html_chunked/)

****

### Overcome challenges


### Results
1. 
Physical layer - RS-232 / Ethernet (IEEE 802.3) / ISDN 

Data link layer (Physical addressing) - PPP / SLIP / IEEE 802.2

Network layer (Path determination and logical addressing) - IP / ICMP / PX / ARP

Transport layer (End-to-end connections and reliability) - TCP / UDP / SPX

Session layer (Interhost communication) - NFS / RPC / SQL / RTP / SAP

Presentation layer (Data representation and encryption) - MPEG / ASCH / SSL / HTML / TLS

Application layer (Network process to end-user application) SMTP / DNS / HTTP / FTP / POP3

2. 

The organisations that determine what protocols we use are:

- The world Wide Web Consortium (W3C)

- Internet Architecture Board (IAB)

- Internet corparation for Assigned Names and Numbers (ICANN)

- Internet Assigned Number Authority (IANA)

- The institute of Electrical and Electronics Engineers (IEEE)

- The internet Engineering Task Force (IETF)

- The international organization for standardization (ISO)

- The international telecommunications union (ITU)

- Internet Research Task Force (IRTF)

To introduce our own protocol, we need RFC (request for comments) Any member of the Internet Society (ISOC) can submit an RFC for consideration, although submission is usually done through the Internet Engineering Task Force (IETF). Once published, an RFC is reviewed by various technical groups. 

About all steps [https://www.ietf.org/standards/publication/](https://www.ietf.org/standards/publication/)

3.

![image](/00_includes/networking_03_screenshot.png)

