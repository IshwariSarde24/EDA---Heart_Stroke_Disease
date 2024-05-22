#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df=pd.read_csv('C:/Users/Ishwari/Downloads/healthcare-dataset-stroke-data.csv')


# In[5]:


df


# In[4]:


df.info()


# In[5]:


df.shape


# In[6]:


df.describe()


# In[8]:


df[['age','hypertension','heart_disease','avg_glucose_level','bmi','stroke',]].corr()


# In[11]:


sns.heatmap(df[['age','hypertension','heart_disease','avg_glucose_level','bmi','stroke']].corr(),annot=True)


# # bar graph

# In[13]:


sns.countplot(data=df,x='work_type',hue='smoking_status')

Interpretation: No.of formerly smoked people are more in the private sector.
# # Histogram

# In[8]:


sns.histplot(data=df,x='age',bins=10,kde=True)

 Interpretation: In the age group between 50-60 have high chance of heart stroke.
# In[11]:


sns.histplot(data=df,x='avg_glucose_level',bins=5,hue='work_type')

Interpretation: in the private sector the avg_glucose_level is high 
# In[15]:


sns.histplot(data=df,x='avg_glucose_level',bins=5,hue='gender')

Interpretation: avg_glucose_level is high in male than female
# In[16]:


sns.histplot(data=df,x='bmi',kde=True)

Interpretation: there is high BMI between age group 20-40
# # box plot

# In[17]:


sns.boxplot(data=df,x='smoking_status',y='age')

Interpretation:From the above graph the distribution of formerly smoked people are negatively skewed and distibution of unknown
is positively skewed where the distribution of never smoked and smokes people are approximately normal.sns.boxplot(data=df,x='Residence_type',y='bmi')Interpretation:From the above graph we have seen that the distribution of Residence_type is approximately normally distributed.
# # scatter plot

# In[25]:


sns.scatterplot(data=df,x='age',y='avg_glucose_level',hue='Residence_type')

Interpretation:There is no correlation between age and avg_glucose_level.
# # Lmplot

# In[26]:


sns.lmplot(data=df,x='bmi',y='age',hue='hypertension')


# # Jointplot

# In[13]:


sns.jointplot(data=df,x='bmi',y='age',kind='hex')
plt.colorbar()


# # Violin plot

# In[30]:


sns.violinplot(data=df,x='smoking_status',y='age',palette='colorblind')


# In[32]:


sns.pairplot(data=df,vars=['age','hypertension','heart_disease','avg_glucose_level','bmi','stroke'],hue='ever_married')


# In[15]:


sns.swarmplot(data=df, x='ever_married', y='age')


# In[17]:


sns.catplot(data=df, x="Residence_type", y="avg_glucose_level", hue="ever_married", col="work_type", kind='bar', palette='pastel')


# In[19]:


sns.catplot(data=df, x="Residence_type", y="bmi", hue="smoking_status", col="gender", kind='box', palette='bright')


# In[1]:


import plotly.express as px


# In[6]:


fig_3d = px.scatter_3d(df, x='hypertension', y='age', z='bmi', color='heart_disease')
fig_3d.show()


# In[ ]:




