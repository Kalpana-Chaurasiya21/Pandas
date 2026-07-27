#importing pandas library

import pandas as pd

import numpy as np



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,103,105,106],

    "Employee_Name":["Rahul","Priya",None,"Aman","Riya","Karan"],

    "Department":["IT","HR","IT","IT",None,"Finance"],

    "Salary":[50000,np.nan,70000,70000,60000,75000],

    "Experience":[2,5,3,3,np.nan,6]

})



print(employees)



#isnull()

#definition

#isnull() checks

#whether each value

#is missing

#syntax

#dataframe.isnull()

#uses

#used to identify

#missing values

print(

    employees.isnull()

)



#isnull().sum()

#definition

#counts missing values

#in every column

#syntax

#dataframe.isnull().sum()

#uses

#used before

#data cleaning

print(

    employees.isnull().sum()

)



#isnull().sum().sum()

#definition

#counts total missing values

#in the dataframe

#syntax

#dataframe.isnull().sum().sum()

print(

    employees.isnull().sum().sum()

)



#duplicated()

#definition

#checks duplicate rows

#returns True

#for duplicate records

#syntax

#dataframe.duplicated()

#uses

#used before

#removing duplicates

print(

    employees.duplicated()

)



#duplicated().sum()

#definition

#counts duplicate rows

print(

    employees.duplicated().sum()

)



#drop_duplicates()

#definition

#removes duplicate rows

#from dataframe

#syntax

#dataframe.drop_duplicates()

#uses

#used to clean

#duplicate records

employees = employees.drop_duplicates()



print(employees)



#fillna()

#definition

#fills missing values

#using custom values

#syntax

#dataframe.fillna(value)

employees["Employee_Name"] = employees["Employee_Name"].fillna(

    "Unknown"

)



employees["Department"] = employees["Department"].fillna(

    "Not Assigned"

)



employees["Salary"] = employees["Salary"].fillna(

    employees["Salary"].mean()

)



employees["Experience"] = employees["Experience"].fillna(

    employees["Experience"].median()

)



print(employees)



#checking again

print(

    employees.isnull().sum()

)



#important interview points

#isnull() checks missing values

#isnull().sum() counts missing values

#duplicated() finds duplicate rows

#drop_duplicates() removes duplicate rows

#fillna() replaces missing values

#mean() used for numeric columns

#median() useful when outliers exist