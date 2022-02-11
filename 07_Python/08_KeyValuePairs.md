# Key Value Pairs
Key-value pairs are a general concept you will definitely encounter. Some examples of where you will find them are NoSQL databases or AWS resource tags. Dictionaries (dict) in Python also use key-value pairs to store information.

Dicts in Python are written using curly brackets {}. You can get values from the dict by calling its key. 

## Key-terms

## Opdracht
Exercise 1:

Create a new script.

Create a dictionary with keys and values

Loop over the dictionary and print every key-value pair in the terminal.

Exercise 2:

Create a new script.

Use user input to ask for their information (first name, last name, job title, company). 

Store the information in a dictionary.
Write the information to a csv file (comma-separated values). 

The data should not be overwritten when you run the script multiple times.



### Gebruikte bronnen

### Ervaren problemen


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