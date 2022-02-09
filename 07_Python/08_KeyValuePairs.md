# [Onderwerp]
[Geef een korte beschrijving van het onderwerp]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Gebruikte bronnen
[Plaats hier de bronnen die je hebt gebruikt.]

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
### Exercise 1:
```
dict = { "First Name" : "XXX", "Last Name" : "AAA", "Job Title" : "Coach", "Id":100}
for i,j in dict.items():
    print(i,j)
for i in dict.values():
    print(i)
```
### Exercise 2:
```

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


```