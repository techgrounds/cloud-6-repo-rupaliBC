

dict= { "Fname" : input ("Enter Your First Name "), 
        "LName": input ("Enter Your Last Name "),
        "Job": input ( "Enter Your Job Title "),
        "Company":input( "Enter your Company Name ")
        } 

print(dict)
import csv

with open('newfile.csv','a',encoding='UTF-8',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(dict.items())
