#importing pandas library

import pandas as pd



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104,105,106,107,108],

    "Employee_Name":["Rahul","Priya","Aman","Neha","Riya","Karan","Ankit","Simran"],

    "Department":["IT","HR","IT","Finance","HR","Finance","IT","Marketing"],

    "Salary":[50000,60000,65000,70000,72000,68000,75000,55000],

    "Experience":[2,5,3,7,4,6,5,2]

})



print(employees)



#groupby()

#definition

#groupby() groups

#rows having

#the same values

#syntax

#dataframe.groupby(column)

#uses

#used for comparing

#categories

department_salary = employees.groupby(

    "Department"

)["Salary"].mean()

print(department_salary)



#groupby() with multiple aggregations

#definition

#agg() performs

#multiple calculations

#syntax

#groupby().agg()

salary_summary = employees.groupby(

    "Department"

).agg({

    "Salary":["mean","min","max"],

    "Experience":["mean","max"]

})



print(salary_summary)



#sort_values()

#definition

#sorts dataframe

#by column values

#syntax

#dataframe.sort_values()

#uses

#used to find

#highest salary

sorted_salary = employees.sort_values(

    by="Salary",

    ascending=False

)

print(sorted_salary)



#corr()

#definition

#corr() calculates

#correlation

#between numeric columns

#syntax

#dataframe.corr()

#uses

#used to check

#relationship strength

correlation = employees[

    ["Salary","Experience"]

].corr()



print(correlation)



#cov()

#definition

#cov() calculates

#covariance

#between numeric columns

#syntax

#dataframe.cov()

#uses

#used in statistics

covariance = employees[

    ["Salary","Experience"]

].cov()



print(covariance)



#crosstab()

#definition

#crosstab()

#creates frequency table

#between categories

#syntax

#pd.crosstab()

#uses

#used to compare

#categorical variables

cross_table = pd.crosstab(

    employees["Department"],

    employees["Experience"]

)



print(cross_table)



#important interview points

#groupby() compares categories

#agg() performs multiple calculations

#corr() measures relationship

#cov() measures joint variation

#crosstab() compares categories