# Conditions
Very often, you will want to run a piece of code only when certain conditions are met. For example, you might want to write something to an error log only if an error occurred.
Python makes use of the if, elif, and else statements.


## Key-terms

## Opdracht

### Exercise 1:
Create a new script.

Use the input() function to ask the user of your script for their name. 

If the name they input is your name, print a personalized welcome message. 

If not, print a different personalized message.
### Exercise 2:
Create a new script.

Ask the user of your script for a number.

Give them a response based on whether the number is higher than, lower than, or equal to 100.


### Gebruikte bronnen

### Ervaren problemen



### Resultaat
### exercise 1:
```
name = "Tom"
x = input ("Please enter your name:  ")
if ( x == name):
    print("Hi, " + x)
else: 
    print( "You are not " + name)
```
### Exercise 2:
```

while True:
    x = input ("Enter your number ")
    x = int(x)
    if x < 100:
        print( " The number is smaller than 100 ")
    elif x > 100:
        print( " The number is greater than 100 ")
    else:
        print( " The number is equal to 100 ")
        break
    ```