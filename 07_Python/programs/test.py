dict= {"1": "One","2": "Two","3":"Three","4":"Four" }
s = input("Enter your phone nr")
result =" "
for i in s:
    
    result += dict.get(i, "not valid") + " "
    
print (result)