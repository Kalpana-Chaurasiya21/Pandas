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

        "IT",

        "Finance",

        "HR"

    ],

    "Salary":[

        50000,

        60000,

        70000,

        80000,

        65000

    ]

})



print(employees)



#assign()

#definition

#assign() creates

#new columns

#without modifying

#original dataframe

#syntax

#dataframe.assign()

#uses

#used in

#method chaining

new_df = employees.assign(

    Bonus = employees["Salary"] * 0.10

)



print(new_df)



print(employees)



#multiple assign()

updated_df = employees.assign(

    Bonus = employees["Salary"] * 0.10,

    Total_Salary = employees["Salary"] * 1.10

)



print(updated_df)



#pipe()

#definition

#pipe() passes

#dataframe into

#custom function

#syntax

#dataframe.pipe(function)

#uses

#used to create

#clean pipelines

def increase_salary(df):

    df = df.copy()

    df["Salary"] = df["Salary"] + 5000

    return df



result = employees.pipe(

    increase_salary

)



print(result)



#method chaining

final_df = (

    employees

    .assign(

        Bonus = employees["Salary"] * 0.10

    )

    .query(

        "Salary >= 60000"

    )

    .sort_values(

        by="Salary",

        ascending=False

    )

)



print(final_df)



#important interview points

#assign()

#returns new dataframe

#pipe()

#passes dataframe

#to functions

#method chaining

#improves readability

#original dataframe

#remains unchanged