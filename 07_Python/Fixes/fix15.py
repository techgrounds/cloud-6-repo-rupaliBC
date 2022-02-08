'''
The output should be:
a5|||5|||5|||a5|||5|||5|||a5|||5|||5|||
'''

x = ''
for i in range (3):
    x+='a'
    for j in range (3):
        x+='5'
        for k in range(3):
            x+='|'
print (x)
