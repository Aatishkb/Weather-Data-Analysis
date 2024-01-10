#!/usr/bin/env python
# coding: utf-8

# # Weather Data Analysis

# - IN THIS POJECT WE WILL USE FOLLOWING COMMANDS/OPERATIONS TO ANALYZE THE WEATHER'S DATA :-

# ### Pandas

# - Pandas :- Pandas is a library used to work with Data-Set.
# - Pandas has Functions for Analyzing,Cleaning,Exploring & Manipulating data.

# In[65]:


import pandas as pd


# ### NumPy

# - NumPy :- NumPy library is used to perform Mathematical Operation on Arrays.

# In[66]:


import numpy as np


# ### Importing the DataSet/DataFrame

# - Syntax to Load or import the DataSet(DataFrame)
# - d = pd.read_csv(r'csv_FilePath Or Location\csv_fileName')
# - d is a variable where we have stored Whole Data Set/frame

# In[67]:


d = pd.read_csv(r'A:\MTECH(Data Science)\DataSet\archive\weather.csv')


# ### NOW TO ANALYZE THE WEATHER'S DATA I AM USING FOLLOWING COMMANDS :-

# # d

# - This command will show whole Data-Set
# - print(d) are eqivalent command.

# In[68]:


d


# # d.head()

# - This command will show the by default first 5 rows from the loaded DataSet.

# In[69]:


d.head()


# # d.tail()

# - This command will show the by default last 5 rows from the loaded DataSet.

# In[70]:


d.tail()


# # d.head(8)

# - This command will show the first N rows from the loaded DataSet.
# - d.head(7) = This command will show the first 7 rows from the loaded DataSet.
# - d.head(11) = This command will show the first 11 rows from the loaded DataSet.

# In[71]:


d.head(8)


# # d.shape

# - This command will show the Total No. of rows and Total No. of Columns of the loaded DataSet.

# In[72]:


d.shape


# # d.index

# - This command will show the Range of the loaded DataSet.

# In[73]:


d.index


# # d.columns

# - This command will show the complete Attributes(columns) of the loaded DataSet.

# In[74]:


d.columns


# # d.dtypes

# - This command will show the Data Type of each Column of the loaded DataSet.

# In[75]:


d.dtypes


# # d['Column_Name'].unique()

# - This command will show all the unique values of a particular column and it can be apply in only single column.

# In[76]:


d['MinTemp'].unique()


# # d.nunique()

# - This command will show total no. of in unique values in each column and it can be apply in single column as well as on whole DataFrame.
# - d.nunique() Apply in whole DataFrame

# In[77]:


d.nunique()


# # d.nunique() Apply in Single DataFrame

# - It will show Total No. of Unique values that are present in particular column(Attribute).

# In[78]:


d['MinTemp'].nunique()


# # d.value_counts

# - This command will show all the unique values with their count(Times or frequency).
# - It can be apply in only single column.

# In[79]:


d['MinTemp'].value_counts()


# In[80]:


d['RainTomorrow'].value_counts() # Show frequency


# # d.info()

# - This command will provide us basic information about the DataFrame.

# In[81]:


d.info()


# # d.count

# - This command will show total no. of Non-NULL values in each column and it can be apply in single column as well as on whole DataFrame.
# - Apply in whole DataFrame

# In[82]:


d.count()


# # d.notnull().sum()

# - This command is used to check all rows amd column are filled or not in our loaded dataframe.

# In[83]:


d.notnull().sum()


# # d.isnull().sum()

# - This command is used to check NULL values present or not in our dataframe.
# - isnull command is used to check for null values.

# In[84]:


pd.isnull(d).sum()


# ### In this Data_Frame has NULL values so first of all we have to clean it and then we will apply any kind of operations.

# - In above cell we have got null values in following columns :-
 Sunshine          3
 WindGustDir       3
 WindGustSpeed     2
 WindDir9am       31
 WindDir3pm        1
 WindSpeed9am      7
# - So we have to remove null values by using drop command.

# In[85]:


# drop null values
d.dropna(inplace=True)


# # After removing null values.

# In[86]:


pd.isnull(d).sum()


# # Operation - 1

# Rename Column

# In[87]:


# Syntax
# d.rename('columns={'Old_Name_Of_Column':'New_Name_Of_Column'})
# Rename Temporary
d.rename(columns={'WindGustDir':'WindGustDirection'})


# In[88]:


# Above Command Rename Temporary
d.head(2)


# In[89]:


# To Rename Permanently
# Syntax
# d.rename('columns={Old_Name_Of_Column':'New_Name_Of_Column'},inplace=True)
d.rename(columns={'WindGustDir':'WindGustDirection'},inplace=True) # Rename Permanently


# In[90]:


# see again it is changed or not?
d.head(2)


# # Operation - 2

# Calculation of Mean

# In[91]:


# Syntax
# d.Column_name.mean()
d.MinTemp.mean()


# In[92]:


d.MaxTemp.mean()


# In[93]:


d.mean()


# In[94]:


d.groupby('MinTemp').mean()


# # Operation - 3

# Calculation of Standard Deviation

# In[95]:


# Syntax
# d.Column_name.std()
d.MinTemp.std()


# In[96]:


d.MaxTemp.std()


# In[97]:


d.std()


# # Operation - 4

# Calculation of Variance

# In[98]:


# Syntax
# d.Column_name.var()
d.MinTemp.var()


# In[99]:


d.MaxTemp.var()


# In[100]:


d.var()


# # Operation - 5

# Calculation of Median

# In[101]:


# Syntax
# d.Column_name.median()
d.MinTemp.median()


# In[102]:


d.MaxTemp.median()


# In[103]:


d.median()


# # Operation - 6

# Calculation of Mode

# In[104]:


# Syntax
# d.Column_name.mode()
d.MinTemp.mode()


# In[105]:


d.mode()


# # Operation - 7

# Calculation of Kurtosis

# In[106]:


# Syntax
# d.Column_name.kurt()
# for single attribute
d.MinTemp.kurt()


# In[107]:


# For complete attributers
d.kurt()


# # Operation - 8

# Calculation of Skewness

# In[108]:


# Syntax
# d.Column_name.skew()
d.MinTemp.skew()


# In[109]:


# For complete attributers
d.skew()


# # Operation - 9

# Calculation of Correlation

# In[110]:


# Syntax
# d.corr()
d.corr()


# # Operation - 10

# FILTER

# We are filtring the records where the attribute RainTomorrow has only Yes.

# In[111]:


# Syntax
# d[d['Column_name']=='value']

d[d['RainTomorrow']=='Yes']


# # Operation - 11

# FILTER

# We are filtring the records where the attribute RainTomorrow has only No.

# In[112]:


d[d['RainTomorrow']=='No']


# # Operation - 12

# Calculation of Minimum Value

# In[113]:


# This command will give us minimum value from each column.
d.min()


# In[114]:


# For Particular column
d['RISK_MM'].min()


# In[115]:


d.groupby('MinTemp').min()


# # d.sum()

# In[116]:


d.sum()


# # d.describe()

# - This command will show us count, mean, std, min, max of whole dataframe.

# In[117]:


d.describe()


# # Operation - 13

# Calculation of Maximum Value

# In[118]:


# This command will give us maximum value from each column.
d.max()


# In[119]:


# For Particular column
d['RISK_MM'].max()


# In[120]:


d.groupby('MinTemp').max()


# # Operation - 14

# str.contains

# # Retrieved data only if RainToday is Yes

# In[121]:


d[(d['RainToday'].str.contains('Yes'))]


# In[122]:


d[d['RainToday']=='Yes']


# # Operation - 15

# In[123]:


d[d['RainToday']=='No']


# # If 'RainToday =='No' AND 'Rainfall'==0.0 AND 'RISK_MM'==0.0 Then It May be No Rain Tomorrow

# In[124]:


d[(d['RainToday']=='No')&(d['Rainfall']==0.0)&(d['RISK_MM']==0.0)]


# In[125]:


d[(d['RainToday']=='Yes')&(d['Rainfall']!=0.0)]


# ### In this Weather Data Analysis we apply Following Algoriths for Weather prediction :-
#  - Decision Tree
#  - NBC
#  - SVM
#  - ARIMA
# 

# ### I have completed this projet with the help of online resourses and plateform.

# - Name - Aatish Kumar Baitha
# - M.Tech(Data Science 2nd Year Student)

# ### My Linkedin Profile -
# - www.linkedin.com/in/aatish-kumar-baitha-ba9523191

# ### My Blog -
# - https://computersciencedatascience.blogspot.com/

# ### Thank you!
