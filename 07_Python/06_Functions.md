# [Functions]
A function is a block of code that only runs when it is called. Functions are recognizable by the brackets () next to the function name. These brackets serve as a place to input data into a function.
Functions can return data as a result.

Besides the built-in functions, you can also write custom functions, or import functions from a library or package.


## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Exercise 1 :
Create a new script.

Import the random package.

Print 5 random integers with a value between 0 and 100.
### Exercise 2:
Create a new script.

Write a custom function myfunction() that prints “Hello, world!” to the terminal. Call myfunction.

Rewrite your function so that it takes a string as an argument. Then, it should print “Hello, <string>!”.
### Exercise 3 :
Write the custom function avg() so that it returns the average of the given parameters.

### Gebruikte bronnen
[Plaats hier de bronnen die je hebt gebruikt.]

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
### Exercise 1:
```
import random
for i in range (5):
    print ( random.randint(0,100))

```
### Exercise 2:
```
def myfunction():
    print("Hello, World")
myfunction()
```
### Exercise 3:
```
def avg(x,y):
    return((x+y)/2)
x = 128
y = 255
z = avg(x,y)
print("The average of",x,"and",y,"is", z)
```
