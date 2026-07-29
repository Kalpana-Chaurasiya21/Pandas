#importing pandas library

import pandas as pd



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104,105,106,107,108],

    "Employee_Name":["Rahul","Priya","Aman","Neha","Riya","Karan","Ankit","Simran"],

    "Department":["IT","HR","IT","Finance","HR","Finance","IT","Marketing"],

    "Gender":["Male","Female","Male","Female","Female","Male","Male","Female"],

    "Salary":[50000,60000,65000,70000,72000,68000,75000,55000],

    "Experience":[2,5,3,7,4,6,5,2]

})



print(employees)



#groupby() with multiple columns

#definition

#groups data

#using multiple columns

#syntax

#dataframe.groupby([column1,column2])

#uses

#used for detailed

#business analysis

grouped_data = employees.groupby(

    ["Department","Gender"]

).mean(

    numeric_only=True

)

print(grouped_data)



#agg()

#definition

#performs multiple

#calculations together

#syntax

#groupby().agg()

summary = employees.groupby(

    ["Department","Gender"]

).agg({

    "Salary":["mean","min","max"],

    "Experience":["mean","sum"]

})



print(summary)



#pivot_table()

#definition

#creates summary table

#from dataframe

#syntax

#pd.pivot_table()

#uses

#used in dashboards

pivot = pd.pivot_table(

    employees,

    values="Salary",

    index="Department",

    columns="Gender",

    aggfunc="mean"

)



print(pivot)



#multiple values

pivot_multiple = pd.pivot_table(

    employees,

    values=[

        "Salary",

        "Experience"

    ],

    index="Department",

    columns="Gender",

    aggfunc="mean"

)



print(pivot_multiple)



#margins

#definition

#margins=True

#adds total rows

#and columns

pivot_total = pd.pivot_table(

    employees,

    values="Salary",

    index="Department",

    columns="Gender",

    aggfunc="mean",

    margins=True

)



print(pivot_total)



#important interview points

#multivariate analysis studies

#three or more variables

#pivot_table creates

#business summaries

#groupby supports

#multiple columns

#margins=True

#adds grand totals