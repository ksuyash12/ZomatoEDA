#!/usr/bin/env python
# coding: utf-8

# In[48]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv("zomato.csv",encoding ="latin-1")


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[7]:


[features for features in df.columns if df[features].isnull().sum()>1]


# In[8]:


df_country=pd.read_excel('Country-Code.xlsx')
df_country.head(14)


# In[9]:


df.columns


# In[10]:


final_df=pd.merge(df,df_country,on='Country Code',how='left')
final_df.head(2)


# In[11]:


country_name=final_df.Country.value_counts().index 
country_name


# In[12]:


country_value=final_df.Country.value_counts().values
country_value 


# In[13]:


plt.pie(country_value[:3],labels=country_name[:3])


# In[14]:


ratings=final_df.groupby(['Aggregate rating','Rating color', 'Rating text']).size().reset_index().rename(columns={0: 'Rating Counts'})
ratings


# In[15]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6) 
sns.barplot(x="Aggregate rating", y="Rating Counts",data=ratings)


# In[16]:


sns.barplot(x="Aggregate rating", y="Rating Counts", hue="Rating color",data=ratings)


# In[17]:


sns.countplot(x='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])


# In[18]:


final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(4)


# In[19]:


final_df[final_df['Aggregate rating']==0].groupby('Country').size().reset_index()


# observation 
# maximum zero ratings are from india

# In[24]:


final_df.groupby(['Country','Currency']).size().reset_index().rename(columns={0: 'count'})


# In[25]:


final_df.columns


# In[26]:


final_df.head()


# In[30]:


final_df[final_df['Has Online delivery']=='Yes'].groupby('Country').size()


# In[43]:


final_df.City.value_counts().index


# In[45]:


City_value=final_df.City.value_counts().values
City_label=final_df.City.value_counts().index


# In[54]:



plt.pie(City_value[:5],labels=City_label[:5],autopct='%1.2f%%')
plt.show


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




