# AWS Security Groups and NACL
Security Groups are stateful virtual firewalls that can be assigned to instances. They do not run in the OS, but rather in the VPC.
One Security Group can be assigned to multiple instances. The other way around, one instance can have up to 5 Security Groups.
Security Groups only have allow rules. Everything not explicitly allowed is automatically implicitly denied.

A Network Access Control List (NACL) is a stateless firewall that runs on the subnet level in a VPC.
A NACL has both explicit allow and deny rules. Rules have a number assigned to them. This number indicates the order in which the rules are applied.
By default, a NACL is configured to allow all traffic in and out of the network.


## Key-terms



## Opdracht
- Security Groups in AWS
- Network Access Control Lists in AWS


### Gebruikte bronnen


### Ervaren problemen

### Resultaat


![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/.png)