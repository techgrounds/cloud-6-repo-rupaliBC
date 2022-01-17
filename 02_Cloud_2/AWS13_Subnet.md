# AWS Subnetting
A subnetwork or subnet is a logical subdivision of an IP network. The practice of dividing a network into two or more networks is called subnetting.

Computers that belong to the same subnet are addressed with an identical most-significant bit-group in their IP addresses. This results in the logical division of an IP address into two fields: the network number or routing prefix and the rest field or host identifier. The rest field is an identifier for a specific host or network interface.

Subnetting is the process of designating some high-order bits from the host part as part of the network prefix and adjusting the subnet mask appropriately. This divides a network into smaller subnets.
## Key-terms
- NAT Gateway : 

    A NAT gateway is a Network Address Translation (NAT) service. You can use a NAT gateway so that instances in a private subnet can connect to services outside your VPC but external services cannot initiate a connection with those instances.
- Internet Gateway :

    An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet. 
- Subnetting :

    Subnetting is the practice of dividing a network into two or smaller networks. It increases routing efficiency, which helps to enhance the security of the network and reduces the size of the broadcast domain.

## Opdracht
- Create a network architecture that meets the following requirements:
- 1 private subnet that can only be reached from within the LAN. This subnet must be able to accommodate at least 15 hosts.
- 1 private subnet that has Internet access through a NAT gateway. This subnet must be able to place at least 30 hosts (the 30 hosts does not include the NAT gateway).
- 1 public subnet with an internet gateway. This subnet must be able to place at least 5 hosts (the 5 hosts is excluding the internet gateway).

### Gebruikte bronnen
- https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html
- https://www.youtube.com/watch?v=ecCuyq-Wprc
- https://www.youtube.com/watch?v=qulRjRFavJI
- https://www.subnet-calculator.com/
- https://docs.microsoft.com/en-us/troubleshoot/windows-client/networking/tcpip-addressing-and-subnetting  


### Ervaren problemen
- It was bit difficult initially to draw an architecture using the website https://app.diagrams.net/. 
- Also finding out subnet ids withoud subnet calculator is bit hard.

### Resultaat


![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/subnet1.png)
