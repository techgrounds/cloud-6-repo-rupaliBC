Physical layer or below : Hubs, Repeaters, Cables, Fibers, Wireless..
Data-link layer: Bridges, Modems, Network cards, 2-layer switches.
Network layer: Routers, Brouters, 3-layer switches.
Transport layer: Gateways, Firewalls.
Session layer: Gateways, Firewalls, PC’s.
Presentation layer : Gateways, Firewalls, PC’s.
Application layer: Gateways,Firewalls, all end devices like PC’s, Phones, Servers..


A repeater is a two-port device used to extend an Ethernet connection to allow devices to communicate at greater distances. A repeater strengthens and retransmits signals.
A hub is a multiport repeater. It may be active (amplifying the signal) or passive (no amplification). Hubs transmit data to all ports regardless of the final destination.
A modem works in all seven layers but primarily at OSI layer 1. A modem modulates and demodulates signals sent over telephone lines. A modem converts a computer’s digital signal into a land line’s analog signal.
1. Repeater – A repeater operates at the physical layer. Its job is to regenerate the signal over the same network before the signal becomes too weak or corrupted so as to extend the length to which the signal can be transmitted over the same network. An important point to be noted about repeaters is that they do not amplify the signal. When the signal becomes weak, they copy the signal bit by bit and regenerate it at the original strength. It is a 2 port device. 

2. Hub –  A hub is basically a multiport repeater. A hub connects multiple wires coming from different branches, for example, the connector in star topology which connects different stations. Hubs cannot filter data, so data packets are sent to all connected devices.  In other words, the collision domain of all hosts connected through Hub remains one.  Also, they do not have the intelligence to find out the best path for data packets which leads to inefficiencies and wastage. 
3. 3. Bridge – A bridge operates at the data link layer. A bridge is a repeater, with add on the functionality of filtering content by reading the MAC addresses of source and destination. It is also used for interconnecting two LANs working on the same protocol. It has a single input and single output port, thus making it a 2 port device.
4. 4. Switch – A switch is a multiport bridge with a buffer and a design that can boost its efficiency(a large number of ports imply less traffic) and performance. A switch is a data link layer device. The switch can perform error checking before forwarding data, which makes it very efficient as it does not forward packets that have errors and forward good packets selectively to the correct port only.  In other words, the switch divides the collision domain of hosts, but broadcast domain remains the same. 
  
5. Routers – A router is a device like a switch that routes data packets based on their IP addresses. The router is mainly a Network Layer device. Routers normally connect LANs and WANs together and have a dynamically updating routing table based on which they make decisions on routing the data packets. Router divide broadcast domains of hosts connected through it.

 
