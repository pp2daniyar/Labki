import re 
a=input()
f=re.findall('bb{2}',a)
print(len(f))