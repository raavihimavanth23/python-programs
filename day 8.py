#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Find the factors of a given number
# 12 -- > 1 2 3 4 6 12
def factorsList(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=" ")
    return
factorsList(12)


# In[2]:


# Given number is Prime number or not
def isPrime(n):
    flag = True
    for i in range(2,n//2+1):
        if n % i == 0:
            flag = False
            return flag
    return flag
isPrime(11)


# In[3]:


# Function to find Prime numbers count from 1 to N
# 10 -- 4(2,3,5,7)
def primeCount(n):
    cnt = 0 
    for a in range(2,n+1):
        k = 0
        for i in range(2,a//2+1):
            if a % i == 0:
                k = k + 1
        if(k<=0):
            cnt = cnt + 1
    return cnt
print(primeCount(10))


# In[4]:


# Individual digit factorial sum is same as original number
# Example :-
# 145 -- Yes (5! + 4! + 1! = 145)
# 123 -- No  (3! + 2! + 1! = 9)
# Strong Number
def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact
def digitFactSum(n):
    sum = 0
    buffer = n
    while n != 0 :
        r = n % 10
        sum += factorial(r)
        n = n // 10        
    if sum == buffer:
        return "Yes"
    else:
        return "No"
    return 
print(digitFactSum(145))
print(digitFactSum(123))


# In[5]:


# Function to return the count of Palindrome number two limits
# Input : 1 10 
# Output: 9 (1,2,3,4,5,6,7,8,9)

# Input : 11 100
# output : 9(11,22,33,....,99)
def isPalindrome(n):
    rev = 0
    buffer = n
    while n!= 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    if rev == buffer:
        return True
    else:
        return False
    return

def countPalindrome(lb,ub):
    cnt = 0
    while lb != ub:
        # Implement
        if isPalindrome(lb) == True:
            cnt = cnt + 1
        lb = lb + 1
    return cnt
countPalindrome(1,10)


# In[6]:


# Function to generate the perfect numbers in a given range
# Perfect Number : Sum of all its factors same as original number 
# Example : 6 -- 1 2 3 (1 + 2 + 3)
# Input : 1 10
# Output : 6
def factorsList(n):
    sum = 0
    for i in range(1,n//2+1):
        if n % i == 0:
            sum = sum + i        
    return sum
def isPerfect(n):
    if factorsList(n) == n:
        return True
    return False
def generatePerfect(lb,ub):
    for x in range(lb,ub+1):
        if isPerfect(x):
            print(x,end = " ")
    print()
    return

generatePerfect(1,10)
generatePerfect(1,10000)


# In[7]:


s1 = 'Python'
print(s1)
print(type(s1))


# In[8]:


s1 = 'Python'
print(s1[0]) # Access the first character
print(s1[1]) # Access the second character
print(s1[5]) # Last character
print(s1[len(s1)-1]) # Access the last character


# In[9]:


print(s1[-1]) #Another way Access the last charcter
print(s1[-2]) # Another wayt to access the last second character
print(s1[0:2]) # Access the first characters
print(s1[:2]) # Access the first characters
print(s1[-3:]) # Last three characters
print(s1[2:]) # From second character to last character


# In[10]:


print(s1[1:-1]) # printing all character expect first and last
print(s1[len(s1)//2]) # Middle of the string
print(s1[-1::-1]) # Reverse of the string
print(s1[-1:-3:-1]) # Access the last two characters in reverse order
# Access the alternate characters
print(s1[::2]) # two characters 
print(s1[::3]) # three characters
print(s1[::-2]) # from reverese order


# In[11]:


def reverseString(str):
    return str[-1::-1]
reverseString("Programming")


# In[12]:


def isPalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
    return 
print(isPalindrome("Python"))
print(isPalindrome('ganag'))


# In[13]:


def isPalindrome(str):
    return str == str[::-1]
print(isPalindrome("Python"))
print(isPalindrome('ganag'))


# In[14]:


# Function to print the Upper case characters
# Example:- PyThon -- P T
# ASCII :-
# A - Z : 65 - 90
# a - z : 97 - 122
# 0- 9  : 48 - 57
# space : 32
def printUpper(x):
    for i in range(len(x)):
        if ord(x[i]) >= 65 and ord(x[i]) <= 90:
            print(x[i],end = " ")
    return
printUpper("PyThon")


# In[15]:


ord('A') # It give you the equ ascii number for input character


# In[16]:


# Function to print "SameCount" if the count of 
# Upper and lower case is same
# Print "Programming" if not same
# Example : PyThOn -- 3 P T O (Upper case) -- SameCount
#                     3 y h n (Lower case)
# PytHon -- P H  (2)
#        -- y t o n (4) - Programming
def findCount(str):
    cntUpper = 0
    cntLower = 0
    for x in range(len(str)):
        if ord(str[x]) >= 65 and ord(str[x]) <= 90:
            cntUpper = cntUpper + 1
        elif ord(str[x]) >= 97 and ord(str[x]) <= 122:
            cntLower = cntLower + 1
    if cntUpper == cntLower:
        return "SameCount"
    else:
        return "Programming"
    return
print(findCount('PyThOn')) # SameCount
print(findCount('PYTHon')) # Programming


# In[17]:


# Extract digits from given string
# Example:
# Input : Appli1cat8ion89
# Output : 1 8 8 9
def extractDigits(str):
    for x in range(len(str)):
        if ord(str[x]) >= 48  and ord(str[x]) <= 57:
            print(str[x],end=" ")
    return
extractDigits("Appli1cat8ion89") # 1 8 8 9


# In[18]:


# Function to return the sum of digits in a given string
# Example : 
# Input : Appli1cat8ion89
# Output: 26(1+8+8+9)
# 0 1 2 3 4 5 ... 9
# 48 49 50 51 52 53 ... 57
def sumOfDigits(str):
    sum = 0
    for x in range(len(str)):
        if ord(str[x]) >= 48 and ord(str[x]) <= 57:
            sum = sum + (ord(str[x])-48)
    return sum
sumOfDigits('Appli1cat8ion89')


# In[19]:


# Function to return the sum of digits in a given string
# Example : 
# Input : Appli1cat8ion89
# Output: 16(8+8)
def sumOfEvenDigits(str):
    sum = 0
    for x in range(len(str)):
        if ord(str[x]) >= 48 and ord(str[x]) <= 57:
            if (ord(str[x])-48) % 2 == 0:
                sum = sum + (ord(str[x])-48)            
    return sum
sumOfEvenDigits('Appli1cat8ion89')


# In[20]:


# Function to print the Specific Word in Upper case
# Example:
# Input : Python Made Easy
# Output : MADE
# Input : Learn Python Programming
# Output : PYTHON
def wordUpperCase(s):
    spaceCnt = 0
    for x in range(len(s)):        
        if ord(s[x]) == 32:
            spaceCnt += 1 # spaceCnt = spaceCnt + 1           
        if spaceCnt == 1:
            if ord(s[x]) >= 65 and ord(s[x]) <= 90:
                print(s[x],end="")
            elif ord(s[x]) >= 97 and ord(s[x]) <= 122 :
                print(chr(ord(s[x])-32),end="")
        if spaceCnt == 2:
            break
    return
wordUpperCase('Python Made Easy') # MADE


# In[21]:


print('hello')


# In[ ]:




