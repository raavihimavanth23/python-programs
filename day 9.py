#!/usr/bin/env python
# coding: utf-8

# In[1]:


lst = [1,8,16,9,2]
print(lst) # Access the entire list
print(lst[0]) # Access the first item list
print(lst[1]) # Access the second item list
print(lst[-1]) # Access the Last item list
print(lst[-2])
print(lst[1:])
print(lst[1:4])


# In[2]:


# Update the list item values using index (Direct Referncing)
li = ["Gitam","Python",1989,2002]
print(li)
li[2] = 2019
print(li)


# In[3]:


# delete the specific item in the list
print(li)
del li[2]
print(li)


# In[4]:


# Basic List Operations
lst1 = [1,9,6,18,2]
print(len(lst1)) # len of the list
print(lst1 * 2) # Repetation
print(len(lst1)) 
print(9 in lst1) # list item is present or not
print(15 in lst1)
# Access the list items using iteration
for x in range(len(lst1)):
    print(lst1[x],end=' ')


# In[5]:


# Function of the list
lst1
print(min(lst1)) # Min item/element of the list
print(max(lst1)) # Max element of the list
print(sum(lst1)) # sum of the all elememts of the list
print(sum(lst1)//len(lst1)) # Average of list elements
print(sum(lst1[1::2])/len(lst1[1::2])) # Average of all the alternate elements


# In[6]:


# Methods of List Object
lst1
lst1.append(24) # Adding a new element at the end of the list
lst1
lst1.insert(2,56) # Adding an element at particular index
lst1
lst1.count(18) # return the value how many times the object repeated
lst1.index(56)
lst1.sort() # It's sort the list in ascending order
lst1
lst1.pop() # remove the last element from the list
lst1
lst1.pop(1) # Remove an element from a particular index
lst2 = [123,23,45]
lst1.extend(lst2) # Merge the list2 into list1
lst1.reverse() # reverse the list
lst1.remove(123) # remove the element from the list
lst1


# In[7]:


lst1


# In[8]:


li = [1,9,8,2,6,3]
print(li[-1:2:-2])


# In[9]:


# Function to find the second large item from the list
# Input  :   [1,19,6,2,8,18,3]
# Output :   18
def secondLarge(li):
    li.sort()
    return li[-2]
def genericLarge(li,n):
    li.sort()
    return li[-n]
li = [1,19,6,2,8,18,3]
genericLarge(li,4)


# In[10]:


# Function to find the least item from the list
# Input  :   [1,19,6,2,8,18,3]
# Output :   2 
def secondLeast(li):
    li.sort()
    return li[1]
def genericLeast(li,n):
    li.sort()
    return li[n-1]
li = [1,19,6,2,8,18,3]
genericLeast(li,4)


# In[11]:


# Function to search the data in a list
# Search is found then return the index if not return -1
def linearSearch1(li,tarItem):
    for x in range(len(li)):
        if li[x] == tarItem:
            return x
    return -1
li = [1,19,6,2,8,18,3]
linearSearch1(li,225)


# In[12]:


# Function 
# Input : [1,5,9,6,5,15,1,2,5],key=5 # Duplicate
# Output : 1 4 8
def linearSearch2(li,tarItem):
    for x in range(len(li)):
        if li[x] == tarItem:
            print(x,end=" ")
    return
li = [1,5,9,6,5,15,1,2,5]
linearSearch2(li,5) # 1 4 8


# In[13]:


# Fuction 
# Input : List
# Ouput : Seq of characters
# Test case
# [1,5,9,6,5,15,1,2,5],tar=5 -- !! !!!!! !!!!!!!!!
def linearSearch3(li,tarItem):
    # Implement the logic
    for x in range(len(li)):
        if li[x] == tarItem:
            j = 0
            while j != x+1:
                print("!",end="")
                j = j + 1
            print(end=" ")
    return
li = [1,5,9,6,5,15,1,2,5]
linearSearch3(li,5) # !! !!!!! !!!!!!!!!


# In[14]:


# Function
# Input : List
# Output : Formatted
# Test case:
# [12,2,45,9,18,15,36] -- 60
# A list item which is perfectly multiple of 3 and 5
def linearSearch4(li):
    sum = 0
    for x in range(len(li)):
        if li[x] % 3 == 0 and li[x] % 5 == 0:
            sum += li[x] # sum = sum + li[x]
    return sum
li = [12,2,45,9,18,15,36]
linearSearch4(li) # 60


# In[15]:


# Function
# Input  : List
# Output : Formatted Output
# Test Case :
# [1,2,3,4,5] -- [1,3,8,15,5]
# [6,5,2,8,2] -- [6,12,40,4,2]
def linearSearch5(li):
    for x in range(len(li)):
        if x == 0 or x == len(li) - 1:
            print(li[x],end=" ")
        else:
            print(li[x-1]*li[x+1],end=" ")
    return
li = [1,2,3,4,5]
linearSearch5(li)


# In[16]:


# Function
# Input  : List
# Output : Formatted Output
# Test cases:
# [1,6,9,4,16,19,22] -- 1 9 19 22
def linearSearch6(li):
    # Implement the logic
    for x in range(len(li)):
        if x == 0 or x == len(li) - 1:
            print(li[x],end=" ")
        elif li[x-1] % 2 == 0 and li[x+1] % 2 == 0:
            print(li[x],end=" ")
    return
li = [1,6,9,4,16,19,22]
linearSearch6(li) #  1 9 19 22


# In[17]:


# Function for Converstion - Number to List
# Input  -- Number
# Output -- list
# Test Cases:-
# 14569 -- [1,4,5,6,9]
# 1990  -- [1,9,9,0]
def numberListConversion(n):
    li = []
    while n != 0:
        r = n % 10
        li.append(r)
        n = n // 10
    li.reverse()
    return li
numberListConversion(14569)#[1,4,5,6,9]


# In[18]:


# Function to count the occurances of a character in a string
# "Python Programming", P -> 2
# "Python Programming", m -> 2
def countCharOccurances(s,c):
    cnt = 0
    for ch in s:
        if ch == c:
            cnt += 1
    return cnt
def countCharOccurances1(s,c):
    return s.count(c)
countCharOccurances1("Python Programming",'m')


# In[19]:


#Function to convert the string to list
# Test Case
# "1 2 3 4 5 6" -- [1,2,3,4,5,6]
def strintToListConversion(s):
    li = s.split()
    numberslist = []
    for i in li:
        numberslist.append(int(i))
    return numberslist
s = "1 2 3 4 5 6"
strintToListConversion(s) # [1,2,3,4,5,6]


# In[20]:


# Function to represent tht Bubble sort
def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]            
    return li
li = [19,1,25,6,18,3]
bubbleSort(li)


# In[ ]:




