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

        60000,

        70000,

        80000,

        65000

    ]

})



print(employees)



#set_index()

#definition

#sets a column

#as dataframe index

#index becomes row labels

#index column is removed

#syntax

#dataframe.set_index(column)

#index by employee id

employees_index = employees.set_index(

    "Employee_ID"

)

print(employees_index)



#loc() using new index

print(

    employees_index.loc[103]

)



#reset_index()

#definition

#converts index

#back into column

#syntax

#dataframe.reset_index()

normal_df = employees_index.reset_index()

print(normal_df)



#rename_axis()

#definition

#renames index label

#syntax

#dataframe.rename_axis(name)

renamed = employees_index.rename_axis(

    "ID"

)

print(renamed)



#reindex()

#definition

#changes order

#or adds rows

#syntax

#dataframe.reindex()

new_order = employees_index.reindex(

    [105,103,101,104,102]

)

print(new_order)



#reindex with missing index

new_rows = employees_index.reindex(

    [101,102,106,107]

)

print(new_rows)



#index object

#definition

#returns dataframe index

print(

    employees_index.index

)



#index name

print(

    employees_index.index.name

)



#important interview points

#set_index changes index

#reset_index restores column

#reindex changes order

#rename_axis renames index

#index stores row labels