#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[14]:


def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =  np.arange(1,13).reshape((6,2)) 

    return x


# In[15]:


function1()


# In[29]:


def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    
    x = np.arange(10,37,dtype=np.float64).reshape((3,3,3))     #wrtie your code here


    return x


# In[30]:


function2()


# In[51]:


def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    a = a.flatten() 
    x=a[34::35]
    #wrtie your code here
    return x


# In[52]:


function3()


# In[6]:


def function4():
    #Swap columns 1 and 2 in the array arr.

    arr = np.arange(9).reshape(3,3)
   # arr=arr[:,[1,0,2]]

    return arr#wrtie your code here


# In[7]:


function4()


# In[18]:


def function5():
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function

    z = np.zeros((4,5))
   

    return z


# In[13]:


function5()


# In[19]:


def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively

    arr =np.zeros(10)
    arr[5]=10
    arr[8]=20
    return arr


# In[21]:


function6()


# In[22]:


def function7():
    #  Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.arange(4, dtype=np.int64)
    x=np.zeros(4,dtype=np.int64)

    return x#write your code here


# In[23]:


function7()


# In[27]:


def function8():
    # Create a new array of 2x5 uints, filled with 6.

    x =(np.ones((2,5)))*6
    #write your code here

    return x


# In[28]:


function8()


# In[32]:


def function9():
    # Create an array of 2, 4, 6, 8, ..., 100.

    a =np.arange(101)
    a=a[2:101:2]
    # write your code here

    return a


# In[33]:


function9()


# In[35]:


def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.

    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt = arr-brr
    # write your code here 

    return subt


# In[36]:


function10()


# In[43]:


def function11():
    # Replace all odd numbers in arr with -1 without changing arr.

    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ans =np.where(arr % 2 == 1, -1, arr)
    #write your code here 

    return ans


# In[44]:


function11()


# In[47]:


def function12():
    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking concept

    arr = np.array([1,2,3])
    arr2=np.repeat(arr,3)
    arr3=np.tile(arr,3)
    ans =np.hstack((arr2,arr3))
    #write your code here 

    return ans


# In[48]:


function12()


# In[51]:


def function13():
    # Set a condition which gets all items between 5 and 10 from arr.


    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans = arr[(arr > 5) & (arr < 10)]
    #write your code here 

    return ans


# In[52]:


function13()


# In[57]:


def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method


    arr = np.arange(10, 34, 1).reshape(8,3) #write reshape code
    ans =np.split(arr,[2,5,8])
    #write your code here 

    return ans


# In[58]:


function14()


# In[59]:


def function15():
    #Sort following NumPy array by the second column


    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
    ans = np.sort(arr)

    return ans


# In[60]:


function15()


# In[66]:


def function16():
    #Write a NumPy program to join a sequence of arrays along depth.


    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    ans =np.dstack((x,y))
    #write your code here 

    return ans


# In[67]:


function16()


# In[74]:


def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    arr = np.arange(1,10*10+1).reshape((10,10))
    ans=np.where((arr % 3 == 0 )| (arr % 5 == 0),'yes','No')
    return ans


# In[75]:


function17()


# In[79]:


def function18():
    # count values of "students" are exist in "piaic"
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    x = np.count_nonzero(students)
    # Write you code Here
    return x


# In[80]:


function18()

