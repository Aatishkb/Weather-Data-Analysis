# Weather-Data-Analysis

- IN THIS POJECT WE WILL USE FOLLOWING COMMANDS/OPERATIONS TO ANALYZE THE WEATHER'S DATA :-

### Pandas

- Pandas :- Pandas is a library used to work with Data-Set.
- Pandas has Functions for Analyzing,Cleaning,Exploring & Manipulating data.

import pandas as pd

### NumPy

- NumPy :- NumPy library is used to perform Mathematical Operation on Arrays.

import numpy as np

### Importing the DataSet/DataFrame

- Syntax to Load or import the DataSet(DataFrame)
- d = pd.read_csv(r'csv_FilePath Or Location\csv_fileName')
- d is a variable where we have stored Whole Data Set/frame

d = pd.read_csv(r'A:\MTECH(Data Science)\DataSet\archive\weather.csv')

### NOW TO ANALYZE THE WEATHER'S DATA I AM USING FOLLOWING COMMANDS :-

# d

- This command will show whole Data-Set
- print(d) are eqivalent command.

d

# d.head()

- This command will show the by default first 5 rows from the loaded DataSet.

d.head()


# d.tail()

- This command will show the by default last 5 rows from the loaded DataSet.

d.tail()

# d.head(8)

- This command will show the first N rows from the loaded DataSet.
- d.head(7) = This command will show the first 7 rows from the loaded DataSet.
- d.head(11) = This command will show the first 11 rows from the loaded DataSet.

d.head(8)

# d.shape

- This command will show the Total No. of rows and Total No. of Columns of the loaded DataSet.

d.shape

# d.index

- This command will show the Range of the loaded DataSet.

d.index

# d.columns

- This command will show the complete Attributes(columns) of the loaded DataSet.

d.columns

# d.dtypes

- This command will show the Data Type of each Column of the loaded DataSet.

d.dtypes

# d['Column_Name'].unique()

- This command will show all the unique values of a particular column and it can be apply in only single column.

d['MinTemp'].unique()

# d.nunique()

- This command will show total no. of in unique values in each column and it can be apply in single column as well as on whole DataFrame.
- d.nunique() Apply in whole DataFrame

d.nunique()

# d.nunique() Apply in Single DataFrame

- It will show Total No. of Unique values that are present in particular column(Attribute).

d['MinTemp'].nunique()

# d.value_counts

- This command will show all the unique values with their count(Times or frequency).
- It can be apply in only single column.

d['MinTemp'].value_counts()

d['RainTomorrow'].value_counts() # Show frequency

# d.info()

- This command will provide us basic information about the DataFrame.

d.info()

# d.count

- This command will show total no. of Non-NULL values in each column and it can be apply in single column as well as on whole DataFrame.
- Apply in whole DataFrame

d.count()

# d.notnull().sum()

- This command is used to check all rows amd column are filled or not in our loaded dataframe.

d.notnull().sum()

# d.isnull().sum()

- This command is used to check NULL values present or not in our dataframe.
- isnull command is used to check for null values.

pd.isnull(d).sum()

### In this Data_Frame has NULL values so first of all we have to clean it and then we will apply any kind of operations.

- In above cell we have got null values in following columns :-

 Sunshine          3
 WindGustDir       3
 WindGustSpeed     2
 WindDir9am       31
 WindDir3pm        1
 WindSpeed9am      7

- So we have to remove null values by using drop command.

# drop null values
d.dropna(inplace=True)

# After removing null values.

pd.isnull(d).sum()

# Operation - 1

Rename Column

# Syntax
# d.rename('columns={'Old_Name_Of_Column':'New_Name_Of_Column'})
# Rename Temporary
d.rename(columns={'WindGustDir':'WindGustDirection'})

# Above Command Rename Temporary
d.head(2)

# To Rename Permanently
# Syntax
# d.rename('columns={Old_Name_Of_Column':'New_Name_Of_Column'},inplace=True)
d.rename(columns={'WindGustDir':'WindGustDirection'},inplace=True) # Rename Permanently

# see again it is changed or not?
d.head(2)

# Operation - 2

Calculation of Mean

# Syntax
# d.Column_name.mean()
d.MinTemp.mean()

d.MaxTemp.mean()

d.mean()

d.groupby('MinTemp').mean()

# Operation - 3

Calculation of Standard Deviation

# Syntax
# d.Column_name.std()
d.MinTemp.std()

d.MaxTemp.std()

d.std()

# Operation - 4

Calculation of Variance

# Syntax
# d.Column_name.var()
d.MinTemp.var()

d.MaxTemp.var()

d.var()

# Operation - 5

Calculation of Median

# Syntax
# d.Column_name.median()
d.MinTemp.median()

d.MaxTemp.median()

d.median()

# Operation - 6

Calculation of Mode

# Syntax
# d.Column_name.mode()
d.MinTemp.mode()

d.mode()

# Operation - 7

Calculation of Kurtosis

# Syntax
# d.Column_name.kurt()
# for single attribute
d.MinTemp.kurt()

# For complete attributers
d.kurt()

# Operation - 8

Calculation of Skewness

# Syntax
# d.Column_name.skew()
d.MinTemp.skew()

# For complete attributers
d.skew()

# Operation - 9

Calculation of Correlation

# Syntax
# d.corr()
d.corr()

# Operation - 10

FILTER

We are filtring the records where the attribute RainTomorrow has only Yes.

# Syntax
# d[d['Column_name']=='value']

d[d['RainTomorrow']=='Yes']

# Operation - 11

FILTER

We are filtring the records where the attribute RainTomorrow has only No.

d[d['RainTomorrow']=='No']

# Operation - 12

Calculation of Minimum Value

# This command will give us minimum value from each column.
d.min()

# For Particular column
d['RISK_MM'].min()

d.groupby('MinTemp').min()

# d.sum()

d.sum()

# d.describe()

- This command will show us count, mean, std, min, max of whole dataframe.

d.describe()

# Operation - 13

Calculation of Maximum Value

# This command will give us maximum value from each column.
d.max()

# For Particular column
d['RISK_MM'].max()

d.groupby('MinTemp').max()

# Operation - 14

str.contains

# Retrieved data only if RainToday is Yes

d[(d['RainToday'].str.contains('Yes'))]

d[d['RainToday']=='Yes']

# Operation - 15

d[d['RainToday']=='No']

# If 'RainToday =='No' AND 'Rainfall'==0.0 AND 'RISK_MM'==0.0 Then It May be No Rain Tomorrow

d[(d['RainToday']=='No')&(d['Rainfall']==0.0)&(d['RISK_MM']==0.0)]

d[(d['RainToday']=='Yes')&(d['Rainfall']!=0.0)]

### In this Weather Data Analysis we apply Following Algoriths for Weather prediction :-
 - Decision Tree
 - NBC
 - SVM
 - ARIMA


### I have completed this projet with the help of online resourses and plateform.

- Name - Aatish Kumar Baitha
- M.Tech(Data Science 2nd Year Student)

### My Linkedin Profile -
- www.linkedin.com/in/aatish-kumar-baitha-ba9523191

### My Blog -
- https://computersciencedatascience.blogspot.com/

### 👉 PLEASE CLICK ON .ipynb file to see original view of this project.
### 👉 https://github.com/Aatishkb/Weather-Data-Analysis/blob/main/Weather%20Data%20Analysis%20(1).ipynb

### Thank you!
