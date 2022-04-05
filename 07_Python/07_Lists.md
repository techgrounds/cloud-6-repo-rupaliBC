# Lists
You can declare a list of values in a single variable. A list is represented by square brackets [], and each value is separated by a comma.

Each position in a list has a number associated with it called the index. Indexes start at 0, so the first item in a list will have the index 0. The second item will have index 1, etc. You can call individual items in a list by calling its index.

You can loop over a list using a for loop. Instead of a number within a range, i (or whatever you name the variable you declare) will have the value of an item in the list. You can still use range() to loop over a list. In this case, i will be used to call an index in a list.


## Key-terms

## Opdracht
### Exercise 1:
Create a new script.

Create a variable that contains a list of five names.

Loop over the list using a for loop.

Print every individual name in the list on a new line.
### Exercise 2:
Create a new script.

Create a list of five integers.

Use a for loop to do the following for every item in the list:

Print the value of that item added to the value of the next item in the list.
If it is the last item, add it to the value of the first item instead (since there is no next item).

### Gebruikte bronnen


### Ervaren problemen

### Resultaat
### Exercise 1
```
x = ["xxx","yyy","zzz","aaa","bbb"]
for i in x:
    print (i)
```
### Exercise 2
```

list = [9,80,16,67,35]
res = [sum(sub) for sub in zip(list, list[1:] + [list[0]])]  
print (res)
for i in range(len(list)):
    
    if i==len(list)-1:
      print(list[0]+list[i])
    else:
      print (list[i]+list[i+1])
```