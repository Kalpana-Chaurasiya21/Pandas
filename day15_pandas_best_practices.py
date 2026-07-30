#importing pandas library

import pandas as pd



#creating dataframe

employees = pd.DataFrame({

    "Employee_ID":[101,102,103,104,105],

    "Employee_Name":[

        "Rahul",

        "Priya",

        "Aman",

        "Neha",

        "Riya"

    ],

    "Department":[

        "IT",

        "HR",

        "Finance",

        "IT",

        "HR"

    ],

    "Salary":[

        50000,

        65000,

        70000,

        80000,

        60000

    ],

    "Experience":[

        2,

        5,

        6,

        8,

        4

    ]

})



print(employees)



#copy()

#definition

#copy() creates

#a completely

#independent copy

#of dataframe

#syntax

#dataframe.copy()

#uses

#prevents accidental

#changes in

#original dataframe

employees_copy = employees.copy()

employees_copy["Salary"] = employees_copy["Salary"] + 5000



print(employees_copy)

print(employees)



#sample()

#definition

#sample() returns

#random rows

#from dataframe

#syntax

#dataframe.sample()

#uses

#used for testing

#and random inspection

print(

    employees.sample(

        n=2,

        random_state=42

    )

)



#nlargest()

#definition

#returns rows

#having largest

#values

#syntax

#dataframe.nlargest()

print(

    employees.nlargest(

        3,

        "Salary"

    )

)



#nsmallest()

#definition

#returns rows

#having smallest

#values

#syntax

#dataframe.nsmallest()

print(

    employees.nsmallest(

        2,

        "Salary"

    )

)



#sort_index()

#definition

#sorts dataframe

#using index

#instead of

#column values

print(

    employees.sort_index(

        ascending=False

    )

)



#compare()

#definition

#compares two

#dataframes

#and shows

#differences

modified = employees.copy()

modified.loc[0,"Salary"] = 55000



print(

    employees.compare(

        modified

    )

)



#important interview points

#copy() avoids

#unwanted modifications

#sample() selects

#random rows

#nlargest() returns

#highest values

#nsmallest() returns

#lowest values

#compare() finds

#differences between dataframes