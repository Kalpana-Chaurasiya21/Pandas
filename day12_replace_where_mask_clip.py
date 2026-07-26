#importing pandas library

import pandas as pd

import numpy as np



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104,105],

    "Employee_Name":["Rahul","Priya","Aman","Neha","Riya"],

    "Department":["IT","HR","IT","Finance","HR"],

    "Salary":[50000,65000,70000,80000,60000],

    "Experience":[2,4,3,5,1]

})



print(employees)



#replace()

#definition

#replace() replaces old values

#with new values

#it can replace numbers

#strings or multiple values

#syntax

#dataframe.replace(old_value,new_value)

#uses

#used for correcting wrong data

#used for cleaning datasets

employees["Department"] = employees["Department"].replace(

    "HR",

    "Human Resources"

)

print(employees)



#replacing multiple values

employees["Department"] = employees["Department"].replace({

    "IT":"Information Technology",

    "Finance":"Accounts"

})

print(employees)



#where()

#definition

#where() keeps values

#that satisfy a condition

#other values become NaN

#or another specified value

#syntax

#dataframe.where(condition)

#uses

#used for conditional filtering

#used for data cleaning

high_salary = employees["Salary"].where(

    employees["Salary"] >= 65000

)

print(high_salary)



#where() with custom value

salary_check = employees["Salary"].where(

    employees["Salary"] >= 65000,

    "Low Salary"

)

print(salary_check)



#mask()

#definition

#mask() works opposite

#to where()

#it replaces values

#where the condition is True

#syntax

#dataframe.mask(condition)

#uses

#used for hiding

#or replacing unwanted values

masked_salary = employees["Salary"].mask(

    employees["Salary"] > 70000,

    "High Salary"

)

print(masked_salary)



#clip()

#definition

#clip() limits values

#between a minimum

#and maximum value

#syntax

#series.clip(lower,upper)

#uses

#used for removing outliers

#used in preprocessing

clipped_salary = employees["Salary"].clip(

    lower=55000,

    upper=75000

)

print(clipped_salary)



#important interview points

#replace() changes values

#where() keeps values matching condition

#mask() replaces values matching condition

#clip() limits values within a range