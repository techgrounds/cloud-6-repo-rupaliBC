# Protocols
A network protocol is an agreement we humans have made about how computers communicate with each other. These agreements make it possible for the Internet to exist without having to use a different standard for each connection.
The OSI model is a good tool to describe where a protocol 'lives' and what the purpose of a protocol is. Often enough, a protocol 'lives' in several layers of the OSI model.
## Key-terms
- TCP - Transmission Control Protocol
- IP - Internet Protocol
- 



## Opdracht

- Understand how an HTTPS TCP/IP packet is constructed
- Understand who determines which protocols we use and what you have to do yourself to introduce a new protocol.
- Identify at least one protocol per OSI layer.
- Facebook was recently unavailable for a long time. Find out why. Hint

### Gebruikte bronnen
https://www.techtarget.com/searchnetworking/feature/3-lessons-from-the-2021-Facebook-outage-for-network-pros
### Ervaren problemen
.

### Resultaat
### Understand how an HTTPS TCP/IP packet is constructed
![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/TCP.png)
![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/IP.png)
![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/http.png)
### Identify at least one protocol per OSI layer.
![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/OSI.png)

### Facebook was recently unavailable for a long time. Find out why. 
  - There was a misconfiguration at the backbone of the network and a software bug caused the control to fail. The faulty command executed across the backbone routers and disconnected Facebook's data centers.That, in turn, triggered the secondary DNS and BGP problems. <br> When the company's DNS servers couldn't communicate with the data centers, they automatically withdrew their BGP route advertisements, essentially removing themselves from the virtual map of the internet. Suddenly, it was as if Facebook, Instagram and WhatsApp didn't exist.<br>To make matters worse, Facebook's internal operations tools rely on the company's own infrastructure and DNS to function. Employees, therefore, couldn't access the systems they typically use to work and communicate, and the networking staff couldn't investigate or resolve the outage remotely via their usual methods.
Engineers ultimately had to get inside Facebook's data centers to manually debug and reset routers and servers

