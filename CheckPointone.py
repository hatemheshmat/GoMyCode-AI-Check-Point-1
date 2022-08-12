#!/usr/bin/env python
# coding: utf-8

# In[14]:


listRang = []
for x in range(2000 , 3200 ):
    if x%7 == 0 and x%5 > 1:
        listRang.append(x)
listRang
print(None)


# In[12]:


def Factorial(n):
  if (n==1 or n == 0):
    result = 1
  else:
    result = n*Factorial(n-1)
  return result
print("pls enter number that you need the factorial of it")
number = input() 
print("\n Factorial of Number "+number+" is "+str(Factorial(int(number))))


# In[27]:


number = int(input())
my_dictionary = dict()
for n in range(1, number+1):
    my_dictionary[n] = (n*n)
my_dictionary


# In[37]:


number = int(input())
string = "kitten"
print(string[:number-len(string)]+string[number+1-len(string):])
#negative indexes to start the slice from the end of the string


# In[39]:


import numpy as np
new_array = np.array([[1,2,3]
                      ,[4,5,6]])
new_array.tolist()


# In[40]:


import numpy as np
array1 = np.array([[0,1,2]])
array2 = np.array([[2,1,0]])
np.cov(array1,array2)


# In[71]:


import math as math
dinput = '100,150,180'
List = list(map(int, 
               [dinput.split(',')[0],
        dinput.split(',')[1],
       dinput.split(',')[2]]))
dListoutput=[]
for dIteam in List:
    C= 50
    H = 30
    dListoutput.append(int(math.sqrt((2*C*dIteam)/H)))
dListoutput


# In[ ]:




