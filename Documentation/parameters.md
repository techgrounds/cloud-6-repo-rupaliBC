## Parameters:

### VPC Parameters

| Parameters       | Value         |
| ---------------- | ------------- |
| vpc1_id          | Web_VPC       |
| vpc1_max_az      | 2             |
| vpc1_subnet_name | Public        |
| vpc1_cidr_range  | 10.10.10.0/24 |
| vpc2_id          | Mgmt_VPC      |
| vpc2_max_az      | 2             |
| vpc2_subnet_name | Public        |
| vpc2_cidr_range  | 10.20.20.0/24 |
| peering_id       | VPCPeering    |
| peering_region   | eu-central-1  |
| vpc1_route_id    | vpc1_route_id |
| vpc2_route_id    | vpc2_route_id |


### Security Groups

| Parameters | Value                  |
| ---------- | -------------------- |
| mgsg_id    | MgmtSG               |
| mgsg_name  | MgmtServerSG         |
| mgsg_peer  | **77.248.14.193/32** |
| websg_id   | WebSG                |
| websg_name | WebServerSG          |


### EC2 Instances

| Parameters         | Value      |
| ------------------ | ---------- |
| web_instance_id    | webserver  |
| web_instance_type  | t2.micro   |
| web_volume_size    | 8          |
| mgmt_instance_id   | mgmtserver |
| mgmt_instance_type | t2.micro   |
| mgmt_volume_size   | 8          |

  