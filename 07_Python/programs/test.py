'''
dict= {"1": "One","2": "Two","3":"Three","4":"Four" }
s = input("Enter your phone nr")
result =" "
for i in s:
    
    result += dict.get(i, "not valid") + " "
    
print (result)

ss=["rr","tt","gg","tt"]
ss.append("q")
print (ss)

for i in range(20,100,10):
    print (i)

try:
  f = open("C:\\Users\rupal\"demofile.txt","a")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
for i in range(1,8):
  print ("K"* i)
  '''
var=1
var2= "3"
f=var+var2
print(f)