## Parameters:
Here is the list of all parameters that the script is using. The CDK.json file has to be updated with the required value.The parameters are self explainatory and the values are as per requirement for this project.


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

### **Server BackUps**  
| Parameters | Value  |
| ---------- | ------ |
| hour1      | 07     |
| minute1    | 30     |
| day1       | \*     |
| month1     | \*     |
| year1      | \*     |
| duration1  | 7 days |
| hour2      | 07     |
| minute2    | 30     |
| day2       | \*     |
| month2     | \*     |
| year2      | \*     |
| duration2  | 7 days |
