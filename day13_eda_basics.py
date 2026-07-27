#importing pandas library

import pandas as pd



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104,105,106],

    "Employee_Name":["Rahul","Priya","Aman","Neha","Riya","Karan"],

    "Department":["IT","HR","IT","Finance","HR","Finance"],

    "Salary":[50000,65000,70000,80000,60000,75000],

    "Experience":[2,5,3,7,4,6]

})



print(employees)



#shape

#definition

#shape returns

#number of rows

#and columns

#syntax

#dataframe.shape

#uses

#used to know

#dataset size

print(employees.shape)



#columns

#definition

#returns all

#column names

#syntax

#dataframe.columns

#uses

#used before analysis

print(employees.columns)



#index

#definition

#returns row indexes

#syntax

#dataframe.index

print(employees.index)



#info()

#definition

#shows dataframe summary

#including datatypes

#missing values

#memory usage

#syntax

#dataframe.info()

#uses

#first function

#used in every project

employees.info()



#describe()

#definition

#returns statistical summary

#of numeric columns

#syntax

#dataframe.describe()

#uses

#used to understand

#dataset quickly

print(employees.describe())



#describe()

#definition

#returns summary

#for text columns

print(

    employees.describe(

        include="object"

    )

)



#dtypes

#definition

#shows datatype

#of every column

print(

    employees.dtypes

)



#unique()

#definition

#returns unique values

#syntax

#series.unique()

#uses

#used for checking

#categorical data

print(

    employees["Department"].unique()

)



#nunique()

#definition

#returns number

#of unique values

#syntax

#series.nunique()

print(

    employees["Department"].nunique()

)



#value_counts()

#definition

#counts frequency

#of every value

#syntax

#series.value_counts()

#uses

#used for category analysis

print(

    employees["Department"].value_counts()

)



#important interview points

#shape returns rows and columns

#info() summarizes dataframe

#describe() gives statistics

#unique() returns distinct values

#nunique() counts unique values

#value_counts() counts frequencies