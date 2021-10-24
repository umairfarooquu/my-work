#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# In[2]:


import sys
print("Python version")


# In[3]:


print (sys.version)


# In[4]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[5]:


from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[6]:


aname = input("Input your First Name : ")
bname = input("Input your Last Name : ")
print ("Hello  " + aname + " " + aname)


# In[7]:


aname = input("Input your First Name : ")
bname = input("Input your Last Name : ")
print ("Hello  " + aname + " " + bname)


# In[8]:


a = int(input("enter first number: "))
b = int(input("enter second number: "))
 
sum = a + b
 
print("sum:", sum)


# In[10]:


sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")


# In[11]:


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[12]:


ListName = ["Hello", "umer", 1, 2, 3]
print ("Number of items in the list = ", len(ListName))


# In[13]:


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


# In[14]:


def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))


# In[15]:


test_list= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for element in test_list:
    if(int(element) <5):
        print(str(element)+"\n")


# In[ ]:




