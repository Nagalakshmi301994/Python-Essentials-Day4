#!/usr/bin/env python
# coding: utf-8

# # Print the first ArmStrong number in the range of 1042000 to 702648265 and exit the loop as soon as you encounter the first armstrong number.use while loop

# In[1]:


lower = 1042000


# In[2]:


upper= 702648265


# In[3]:


for num in range(lower, upper + 1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
      print("The first armstrong number is.....", num)
      break
      print("Loop Ended",num)


# In[ ]:




