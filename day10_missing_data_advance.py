#importing pandas library

import pandas as pd

import numpy as np



#creating dataframe

students = pd.DataFrame({

    "Student_ID":[101,102,103,104,105,106],

    "Name":["Rahul","Priya",None,"Neha","Aman",None],

    "Marks":[85,np.nan,76,90,np.nan,88],

    "City":["Delhi","Mumbai",None,"Lucknow","Delhi","Pune"]

})



print(students)



#isna()

#definition

#isna() checks whether

#a value is missing

#it returns True for missing values

#syntax

#dataframe.isna()

#uses

#used for finding missing values

#used before data cleaning

print(

    students.isna()

)



#notna()

#definition

#notna() checks

#whether values are present

#it returns True

#for non missing values

#syntax

#dataframe.notna()

#uses

#used for filtering valid records

print(

    students.notna()

)



#fillna()

#definition

#fillna() replaces

#missing values

#syntax

#dataframe.fillna(value)

#uses

#used for filling missing values

#without deleting records

filled_students = students.fillna({

    "Name":"Unknown",

    "Marks":0,

    "City":"Not Available"

})



print(filled_students)



#ffill()

#definition

#ffill means forward fill

#it copies the previous value

#to the missing value

#syntax

#dataframe.ffill()

#uses

#used in time series data

forward_fill = students.ffill()

print(forward_fill)



#bfill()

#definition

#bfill means backward fill

#it copies the next value

#to the missing value

#syntax

#dataframe.bfill()

#uses

#used when future value

#can replace missing value

backward_fill = students.bfill()

print(backward_fill)



#interpolate()

#definition

#interpolate() estimates

#missing numeric values

#between existing values

#syntax

#series.interpolate()

#uses

#used in sensor data

#used in financial analysis

students["Marks"] = students["Marks"].interpolate()

print(students)



#dropna()

#definition

#dropna() removes

#rows having missing values

#syntax

#dataframe.dropna()

#uses

#used when missing records

#are not useful

clean_students = students.dropna()

print(clean_students)



#dropna()

#definition

#axis=1 removes columns

#containing missing values

column_removed = students.dropna(

    axis=1

)

print(column_removed)



#important interview points

#isna() checks missing values

#notna() checks available values

#fillna() fills missing values

#ffill() copies previous value

#bfill() copies next value

#interpolate() estimates missing numeric values

#dropna() removes rows or columns