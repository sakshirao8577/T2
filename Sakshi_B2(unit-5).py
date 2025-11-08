#!/usr/bin/env python
# coding: utf-8

# # Mutable Data structures

# ### 1.List

# #### Creation of list

# In[1]:


l=[]
print(l)
print(type(l))


# In[3]:


l=[10]
print(l)
print(type(l))


# In[4]:


l=[1,2,3,4]
print(l)
print(type(l))


# #### Creation list with dynamic input

# In[5]:


l=eval(input("Enter list:"))
print(l)
print(type(l))


# In[9]:


l=eval(input("Enter list:"))
print(l)
print(type(l))


# In[10]:


l=eval(input("Enter list:"))
print(l)
print(type(l))


# In[11]:


l=eval(input("Enter list:"))
print(l)
print(type(l))


# #### using list()

# In[12]:


l=list(range(10,20,2))
print(l)


# In[13]:


l="Arman"
x=list(l)
print(x)


# #### using split() function

# In[14]:


s="Learning Python is very easy"
l=s.split()
print(l)


# ### List Mutability

# In[15]:


l=[1,2,3,4,5]
l[2]=10
print(l)


# In[16]:


l=(1,2,3,4,5)
l[2]=10
print(l)


# ### Accessing the elements of list
# - 1.By using index

# In[17]:


l=[10,20,30,40,50,60]
print(l[0])
print(l[3])
print(l[-2])
print(l[10])


# - 2.By using slicing operator

# In[24]:


l=[1,2,3,4,5,6,7,8,9,10]
print(l[2:7:2])
print(l[4::2])
print(l[3:7])
print(l[8:2:-2])
print(l[4:100])
print(l[-5:-2])
print(l[-5:-2:-1])


# ### Mathematical operators
# - 1.concatenation(+)

# In[25]:


a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)


# In[26]:


d=a+[4]
print(d)


# - 2.repetition(*)

# In[27]:


l=[1,2,3]
l1=l*3
print(l1)


# ### Membership operator

# In[28]:


l=[10,20,30,40,50]
print(10 in l)
print(10 not in l)
print(50 in l)
print(60 not in l)


# ### Comparison operator for list

# In[1]:


x=["Dog","Cat","Rat"]
y=["Dog","Cat","Rat"]
z=["DOG","CAT","RAT"]
print(x==y)
print(x==z)
print(x!=z)


# In[2]:


x=[50,20,30]
y=[40,50,60,100,200]
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)


# In[3]:


x=["Dog","Cat","Rat"]
y=["Rat","Cat","Dog"]
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)


# ### Aliasing and cloning of list

# In[4]:


l=[1,2,3,4,5]
x=l
print(x)
x[2]=10
print(x)
print(l)
print(id(x))
print(id(l))


# In[5]:


l=[1,2,3,4,5]
x=l.copy()
print(x)
x[2]=10
print(x)
print(l)
print(id(x))
print(id(l))


# In[6]:


l=[1,2,3,4,5]
x=l[:]
print(x)
x[2]=10
print(x)
print(l)
print(id(x))
print(id(l))


# ## Nested list

# In[12]:


n=[10,20,[30,40]]
print(n)
print(n[2])
print(n[2][1])
n[2].index(40)


# In[11]:


n=[[10,20,30],[40,50,60],[70,80,90]]
print(n[1][2])


# ## Important functions of list
# - 1.len()
# - 2.count()
# 

# In[13]:


l=[1,2,2,3,3,4,4,5,6]
print(len(l))
print(l.count(2))
print(l.count(7))


# - 3.index()

# In[15]:


n=[1,2,2,2,3,3]
print(n.index(1))
print(n.index(2))
#print(n.index(4))
print(n.index(2,2,5))


# - 4.append()
#         ---> used to add item at the end of the list

# In[16]:


l=["A","B","C"]
l.append("D")
l.append("E")
l.append([1,2,3])
print(l)


# - 5.insert()
#        ---> to insert item at the specific index position
#        Syntax---> insert(index,value)

# In[21]:


n=[1,2,3,4,5]
n.insert(2,10)
print(n)
n.insert(10,50)
print(n)
n.insert(-10,0)
print(n)
n.insert(-1,40)
print(n)


# - 6.extend()
#      ---> To add all items of one list to another list
#           l1.extend(l2)---> all items present in l2 will be added to l1

# In[22]:


l1=["Apple","Banana"]
l2=["Orange","Mango"]
l1.extend(l2)
print(l1)
print(l2)


# In[23]:


l1=["Apple","Banana"]
l2=["Orange","Mango"]
l2.extend(l1)
print(l1)
print(l2)


# In[24]:


l1=["amit","sumit"]
l1.extend("kumar")
print(l1)


# - 7.remove()
#          ---> remove specified item from the list
#          ---> if item is multiple times then only first occurence will be removed

# In[27]:


l=[1,2,1,3,2,3]
l.remove(1)
print(l)
l.remove(1)
print(l)
l.remove(1)
print(l)


# - 8.pop()
#        ---> it removes and returns the last element of the list
#        ---> This is the only function which manipulates list and returns some element

# In[29]:


n=[10,20,30,40]
print(n.pop())
print(n.pop())
print(n.pop())
print(n.pop())
print(n.pop())


# In[32]:


n=[1,2,3,4,5]
print(n.pop(1))


# - 9.clear()
#        ---> to remove all the elements of list

# In[33]:


n=[1,2,3,4]
n.clear()
print(n)


# - 10.reverse()

# In[34]:


n=[1,2,3,4,5]
n.reverse()
print(n)


# ### sort()
# 

# In[36]:


n=[2,5,15,1,0]
n.sort()
print(n)
n.sort(reverse=True)
print(n)


# In[37]:


l=["D","B","C","A"]
l.sort()
print(l)


# In[38]:


n=[10,20,"A","B"]
n.sort()
print(n)


# In[41]:


words=["Python","is","very","easy"]
words.sort(key=len)
print(words)


# In[42]:


words=["Python","is","very","easy"]
words.sort(key=len,reverse=True)
print(words)


# In[43]:


def myfunc(e):
    return len(e)
cars=['Ford','Mitsubishi','BMW']
cars.sort(key=myfunc)
print(cars)


# ## Nested list as matrix

# In[55]:


n=[[10,20,30],[40,50,60],[70,80,90]]
for i in range(len(n)):
    print(n[i])
for l in range(len(n)):
    for m in range(len(n)):
        print(n[l][m]," ",end="")
    print()


# ### List comprehension

# - Syntax ---> list=[expression for item in list if condition]

# In[56]:


s=[x*x for x in range(1,11)]
print(s)


# In[57]:


a=[1,2,3,4,5,6,7,8,9,10]
x=[num for num in a if num%2==0]
print(x)


# In[58]:


y=[x+2 for x in range(10)]
print(y)


# In[61]:


y=(x+2 for x in range(10))
print(y)
print(tuple(y))


# ## WAP to perform a circular shift on a list to the right direction

# In[76]:


l=[1,2,3,4,5,6,7]
shift=32
x=shift%len(l)
n=[]
for i in l:
    n=l[-x:]+l[:-x]
print(n)


# ## WAP to print elements with frequency greater than a given value k

# In[84]:


n=[1,1,1,1,2,2,2,3,4,4,5,5,5,6,6]
k=int(input("Enter k:"))
l=[]
for i in n:
    if(n.count(i)>k) and i not in l:
        l.append(i)
print(l)


# ## WAP for given a list l of size n u need to count the no of special elements in the given list an element is special if removal of that element makes the list balanced the list will be balanced if sum of even index elements is equal to the sum of odd index elements also print the updated list after removal of special elements atlast give the count of special elements

# In[1]:


l=eval(input("Enter list:"))
print("Original list:",l)
print()
count=0
for i in range(len(l)):
    c=l.copy()
    c.pop(i)
    sum1=sum(c[::2])
    sum2=sum(c[1::2])
    if(sum1==sum2):
        print("Original list:",l)
        print("index to be removed:",i)
        print("list after removal of index",i,":",c)
        count+=1;
print("Total special elements:",count)


# In[ ]:




