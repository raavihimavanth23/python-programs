#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Find the large number from the given 3 numbers
a1 = int(input("Enter number 1 "))
a2 = int(input("Enter number 2 "))
a3 = int(input("Enter number 3 "))

if a1>a2 and a1>a3:
    print(a1, " is the large number ")
elif a2>a1 and a2>a3:
    print(a2, " is the large number ")
else:
    print(a3, " is the large number ")


# In[3]:


# Check if a year is leap year or not
year = int(input("Enter year"))
if year%400 == 0 or (year % 100 != 0  and year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")


# In[4]:


# Need print "Gitam" for 5 times
print("Gitam")
print("Gitam")
print("Gitam")
print("Gitam")
print("Gitam")


# In[5]:


x = 0
while x < 5 :
    print("Gitam")
    x = x + 1


# In[6]:


# Print N Natural numbers using while loop
# Input - 10
# Output - 1 2 3 ..... 10
n = int(input("Enter a Number"))
i = 1
while i <= n :
    print(i,end = " ")
    i = i + 1


# In[7]:


# Read a Number -- n
# Add only even numbers between 1 to n
# Input -- 10
# Output -- 30(2 + 4 + 6 + 8 + 10)
n = int(input('Enter a number '))
i = 1
sum = 0
while i <= n:
    if i % 2 == 0:
        sum =  sum + i
    i = i + 1

print(sum)


# In[8]:


# Number as a Number -- 123
# Print the digits of given number : 3 2 1
n = int(input('Enter a number '))
while n != 0:
    r = n % 10
    print(r,end = "  ")
    n = n // 10


# In[12]:


def nameoftheFunction(<Parameters>):
    Statement
    return


# In[11]:


# Read a number -- 1234
# Output -- 6(2+4)
def addEvenDigits(n):
    sum = 0
    while n!= 0:
        r = n % 10
        if r % 2 == 0:
            sum = sum + r
        n = n // 10    
    return sum
addEvenDigits(1234)


# In[13]:


# Read a number -- 19528
# Print the large digit print the number
def printLarge(n):
    large = 0
    while n != 0:
        r = n % 10
        if large < r:
            large = r
        n = n // 10
    return large
printLarge(19528)


# In[14]:


# Read a number Input
# Output reverse of the given number
# 123 -- 321
def reverseNumber(n):
    rev = 0
    while n != 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    return rev
reverseNumber(123)


# In[15]:


# Given number is palidrome or not
# input
# 123 -- 321  -- No
# 121 -- 121  -- Yes
def isPalindrome(n):
    rev = 0
    buffer = n
    while n != 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    if buffer == rev:
        return "Yes"
    else:
        return "No"

print(isPalindrome(123))
print(isPalindrome(121))


# In[16]:


#Function to print N Natural numbers with for loop
def printNNaturalNumbers(n):
    for x in range(1,n+1):
        print(x,end=" ")
    return
printNNaturalNumbers(10)


# In[17]:


# Function to print the numbers between two limits
# input : 11,25 
# Output: 11 12 13 ............. 25
def printSeries(lb,ub):
    for x in range(lb,ub+1):
        print(x,end=" ")
    return 
printSeries(11,25)


# In[18]:


# Function to print alternate numbers
# [500,520] -- 500 502 504 506 508 .... 520
# [100,150] -- 100 104 108 112 116
def alternateNumbers(lb,ub):
    for x in range(lb,ub+1,4):
        print(x,end=" ")
    return
alternateNumbers(100,150)


# In[19]:


# Function to print the series in reverse
# Input -- 1,10 
# Output : 10 9 8 7 6 .... 1
def reverseRange(start,end):
    for x in range(end,start-1,-1):
        print(x,end =" ")
    return
reverseRange(1,10)


# In[20]:


# Problem Name
# Algorithm
# Sample Input and Output 
# Flowchart
# Python Code


# In[ ]:




