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