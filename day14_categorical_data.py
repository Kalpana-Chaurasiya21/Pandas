#importing pandas library

import pandas as pd



#creating dataframe

employees = pd.DataFrame({

    "Employee_Name":[

        "Rahul",

        "Priya",

        "Aman",

        "Neha",

        "Riya",

        "Karan"

    ],

    "Department":[

        "IT",

        "HR",

        "Finance",

        "IT",

        "HR",

        "Finance"

    ]

})



print(employees)



#astype()

#definition

#astype() converts

#one datatype

#into another datatype

#syntax

#series.astype(datatype)

#uses

#used to optimize memory

#used to improve performance

employees["Department"] = employees["Department"].astype(

    "category"

)



print(employees)



#dtypes

#definition

#returns datatype

#of every column

print(

    employees.dtypes

)



#cat.categories

#definition

#returns all

#available categories

#syntax

#series.cat.categories

print(

    employees["Department"].cat.categories

)



#cat.codes

#definition

#returns integer code

#for every category

#syntax

#series.cat.codes

print(

    employees["Department"].cat.codes

)



#cat.add_categories()

#definition

#adds new categories

#without changing data

employees["Department"] = employees["Department"].cat.add_categories(

    "Marketing"

)



print(

    employees["Department"].cat.categories

)



#cat.remove_categories()

#definition

#removes unused category

employees["Department"] = employees["Department"].cat.remove_categories(

    "Marketing"

)



print(

    employees["Department"].cat.categories

)



#value_counts()

print(

    employees["Department"].value_counts()

)



#important interview points

#category saves memory

#category improves performance

#cat.categories returns categories

#cat.codes returns numeric codes