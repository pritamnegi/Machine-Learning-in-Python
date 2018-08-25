
# coding: utf-8

# # Numpy
# 
# 1. Numpy is for faster numerical calculations.

# ** Importing numpy package

# In[1]:


import numpy as np


# ** Creating a Numpy Array

# In[5]:


a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(a[-1])


# ** Methods in Numpy

# In[9]:


a.size


# In[10]:


a.dtype


# In[11]:


a.shape


# In[12]:


a.itemsize


# ** Creating a floating point array

# In[13]:


b = np.array([1, 2, 3], dtype =float)
print(b)


# In[15]:


c = np.array([[0, 1, 2, 3], [10, 11 , 12, 13]])
print(c)


# In[16]:


c.shape


# ** Creating a 3-D Array

# In[17]:


d = np.array([[[1, 2, 3],
               [4, 5, 6]],
              
              [[7, 8, 9],
               [10, 11, 12]]])

print(d)


# In[18]:


d.shape


# In[20]:


e = np.arange(10)
print(e)


# In[22]:


f = np.arange(1, 9, 2)
print(f)


# In[24]:


g = np.linspace(0, 1, 6) # linspace = Linearly spaced points
print(g)


# ** Creation of Common Arrays

# In[27]:


h = np.ones((3, 3))
print(h)


# In[29]:


i = np.zeros((2, 2))
print(i)


# In[32]:


j = np.identity(3)
print(j)


# In[33]:


k = np.diag([1, 2, 3, 4])
print(k)


# In[35]:


l = np.random.random((3, 2))
print(l)


# In[36]:


m = np.ones_like(l, float)
print(m)


# In[38]:


n = np.zeros_like(l, float)
print(n)


# ** Transpose of a numpy array

# In[39]:


o = l.T
print(o)


# ** Accessing Array Elements

# In[40]:


print(a[-3])


# In[41]:


print(c[1,3])


# In[42]:


c[1, 3] = 0;
print(c)


# ** Arrays: Basic Operations

# In[43]:


p = np.array([1, 2, 3, 4])
q = np.array([4, 5 , 6, 7])


# In[44]:


print(p+q)


# In[45]:


print(p-q)


# In[46]:


print(p*q)


# In[47]:


print(p/q)


# In[48]:


r= np.arange(10)


# ** Indexing and Slicing Arrays

# In[49]:


r[2:9:3]


# In[50]:


print(r[:4])


# In[52]:


print(r[1:3])


# In[53]:


print(r[::2])


# In[54]:


print(r[3:])


# In[55]:


print(h[0, 1:3])


# In[56]:


print(h[1:, 1:])


# In[57]:


print(h[:, 2])


# ** Reshaping Arrays

# In[58]:


s = np.arange(12)
print(s)


# In[60]:


t = s.reshape(3, 4) # Dimension of reshaping array should be factor of size of original array
print(t)


# ** Array Math

# In[62]:


o = np.floor(o)
print(o)


# In[64]:


o = np.ceil(l)
print(o)


# In[65]:


u = np.sin(p)
print(u)


# In[66]:


v = np.cos(p)
print(v)


# In[69]:


w = np.around(v, 2)
print(w)


# In[70]:


x = np.sqrt(p)
print(x)


# ** Basic Visualization

# In[75]:


import matplotlib.pyplot as plt
x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)      # Line plot
plt.plot(x, y, 'o') # Dot plot
plt.show()


# In[76]:


import matplotlib.pyplot as plt
x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)      # Line plot
plt.plot(x, y, 'o') # Dot plot
plt.title('Example plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()


# In[78]:


a1 = np.linspace(0, 2*np.pi, 50)
plt.plot(np.sin(a1))
plt.show()


# In[80]:


a2 = np.linspace(0, 2*np.pi, 50)
plt.plot(np.cos(a2))
plt.show()


# In[83]:


a3 = np.linspace(0, 2*np.pi, 50)
plt.plot(np.sin(a3), label = 'sin')
plt.plot(np.cos(a3), label = 'cos')
plt.legend()
plt.show()


# In[93]:


a4 = np.linspace(0, 2*np.pi, 50)
plt.plot(a4,np.sin(a4), 'b-o', 
         a4 ,np.cos(a4), 'r-^')
plt.show()


# In[114]:


a5 = np.random.random(200)
a6 = np.random.random(200)
plt.scatter(a5, a6, color = ['r', 'b'])
plt.show()


# In[108]:


plt.hist(np.random.random(200))
plt.show()


# In[109]:


plt.hist(np.random.random(200), 15)
plt.show()


# ** Basic Reductions

# In[117]:


sum = a.sum()
print(sum)


# In[120]:


min = a.min()
print(min)


# In[118]:


mean = a.mean()
print(mean)


# In[119]:


std = a.std()
print(std)


# In[123]:


median = np.median(a) # 3.5 is the position of the median element
print(median)


# In[124]:


loc_min = a.argmin()
loc_max = a.argmax()
loc_min, loc_max


# In[128]:


c


# In[127]:


c.sum(axis = 0)


# In[129]:


c.sum(axis = 1)


# In[130]:


a7 = np.zeros((10, 10))
np.any(a7 != 0)


# In[132]:


np.all(a7 == 0)


# In[135]:


a8 = np.array([1, 2, 3, 2])
a9 = np.array([2, 2, 3, 2])
a10 = np.array([6, 4, 4, 5])
((a8<=a9) & (a9<=a10)).all()

