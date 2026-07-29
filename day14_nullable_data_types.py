#importing pandas library

import pandas as pd

import numpy as np



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,None,104,105],

    "Employee_Name":[

        "Rahul",

        "Priya",

        "Aman",

        None,

        "Riya"

    ],

    "Salary":[50000,60000,None,70000,65000],

    "Is_Active":[True,False,None,True,False]

})



print(employees)



#dtypes

#definition

#returns datatype

#of every column

print(

    employees.dtypes

)



#astype()

#definition

#astype() converts

#one datatype

#into another datatype

#syntax

#series.astype(datatype)

#uses

#used to use

#nullable datatypes

employees["Employee_ID"] = employees["Employee_ID"].astype(

    "Int64"

)



employees["Employee_Name"] = employees["Employee_Name"].astype(

    "string"

)



employees["Is_Active"] = employees["Is_Active"].astype(

    "boolean"

)



print(employees)



#printing datatypes

print(

    employees.dtypes

)



#checking missing values

print(

    employees.isna()

)



#counting missing values

print(

    employees.isna().sum()

)



#fillna()

#definition

#fills missing values

#syntax

#series.fillna(value)

employees["Employee_ID"] = employees["Employee_ID"].fillna(

    999

)



employees["Employee_Name"] = employees["Employee_Name"].fillna(

    "Unknown"

)



employees["Is_Active"] = employees["Is_Active"].fillna(

    False

)



employees["Salary"] = employees["Salary"].fillna(

    employees["Salary"].mean()

)



print(employees)



#printing datatypes again

print(

    employees.dtypes

)



#important interview points

#Int64 supports missing integers

#string supports missing text

#boolean supports missing True False values

#nullable datatypes use pd.NA internally

#better than normal int float object for missing data