#!/usr/bin/env python
# coding: utf-8

# # Question 1: Use numpy to generate array of 25 random numbers sampled from a standard normal distribution

# In[9]:


import numpy as np
rand_num = np.random.randn(5,5)
print("25 random numbers from a standard normal distribution:")
print(rand_num)


# # Question 2: Create a random vector of size 30 and find the mean value.
# 

# In[18]:


np.random.seed(7)
Z = np.random.random(30)
print("The vector is", Z)
print("size of the array is",Z.size)
m = Z.mean()
print("Mean of values is", m)


# # Question 3: Insert 1 to 100 numbers in a numpy array and reshape it to 10*10 matrix.
# 

# In[17]:


a= np.arange(1,101)
print("The array is",a)
a.reshape((10,10))


# # Question 4: Create a 10x10 array with random values and find the minimum and maximum values.

# In[21]:


np.random.seed(7)
x= np.random.randint(0,100,(10,10))
print("The array is", x)
print("Minimum value in the array is", x.min())
print("Maximum value in the array is", x.max())


# # Question 5: Find Dot product of two arrays
# 
# f = np.array([1,2])
# 
# g = np.array([4,5])

# In[5]:


import numpy as np

f = np.array([1,2])
print("First Array is:","\n",f)

g = np.array([4,5])
print("Second Array is:","\n", g)

print("The dot product of f and g is",np.dot(f,g))


# # Question 6: Concatenate following arrays along axis=0
# Ans: x=np.array([[1,2],[3,4]])
# 
# y=np.array([[5,6]])

# In[7]:


x=np.array([[1,2],[3,4]])

y=np.array([[5,6]])

print('Array 1 :','\n',x)
print('Array 2 :','\n',y)
print('Concatenate along rows :','\n',np.concatenate((x,y),axis=0))


# # Question 7: How to get the common items between two python numpy arrays?
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# 
# b = np.array([7,2,10,2,7,4,9,4,9,8])

# In[1]:


import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])

b = np.array([7,2,10,2,7,4,9,4,9,8])
print('Array 1 :','\n',a)
print('Array 2 :','\n',b)
print("Common values between two arrays:")
print(np.intersect1d(a,b))


# # Question 8: Sort the numpy array:
# 
# arr = np.array([10,5,8,4,7,2,3,1])

# In[2]:


arr = np.array([10,5,8,4,7,2,3,1])

print('Original Array is :','\n',arr)

print("Sorted array is :","\n", np.sort(arr))


# In[ ]:




