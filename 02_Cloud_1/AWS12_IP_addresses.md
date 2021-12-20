# AWS IP Addresses

An IP address is a unique address that identifies a device on the internet or a local network. IP stands for "Internet Protocol," which is the set of rules governing the format of data sent via the internet or local network.
In essence, IP addresses are the identifier that allows information to be sent between devices on a network: they contain location information and make devices accessible for communication.

## Key-terms
- Public IP - A public IP address identifies you to the wider internet so that all the information you’re searching for can find you.
- Private IP - A private IP address is used within a private network to connect securely to other devices within that same network.
- NAT - Network Address Translation (NAT) is designed for IP address conservation. It enables private IP networks that use unregistered IP addresses to connect to the Internet. NAT operates on a router, usually connecting two networks together, and translates the private (not globally unique) addresses in the internal network into legal addresses, before packets are forwarded to another network.
- IPv4 - The IPv4 uses a 32-bit address, which is the format that you’re probably most familiar with when discussing an “IP address”. This 32-bit address space provides almost 4.3 billion unique addresses, though some IP blocks are reserved for special uses.
Here’s an example of an IPv4 address: 32.253.431.175
- Ipv6 - The IPv6 is a newer version of IP that uses a 128-bit address format and includes both numbers and letters. Here’s an example of an IPv6 address:
3002:0bd6:0000:0000:0000:ee00:0033:6778
## Opdracht
- Find out what your public IP address is of your laptop and mobile on WiFi
- Find out what your public IP address is on your mobile via mobile internet (if possible)
- Create a VM in your cloud with a public IP. Connect to this VM.
- Remove the public IP address from your VM. Understand what is happening with your connection.
### Gebruikte bronnen
https://www.avast.com/c-ip-address-public-vs-private#gref

https://www.kaspersky.com/resource-center/definitions/what-is-an-ip-address

https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/26704-nat-faq-00.html

https://kinsta.com/blog/ipv4-vs-ipv6/

### Ervaren problemen
- To remove Public IP from the instance, i need to follow these steps.
- Create a new network interface.
    - Attach the new network interface to your instance. Now there will be two or more network interfaces attached to your instance. This is important. There MUST be two or more for this to work.
    - Create a new Elastic IP (in the EC2 console).
    - Right-click on the new EIP and associate it to the instance whose public IP you want to remove. The original public IP will be replaced by the new one.
    - Now do the reverse of step 4, disassociate the EIP you have just added. At this point, right-click on the instance and select "Networking", "Manage IP addresses", you will see there are no public IPs on you instance any more. at this point. You must refresh the instances view otherwise you will not see this.

### Resultaat

When I removed the Public IP adrress from my instance I could not connect to the instance.
