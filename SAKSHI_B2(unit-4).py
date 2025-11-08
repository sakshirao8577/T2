#!/usr/bin/env python
# coding: utf-8

# ## Immutable data structure

# ###    1. String

# #### Access the characters of string

# 1. By using index

# In[3]:


s="Hello World"
print(s[2])
print(s[5])
print(s[20])


# In[2]:


s="Arman"
print(s[3])
print(s[-2])


# 2. By using slicing operator

#     Syntax---> s[begin index:end index:step] 

# In[10]:


s="Learning Python is very easy."
print(s[1:7:1])
print(s[1:7])
print(s[:7])
print(s[5:])
print(s[1:7:2])
print(s[::2])
print(s[:])
print(s[::])
print(s[::-1]) #only for string not for number
print(s[-5::])
print(s[-5:-1:])
print(s[7:1:-1])


# ### Check whether the given string is palindrome or not
# 

# In[15]:


s=input("Enter string:")
str=s[::-1]
if(str==s):
    print(s,"is a palindrome string")
else:
    print(s,"not a palindrome string")


# ## Mathematical operators for string

#     + ---> String concatenation
#     * ---> String repetation
# 

# In[16]:


print("Arman"+"Arman")
print("Arman"*3)


# ### Comparison of String

# In[20]:


s1=input("Enter string 1:")
s2=input("Enter string 2:")
if(s1==s2):
    print("Both strings are equal.")
elif(s1<s2):
    print("Second string is greater.")
else:
    print("First string is greater.")


# ### Joining of string
# 

# Join a group of strings wrt the given separator

# Syntax---> s=separator.join(group of string)

# In[21]:


t=("Arman","Aryan","Dhairya")
x="$".join(t)
print(x)


# ### Formatting of string

# In[24]:


name="Aryan"
salary=40000
age=24
print("{}'s salary is {} and age is {}".format(name,salary,age))
print("{0}'s salary is {1} and age is {2}".format(name,salary,age))


# ## Important functions of string

# 1. len()

# In[25]:


s="Aryan"
print(len(s))


# ### Removing spaces from string
# 1. lstrip()
# 2. rstrip()
# 3. strip()

# In[27]:


s="banana "
print(len(s))
x=s.rstrip()
print(x)
print(len(x))


# In[29]:


s="  banana"
print(s)
x=s.lstrip()
print(x)


# In[30]:


s="  banana  "
print(s)
x=s.strip()
print(x)


# In[31]:


s="banana"
x=s.rstrip("a")
print(x)


# In[32]:


s="banana "
x=s.rstrip("a")
print(x)


# In[34]:


s="banana"
x=s.rstrip("na")
print(x)


# In[35]:


s="bamana"
x=s.rstrip("na")
print(x)


# In[36]:


s="banana"
x=s.lstrip("b")
print(x)


# ### Changing the case of string
# 

# 1. upper()
# 2. lower()
# 3. swapcase()
# 4. title()
# 5. capitalize()

# In[39]:


s="Hello World"
x=s.upper()
y=s.lower()
print(x)
print(y)
z=s.swapcase()
print(z)


# In[40]:


s="HELLO HOW ARE YOU"
x=s.title()
print(x)
y=s.capitalize()
print(y)


# ### To check type of characters present in a string(check function)

# ---> Answer only in True or False

# 1. isalnum()
#        Returns True if all characters are alphanumeric(a-z,A-Z,0-9)

# In[41]:


x="Company123"
print(x.isalnum())


# In[42]:


x="Company 123"
print(x.isalnum())


# 2. isalpha()
# 3. isdigit()
# 4. isnumeric()

# In[45]:


x="CompanyX"
print(x.isalpha())
y="Company 123"
print(y.isalpha())


# In[46]:


x="50525"
print(x.isdigit())
y="50525xyz"
print(y.isdigit())


# ### Casing
# 1. islower()
# 2. isupper()

# In[47]:


t="hello world"
x=t.islower()
print(x)


# In[48]:


t="Hello"
x=t.isupper()
print(x)


# 3. istitle()
# 

# In[50]:


t="Hello How Are You"
x=t.istitle()
print(x)


# In[51]:


a="22 Names"
b="This Is %?"
print(a.istitle())
print(b.istitle())


# 4. isidentifier()

# In[54]:


a="MyFolder"
b="Demo2002"
c="2bring"
d="my demo"
e="mu_demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
print(e.isidentifier())


# 5. isspace()
# 

# In[55]:


t=" "
x=t.isspace()
print(x)


# ### Count number of spaces

# In[57]:


s="Hello How Are You"
count=0
for i in range(len(s)):
    if(s[i].isspace()):
        count+=1
    else:
        continue
print(count)


# In[59]:


s="Hello How Are You"
count=0
for i in s:
    if(i.isspace()):
        count+=1
    else:
        continue
print(count)
print("No.of words:",count+1)


# In[62]:


s="Hello How Are You"
charcount=0
lowcount=0
upcount=0
for i in s:
    if(i.isalpha()):
        charcount+=1
        if(i.islower()):
            lowcount+=1
        elif(i.isupper()):
            upcount+=1
print("Total:",charcount)
print("Lower:",lowcount)
print("Upper:",upcount)


# In[67]:


s=input("enter string:")
n=len(s)
if(n%2==0):
    print(s)
else:
    mid=n//2
    print(s[0],s[mid],s[n-1])


# In[69]:


s="Py$t00567@23hon@_"
chcount=0
dicount=0
spcount=0
sum=0
for i in s:
    if(i.isalpha()):
        chcount+=1
    elif(i.isdigit()):
        dicount+=1
        sum=sum+int(i)
    else:
        spcount+=1
avg=sum/dicount
print(chcount)
print(dicount)
print(spcount)
print(sum)
print(avg)


# ### find()
# Returns index of first occurence of the given substring 
# if it is not available then we will get -1
# #### Syntax---> s.find(substring)

# In[9]:


s="Learning Python is very easy."
print(s.find("a"))
print(s.find("s"))
print(s.find("x"))
print(s.find(" "))
print(s.find("Python"))
print(s.find("s v"))
print(s.find("a",3,))


# ### count()

# In[14]:


s="abcd abcxyz abcdefgh"
print(s.count("a"))
print(s.count("abc"))
print(s.count("abcd"))
print(s.count("i"))
print(s.count(" "))
print(s.count("a",8,15))


# ### replace()
# To replace old string with new string.
# #### Syntax---> s.replace(old string,new string)

# In[19]:


s="Learning Java is easy."
x=s.replace("Java","Python")
y=s.replace("a","A")
print(x)
print(y)


# ### split()
#      split(separator)---> we can split the given string accordinf to specified separator by using split() method.
#                      ---> default separator is space
#                      ---> The return type of split() method is list

# In[25]:


s="Hello     World"
l=s.split()
m=s.split("l")
print(l)
print(m)


# In[24]:


s="29-10-2025"
l=s.split("-")
print(l)


# In[27]:


s="abcd"
l=s.split("d")
print(l)
for i in l:
    print(i)


# ### translate() with maketrans() function
# 

# In[29]:


import string
print(string.punctuation)
print(len(string.punctuation))


# ###    maketrans():make translation table
#                 mapping of character to their replacement or to none for deletion
# #### Syntax---> maketrans(from_chars,to_chars,delete_chars)                
#         

# ### translate()
#        - Applies to translation table created by maketrans()
#        - returns new string with characters replaced or deleted according to table.

# In[36]:


import string
s="Py$@tg!!on"
l=s.maketrans("","",string.punctuation)
x=s.translate(l)
y=s.maketrans("","","@$")
z=s.maketrans("n","m","@$")
print(x)
print(y)
print(z)
n=s.translate(z)
print(n)


# In[38]:


t="Hello Sam!!"
x="mSa"
y="eJo"
table=t.maketrans(x,y)
print(t.translate(table))


# ### Write a program to replace each special symbol with # for following string

# In[50]:


import string
s="/*John is @developer & musician!!"
for i in string.punctuation:
    s=s.replace(i,"#")
print(s)


# ### Write a program to remove ith character from the string

# In[4]:


s="Hello World"
i=int(input("Enter index:"))
l=s.replace(s[i],"",1)
print(l)


# In[6]:


s="Hello World"
i=int(input("Enter index:"))
x=s[:i]+s[i+1:]
print(x)


# ### Write a program to find the count of all occurences of a substring in a given string by ignoring the case
# 

# In[8]:


s="Welcome to USA. usa is awesome.Usa is good.Usain bolt is American."
l=s.lower()
print(l.count("usa"))


# ### Write a program to display all positions of substring in a given string

# In[12]:


s="abcdabcacdab"
l=s.count("a")
sub="a"
pos=0
for i in s:
    if(i==sub):
        print(sub,"found on",pos,"position.")
    pos+=1
print("count:",l)


# ### Write a program to merge characters of two strings into a single string by taking characters alternatively

# In[23]:


x="abc"
y="123"
l=""
for i in range(len(x)):
    l=l+x[i]+y[i]
print(l)


# In[18]:


s="abcabcdefxyzabcxyzab"
sub="abc"
pos=-1
flag=False
n=len(s)
while True:
    pos=s.find(sub,pos+1,n)
    if(pos==-1):
        break
    print("Found at position:",pos)
    flag=True
if flag==False:
    print("Not found.")


# In[30]:


s="a4b3c2"
sub=""
a=0
for i in s:
    if(i.isalpha()):
        a=i
    if(i.isdigit()):
        sub=sub+(a*int(i))
print(sub)


# ### Write a program to check the validity of a password primary conditions for password is given as below
#     minimum 8 characters
#     alphabets should be between [a-z]
#     Atleast one uppercase between[A-Z]
#     atleast one digit between[0-9]
#     atleast one character from[_,@,$]

# In[12]:


password=input("Enter password:")
upcount=0
digicount=0
sym="_@$"
symcount=0
othercount=0
if len(password)>=8:
    for i in password:
        if(i.isalpha()):
            if(i.isupper()):
                upcount+=1
        elif(i.isdigit()):
            digicount+=1
        elif(sym.find(i)>=0):
            symcount+=1
        else:
            othercount+=1
    if(upcount>=1 and digicount>=1 and symcount>=1 and othercount==0):# can use length of password too if sum of all counts=len of password
        print("Valid password")
    else:
        print("Invalid password")
else:
    print("Invalid length")


# ### WAP to shift the decimal digits n places to the left wrapping the extra digits around if shift is greater than the no of digits of n then reverse the string

# In[23]:


n=input("Enter number:")
shift=int(input("Enter shift:"))
p=len(n)
if(p==shift):
    str=n[::-1]
    print(str)
else:
    print(n[shift:]+n[:shift])    


# ## Tuple

# - Tuple is same as list except it is immutable once we create tuple object we cant perform any changes in that object
# - Tuple is read only version of list
# - if our data is fixed and never changes hten we should go for tuple
# - insertion order is preserved
# - duplicates are allowed
# - we can differentiate objects by using index.Hence index play important role in tuple
# - heterogeneous objects are allowed
# - Tuple supports both +ve and -ve indexing
# - we can represent tuple elements within () with comma separator
# - () are optional but recommended to use

# ### Creation of tuple

# In[24]:


t=()
print(type(t))
print(t)


# In[27]:


t=(10)
print(t)
print(type(t))


# In[28]:


t=(10,)
print(t)
print(type(t))


# In[29]:


t=10,20,30
print(t)
print(type(t))


# In[31]:


t=tuple(range(10,20,2))
print(t)


# ### Accessing elements of tuple
# - By using index
# - By using slicing operator

# In[33]:


t=(10,20,30,40,50,60)
print(t[2])
print(t[4])
print(t[-2])
#print(t[100])
print(t[2:5])
print(t[:2])
print(t[4:])
print(t[2:100])
print(t[2:])
print(t[::2])


# ### Mathematical operators of tuple

# - 1.Concatenation operator(+)

# In[34]:


t1=(10,20,30)
t2=(30,40,50)
t=t1+t2
print(t)


# - 2.Repitation operator(*)

# In[35]:


t=(10,20,30)
t1=t*3
print(t1)


# ### Important functions
# - 1.len()

# In[1]:


t=(10,20,30,40)
print(len(t))


# - 2.count()

# In[2]:


t=(1,2,2,3,3,3,1,1,2,4,5)
print(t.count(1))
print(t.count(3))
print(t.count(6))


# - 3.index() - returns the index of first occurence of given element,if specified element is not available then we will get ValueError

# In[3]:


t=(10,20,10,10,20)
print(t.index(10))
print(t.index(30))


# In[6]:


s="Hello World"
print(s.index("l"))


# In[10]:


t=(10,20,10,10,20)
print(t.index(10,1,5))


# - 4.sorted()

# In[11]:


t=(10,30,40,20,50)
t1=sorted(t)
print(t1)


# In[13]:


s="LJIET"
s1=sorted(s)
print(s1)
t=""
for i in s1:
    t=t+i
print(t) 


# In[14]:


t=(10,30,20,40,10)
t1=sorted(t,reverse=True)
print(t1)


# - 5.min() and max() function

# In[15]:


t=(10,50,40,20,30)
print(min(t))
print(max(t))


# ### Tuple packing and unpacking

# In[16]:


a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)


# In[17]:


t=(10,20,30,40)
a,b,c,d=t
print(a,b,c,d)


# In[18]:


t=(10,20,30,40)
a,b,c=t
print(a,b,c)


# ### Loop through tuple

# In[20]:


t=("apple","banana","cherry")
for i in t:
    print(i)


# In[22]:


t=("apple","banana","cherry")
for i in range(len(t)):
    print(t[i])


# In[27]:


t=("apple","banana","cherry")
n=len(t)
i=0
while(i<n):
    print(t[i])
    i+=1


# ### reversed()
# - computes the reverse of the given sequence object and returns it in the form of list

# In[28]:


s="python"
print(list(reversed(s)))


# In[29]:


t=(20,30,10,40,50)
print(list(reversed(t)))


# In[30]:


r=range(5,9)
print(list(reversed(r)))


# In[31]:


l=[1,2,3,4,5]
print(list(reversed(l)))


# ### enumerate()
# - if you pass a string to enumerate(),the output will show you the index and value for each character of the string
# ####          Syntax 
# -             enumerate(iterable,start=0)

# In[32]:


s1="LJIET"
obj1=enumerate(s1)
print(obj1)
print(list(obj1))


# In[37]:


s1="LJIET"
for i,j in enumerate(s1):
    print(i,"-",j)


# In[38]:


s1="LJIET"
for i,j in enumerate(s1,5):
    print(i,"-",j)


# In[40]:


l=["eat","sleep","repeat"]
for i,j in enumerate(l):
    print(i,j)


# In[62]:


t=(1,2,4,6,7,8,13,14,16)
evencount=0
oddcount=0
even_sum=0
odd_sum=0
even_max=0
odd_max=0
even_min=0
odd_min=0
for i in t:
    if(i%2==0):
        evencount+=1
        even_sum+=i
        if(even_max<i):
            even_max=i
        else:
            even_max=even_max
    else:
        oddcount+=1
        odd_sum+=i
        if(odd_max<i):
            odd_max=i
        else:
            odd_max=odd_max
even_min=even_max
odd_min=odd_max
for i in t:
    if(i%2==0):
        if(even_min>i):
            even_min=i
        else:
            even_min=even_min
    else:
        if(odd_min>i):
            odd_min=i
        else:
            odd_min=odd_min
print(evencount)
print(even_sum)
print(oddcount)
print(odd_sum)
print(even_max)
print(odd_max)
print(even_min)
print(odd_min)


# In[ ]:




