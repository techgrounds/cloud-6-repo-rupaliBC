# Data Types
Under the hood, a computer can only see strings of zeros and ones. Programming languages make use of data types to tell the computer how to interpret those strings.
For example, when the computer needs to read the binary string 01000001, it will need to know the data type to determine whether it means 65 or “A”.

This is a non exhaustive list of some important data types in Python:
- Boolean

A binary state that is either True or False.
- string

Technically an array of characters. Strings are denoted using “ ” double quotes or ‘ ’ single quotes.
- int

An integer is a whole number. Ints can be both positive and negative.
- float

A floating-point number is a decimal number.


## Key-terms


## Opdracht
### Exercise 1
Determine the data types of all four variables (a, b, c, d) using a built in function.

Make a new variable x and give it the value b + d. 

Print the value of x.
This will raise an error. 
 
 Fix it so that print(x) prints a float.

Write a comment above every line of code that tells the reader what is going on in your script.

#### Exercise 2:

Create a new script.
Use the input() function to get input from the user.

Store that input in a variable.

Find out what data type the output of input() is.

See if it is different for different kinds of input (numbers, words, etc.).


### Gebruikte bronnen


### Ervaren problemen


### Resultaat
### Exercise 1 :
```
a = 'int' 
b = 7
c = False
d = "18.5"
print ("Data type of a is " )
print (type (a)) # to find out data type
print ("Data type of b is " )
print (type (b)) # to find out data type
print ("Data type of c is " )
print (type(c)) # to find out data type
print ("Data type of d is " )
print ( type(d)) # to find out data type
d = float (d) # convert string to float
print (b+d) # Adding 2 numbers 
```
### Exercise 2:
```
x = input ('Enter your name   ' )
print (type(x))
```