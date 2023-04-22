#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num=int(input('Enter a number to find factorial'))
f=num
while(True):
    num=num-1
    if(num==1):
        break
    else:
        f=f*num
        continue
print('Factorial is ', f)        
        


# In[ ]:


# Prime or composite
num=int(input('Enter a number'))
i=num

if(i==1):
    print(num,' is neither prime nor composite')
        
elif(i==2):
    print(num," is prime")
else:
    if(num%2==0):
        print(num," is composite number")
    else:
        print(num," is prime number")
        
        


# In[ ]:


#palindrome
num=int(input('Enter a number '))
n=num
p=0
while(True):
    if(num//10==0):
        break
    else:
        i=num//10
        num=i
        p=p*10+i
        
        continue
    
if(p==n):
    
    print(n,' is palindrome')
else:
    print(n,' is not palindrome')


# In[7]:


# Third side of right angled triangle
import numpy as np
third_side=str(input('Enter which side you want to find(oppposite/hypotenuse/adjacent)'))
if(third_side=='opp'):
    a=int(input('Enter Hypotenuse value'))
    b=int(input('Enter Adjacent value'))
    c=int((a**2-b**2)**0.5)
elif(third_side=='adj'):
    a=int(input('Enter Hypotenuse value'))
    b=int(input('Enter opposite value'))
    c=int((a**2-b**2)**0.5)
else:
    a=int(input('Enter opposite value'))
    b=int(input('Enter Adjacent value'))
    c=int((a**2+b**2)**0.5)
print('Value of third side is ',c)    
    


# In[8]:


word=str(input('Enter a word to find frequnct'))
f={}
for i in word:
    if i in f:
        f[i]+=1
    else :
        f[i]=1
print('count of all characters is ',f)        


# In[ ]:




