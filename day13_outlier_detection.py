#importing pandas library

import pandas as pd

import numpy as np



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104,105,106,107,108],

    "Employee_Name":["Rahul","Priya","Aman","Neha","Riya","Karan","Ankit","Simran"],

    "Salary":[50000,60000,65000,70000,72000,68000,75000,300000]

})



print(employees)



#describe()

#definition

#describe() returns

#statistical summary

#of numeric columns

#syntax

#dataframe.describe()

#uses

#used to identify

#minimum maximum

#and unusual values

print(

    employees.describe()

)



#quantile()

#definition

#quantile() returns

#the specified percentile

#syntax

#series.quantile(value)

#uses

#used for IQR calculation

Q1 = employees["Salary"].quantile(0.25)

Q3 = employees["Salary"].quantile(0.75)



print("Q1 :",Q1)

print("Q3 :",Q3)



#IQR

#definition

#IQR means

#Inter Quartile Range

#formula

#IQR = Q3 - Q1

#uses

#used to detect outliers

IQR = Q3 - Q1

print("IQR :",IQR)



#lower limit

lower_limit = Q1 - 1.5 * IQR

print("Lower Limit :",lower_limit)



#upper limit

upper_limit = Q3 + 1.5 * IQR

print("Upper Limit :",upper_limit)



#finding outliers

#definition

#outliers are values

#outside lower

#or upper limit

outliers = employees[

    (employees["Salary"] < lower_limit)

    |

    (employees["Salary"] > upper_limit)

]



print(outliers)



#removing outliers

clean_data = employees[

    (employees["Salary"] >= lower_limit)

    &

    (employees["Salary"] <= upper_limit)

]



print(clean_data)



#clipping outliers

#definition

#clip() limits values

#within a range

employees["Salary"] = employees["Salary"].clip(

    lower=lower_limit,

    upper=upper_limit

)



print(employees)



#important interview points

#Q1 is 25th percentile

#Q3 is 75th percentile

#IQR = Q3 - Q1

#values outside limits are outliers

#clip() caps extreme values

#outliers can be removed or capped