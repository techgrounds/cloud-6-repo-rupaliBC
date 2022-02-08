from re import X

list = [9,80,16,67,35]
res = [sum(sub) for sub in zip(list, list[1:] + [list[0]])]  
print (res)
##for i in range(len(list)-1):
  ##  print (list[i]+list[i+1])
  ##  if i==len(list)-1:
  ##   print(list[0]+list[-1])