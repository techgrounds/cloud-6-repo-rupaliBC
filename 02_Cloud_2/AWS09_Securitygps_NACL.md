# AWS Security Groups and NACL
Security Groups are stateful virtual firewalls that can be assigned to instances. They do not run in the OS, but rather in the VPC.
One Security Group can be assigned to multiple instances. The other way around, one instance can have up to 5 Security Groups.
Security Groups only have allow rules. Everything not explicitly allowed is automatically implicitly denied.

A Network Access Control List (NACL) is a stateless firewall that runs on the subnet level in a VPC.
A NACL has both explicit allow and deny rules. Rules have a number assigned to them. This number indicates the order in which the rules are applied.
By default, a NACL is configured to allow all traffic in and out of the network.


## Key-terms
Stateless Firewall : Security groups are stateful: This means any changes applied to an incoming rule will be automatically applied to the outgoing rule. e.g. If you allow an incoming port 80, the outgoing port 80 will be automatically opened.

Stateful Firewall : Network ACLs are stateless: This means any changes applied to an incoming rule will not be applied to the outgoing rule. e.g. If you allow an incoming port 80, you would also need to apply the rule for outgoing traffic.


## Opdracht
- Security Groups in AWS
- Network Access Control Lists in AWS


### Gebruikte bronnen

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html

https://medium.com/awesome-cloud/aws-difference-between-security-groups-and-network-acls-adc632ea29ae#:~:text=State%3A%20Stateful%20or%20Stateless,applied%20to%20the%20outgoing%20rule%20.&text=Network%20ACLs%20are%20stateless%3A%20This,applied%20to%20the%20outgoing%20rule.

https://medium.com/awesome-cloud/aws-difference-between-security-groups-and-network-acls-adc632ea29ae
### Ervaren problemen

### Resultaat
#### Scope: Subnet or Instance (Where to apply)
Security groups are tied to an instance whereas Network ACLs are tied to the subnet.
Network ACLs are applicable at the subnet level, so any instance in the subnet with an associated NACL will follow rules of NACL. That’s not the case with security groups, security groups has to be assigned explicitly to the instance.
#### State: Stateful or Stateless
Security groups are stateful: This means any changes applied to an incoming rule will be automatically applied to the outgoing rule. e.g. If you allow an incoming port 80, the outgoing port 80 will be automatically opened.
Network ACLs are stateless: This means any changes applied to an incoming rule will not be applied to the outgoing rule. e.g. If you allow an incoming port 80, you would also need to apply the rule for outgoing traffic.
#### Rules: Allow or Deny
Security group support allow rules only (by default all rules are denied). e.g. You cannot deny a certain IP address from establishing a connection.
Network ACL support allow and deny rules. By deny rules, you could explicitly deny a certain IP address to establish a connection 
#### Rule process order
All rules in a security group are applied whereas rules are applied in their order (the rule with the lower number gets processed first) in Network ACL.
i.e. Security groups evaluate all the rules in them before allowing a traffic whereas NACLs do it in the number order, from top to bottom.
#### Defense order
Network ACL first layer of defense, whereas Security group is second layer of the defense for inbound/ingress traffic.
Security group first layer of defense, whereas Network ACL is second layer of the defense for outbound/egress traffic.
#### Occurrence
Subnet can have only one NACL, whereas Instance can have multiple Security groups.

![alt text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/nacl.png)
