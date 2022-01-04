# Protocols
A network protocol is an agreement we humans have made about how computers communicate with each other. These agreements make it possible for the Internet to exist without having to use a different standard for each connection.
The OSI model is a good tool to describe where a protocol 'lives' and what the purpose of a protocol is. Often enough, a protocol 'lives' in several layers of the OSI model.
## Key-terms
- TCP - Transmission Control Protocol
- IP - Internet Protocol

## Opdracht

- Understand how an HTTPS TCP/IP packet is constructed
- Understand who determines which protocols we use and what you have to do yourself to introduce a new protocol.
- Identify at least one protocol per OSI layer.
- Facebook was recently unavailable for a long time. Find out why. Hint

### Gebruikte bronnen
https://www.techtarget.com/searchnetworking/feature/3-lessons-from-the-2021-Facebook-outage-for-network-pros

https://www.techrepublic.com/article/exploring-the-anatomy-of-a-data-packet

https://www.cloudflare.com/learning/ssl/what-is-https

https://www.guru99.com/layers-of-osi-model.html

https://www.guru99.com/tcp-ip-model.html

https://www.youtube.com/watch?v=OTwp3xtd4dg
### Ervaren problemen
.

### Resultaat
### Understand how an HTTPS TCP/IP packet is constructed

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/TCP.png)
  - The TCP packet format consists of these fields: 
  - Source Port and Destination Port fields (16 bits each) identify the end points of the connection. 
  - Sequence Number field (32 bits) specifies the number assigned to the first byte of data in the current message. Under certain circumstances, it can also be used to identify an initial sequence number to be used in the upcoming transmission. 
  - Acknowledgement Number field (32 bits) contains the value of the next sequence number that the sender of the segment is expecting to receive, if the ACK control bit is set. Note that the sequence number refers to the stream flowing in the same direction as the segment, while the acknowledgement number refers to the stream flowing in the opposite direction from the segment. 
  - Data Offset (a.k.a. Header Length) field (variable length) tells how many 32-bit words are contained in the TCP header. This information is needed because the Options field has variable length, so the header length is variable too. 
  - Reserved field (6 bits) must be zero. This is for future use. 
  - Flags field (6 bits) contains the various flags: 
  - URG—Indicates that some urgent data has been placed. 
  - ACK—Indicates that acknowledgement number is valid. 
  - PSH—Indicates that data should be passed to the application as soon as possible. 
  - RST—Resets the connection. 
  - SYN—Synchronizes sequence numbers to initiate a connection. 
  - FIN—Means that the sender of the flag has finished sending data. 
  - Window field (16 bits) specifies the size of the sender's receive window (that is, buffer space available for incoming data). 
  - Checksum field (16 bits) indicates whether the header was damaged in transit. 
  - Urgent pointer field (16 bits) points to the first urgent data byte in the packet. 
  - Options field (variable length) specifies various TCP options. 
  - Data field (variable length) contains upper-layer information
### IP 
![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/IP.png)

  - Version field (4 bits) indicates the version of IP currently used. 
  - IP Header Length (IHL) field (4 bits) indicates how many 32-bit words are in the IP header. 
  - Type-of-service field (8 bits) specifies how a particular upper-layer protocol would like the current datagram to be handled. Datagrams can be assigned various levels of importance through this field. 
  - Total Length field (16 bits) specifies the length of the entire IP packet, including data and header, in bytes. 
  - Identification field (16 bits) contains an integer that identifies the current datagram. This field is used to help reconstruct datagram fragments. 
  - Flags field (4 bits; one is not used) controls whether routers are allowed to fragment a packet and indicates the parts of a packet to the receiver. 
  - Time-to-live field (8 bits) maintains a counter that gradually decrements to zero, at which point the datagram is discarded. This keeps packets from looping endlessly. 
  - Protocol field (8 bits) indicates which upper-layer protocol receives incoming packets after IP processing is complete. 
  - Header Checksum field (16 bits) helps ensure IP header integrity. 
  - Source Address field (32 bits) specifies the sending node. 
  - Destination Address field (32 bits) specifies the receiving node. 
  - Options field (32 bits) allows IP to support various options, such as security. 
  - Data field (32 bits) contains upper-layer information. 
  
![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/http.png)
### Identify at least one protocol per OSI layer.
![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/OSI.png)

### Facebook was recently unavailable for a long time. Find out why. 
  - There was a misconfiguration at the backbone of the network and a software bug caused the control to fail. The faulty command executed across the backbone routers and disconnected Facebook's data centers.That, in turn, triggered the secondary DNS and BGP problems. <br> When the company's DNS servers couldn't communicate with the data centers, they automatically withdrew their BGP route advertisements, essentially removing themselves from the virtual map of the internet. Suddenly, it was as if Facebook, Instagram and WhatsApp didn't exist.<br>To make matters worse, Facebook's internal operations tools rely on the company's own infrastructure and DNS to function. Employees, therefore, couldn't access the systems they typically use to work and communicate, and the networking staff couldn't investigate or resolve the outage remotely via their usual methods.
Engineers ultimately had to get inside Facebook's data centers to manually debug and reset routers and servers


