# OSI Stack

## Key terminology
- The Open Systems Interconnection model (OSI model) - a conceptual model created by the International Organization for Standardization which enables diverse communication systems to communicate using standard protocols. In the OSI reference model, the communications between a computing system are split into seven different abstraction layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application.

- The TCP/IP model - a functional model designed to solve specific communication problems, and which is based on specific, standard protocols. 

## Exercise
 - Study:
    - The OSI model and its uses.
    - The TCP/IP model and its uses.

### Sources
[https://en.wikipedia.org/wiki/OSI_model](https://en.wikipedia.org/wiki/OSI_model)

[https://oracle-patches.com/en/cloud-net/the-osi-model-and-the-tcp-ip-stack](https://oracle-patches.com/en/cloud-net/the-osi-model-and-the-tcp-ip-stack)

[https://www.forcepoint.com/cyber-edu/osi-model#:~:text=The%20OSI%20Model%20(Open%20Systems,between%20different%20products%20and%20software.](https://www.forcepoint.com/cyber-edu/osi-model#:~:text=The%20OSI%20Model%20(Open%20Systems,between%20different%20products%20and%20software.)

[https://nightfall.ai/4-reasons-why-the-osi-model-still-matters](https://nightfall.ai/4-reasons-why-the-osi-model-still-matters)

[https://learningnetwork.cisco.com/s/question/0D53i00000Kt6bPCAR/tcpip-model-4-or-5-layer](https://learningnetwork.cisco.com/s/question/0D53i00000Kt6bPCAR/tcpip-model-4-or-5-layer)

****

### Overcome challenges
To find answer:
Does TCP/IP model has 4 layers or 5 layers? (Answer is in the end of the results)

### Results
![image](/00_includes/networking_01_OSI_1.jpeg)

the OSI layers:
1. Physical layer - is responsible for the physical connection between devices. Protocol Data Unit (PDU)- a bit. In addition to ones and zeros, the physical layer knows nothing. Wires, patch panels, network hubs, network adapters work at this layer. The network adapter itself receives a sequence of bits and passes it on.

2. Data link layer. Protocol Data Unit (PDU)- a frame. At this layer appears adressing. (The address is the MAC address.) The data link layer is responsible for the delivery of frames to the destination and their integrity. In the most commom networks the ARP protocol works at the data link layer. Second-layer addressing works only within one network segment and knows nothing about routing - this is handled by a higher layer. Accordingly, devices operating on L2 are switches, bridges and a network adapter driver.

3. Network layer. PDU - a packet. The most common protocol here is IP. Addressing occurs by IP addresses, which consist of 32 bits. The protocol is routable, a packet is able to get to any part of the network through a certain number of routers. Routers work on L3.

4. Transport layer. PDU - segment / datagram . At this layer appear the concepts of ports. TCP and UDP are working here. Protocols of this layer are responsible for direct communication between applications and for the reliability of information delivery. For example, TCP is able to request a retransmission of data in case the data was received incorrectly or not all. TCP can also change the data transfer rate if the receiving side does not have time to accept everything (TCP Window Size).

The following layers are only "correctly" implemented in the RFC. In practice, the protocols described at the following layers operate simultaneously at several levels of the OSI model, so there is no clear separation into session and presentation layers. In this regard, the main stack currently used is TCP / IP.

5. Session layer. PDU - data. Manages a communication session, information exchange, rights. Protocols - L2TP, PPTP.

6. Presentation layer. PDU - data. Presentation and encryption of data. JPEG, ASCII, MPEG.

7. Application layer. PDU - data. The most numerous and varied layer. It runs all high-level protocols. Such as POP, SMTP, RDP, HTTP, etc. The protocols here do not have to think about routing or guaranteeing the delivery of information - these are handled by lower layers. At level 7, it is only necessary to implement specific actions, for example, receiving an html code or an email message to a specific recipient.

****
![image](/00_includes/networking_01_OSI_2.png)

TCP/IP model is defined with 5 layers as application layer, transport layer, network layer, data link layer and physical layer.

While
the four layer TCP/IP model has the layers Application Layer, Transport Layer, Internet Layer and Network Access Layer (link layer).

Internet layer in the above 4 layer model is the same thing as the network layer defined in the 5 layer model. Whereas
Network Access layer (link layer) in the 4 layer model is the data link layer and the physical layer of the 5 layer model combined into a single layer in the 4 layer model.
