#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, Gitam")


# In[2]:


print("Hello, Gitam")
print("Hyderabad")


# In[3]:


print("Hello, Gitam", " ||| ",end = " ")
print("Hyderabad",end=" ||| ")
print("Python Programming")


# In[4]:


n1 = 100 # single Variable Assignment
a = b = c = 20 # Multi Variable Assignment of the same value
a1,b1,c1 = 111,222,333 # Multi Variable Assignment with different values
print(n1)
print(a,b,c)
print(a1,b1,c1)


# # Data types and Conversions
# .int
# .float
# .string

# In[5]:


a = 100;
s1 = "Python"
s2 = 'P'
f1 = 10.2
print(a,s1,s2,f1)
print(type(a),type(s1),type(s2),type(f1))


# In[6]:


i = 100
print(type(i))
s1 = str(i) # str() converts the input into string type
print(type(s1))
f1 = float(i) # float() converts the input into float type
print(type(f1))


# In[7]:


s1 = "100"
print(type(s1))
a = int(s1)
print(type(a))
f = 1.5
a1 = int(f)
print(type(a1))
print(a1)


# In[8]:


# A number is given 1234 -
# Digit count
a1 = 1234
print(len(str(a1)))


# In[9]:


s1 = input("Enter your name")
print(s1)
print(type(s1))


# In[10]:


# Want a number as a input
n1 = int(input("Enter a number"))
print(n1,type(n1))


# In[11]:


n1 = 1234
print(n1+10)
print(n1-10)
print(n1*10)
print(n1/10)
print(n1%10)
print(n1//10)
print(n1**10)


# In[12]:


x = 1 + 2 ** 3 / 4 + 5 
print(x)


# In[13]:


x = 1 + 2 ** 3 / 4 * 5 
print(x)


# In[14]:


x = 10
a1 = x > 15
print(a1)


# In[15]:


i = 100
a1 = (i > 15) and (i < 800)
a2 = (i > 15) and (i > 800)
print(a1)
print(a2)


# In[16]:


# To check given number is even or odd
n = int(input("Enter a number"))
if n%2 == 0:
    print("Even")
else:
    print("Odd")


# In[17]:


# To check given number is perfectly multiple of 3 and 5
n = int(input("Enter a number"))
if n%3 == 0 and n%5 == 0:
    print("Yes")
else:
    print("No")


# In[18]:


# test given number is positive, Negative or Zero
n = int(input("Enter a number"))
if n == 0:
    print("Zero")
elif n>0:
    print("Positive Number")
elif n<0:
    print("Negative number")


# In[ ]:




