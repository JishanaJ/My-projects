#!/usr/bin/env python
# coding: utf-8

# #### Import necessary libraries

# In[2]:


import pandas as pd


# #### Read the data

# In[3]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'

users = pd.read_csv(url,index_col=0,sep='|')


# #### First 10 entries

# In[9]:


users.head(10)


# #### Last 10 entries

# In[10]:


users.tail(10)


# #### What is the number of observations in the dataset?

# In[13]:


users.shape


# In[14]:


users.shape[0]


# Total observations are 943

# #### What is the number of columns in the dataset?

# In[15]:


users.shape[1]


# Total number of columns are 4

# #### Print the name of all the columns

# In[5]:


print('Columns in dataframe are:\n')
for i in users.columns:
    print('\t',i)


# #### How is the dataset indexed?

# In[24]:


users.index


# #### What is the data type of each column?

# In[27]:


users.info()


# #### Print only the occupation column

# In[30]:


users['occupation']


# #### How many different occupations are in this dataset?

# In[35]:


users['occupation'].value_counts().shape[0]


# #### What is the most frequent occupation?

# In[43]:


users['occupation'].value_counts().index[0]


# #### DataFrame Info

# In[44]:


users.info()


# #### Describe all the columns

# In[46]:


users.describe(include='all')


# #### Summarize only the occupation column

# In[47]:


users['occupation'].value_counts()


# #### What is the mean age of users?

# In[49]:


users['age'].mean()


# #### What is the age with least occurrence?

# In[82]:


users_age = pd.DataFrame(users['age'].value_counts())


# In[76]:


users_age.loc[users_age['age']==1]

