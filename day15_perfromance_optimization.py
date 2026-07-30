#importing pandas library

import pandas as pd

import numpy as np



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104,105,106,107,108],

    "Department":[

        "IT",

        "HR",

        "Finance",

        "IT",

        "HR",

        "Finance",

        "IT",

        "Marketing"

    ],

    "Salary":[

        50000,

        60000,

        70000,

        80000,

        65000,

        72000,

        90000,

        55000

    ],

    "Experience":[

        2,

        5,

        7,

        8,

        4,

        6,

        10,

        3

    ]

})



print(employees)



#memory_usage()

#definition

#returns memory

#used by dataframe

#syntax

#dataframe.memory_usage()

print(

    employees.memory_usage()

)



#memory_usage(deep=True)

#definition

#calculates exact

#memory including

#object columns

print(

    employees.memory_usage(

        deep=True

    )

)



#info()

#definition

#shows dataframe summary

#including memory

employees.info(

    memory_usage="deep"

)



#query()

#definition

#filters dataframe

#using expressions

#syntax

#dataframe.query()

high_salary = employees.query(

    "Salary > 65000"

)

print(high_salary)



#boolean indexing

filtered = employees[

    employees["Salary"] > 65000

]

print(filtered)



#eval()

#definition

#evaluates expressions

#efficiently

#syntax

#dataframe.eval()

employees.eval(

    "Bonus = Salary * 0.10",

    inplace=True

)

print(employees)



#category datatype

#improves memory

employees["Department"] = employees["Department"].astype(

    "category"

)



print(

    employees.dtypes

)



print(

    employees.memory_usage(

        deep=True

    )

)



#important interview points

#query() improves readability

#eval() speeds calculations

#category saves memory

#deep=True shows exact memory

#avoid loops in pandas