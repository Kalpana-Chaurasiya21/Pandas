#importing pandas library

import pandas as pd



#creating dataframe

students = pd.DataFrame({

    "Student":["Rahul","Priya","Aman"],

    "Math":[90,85,88],

    "Science":[92,80,91],

    "English":[87,89,84]

})



print(students)



#melt()

#definition

#melt() converts

#wide format data

#into long format

#syntax

#pd.melt(dataframe,id_vars,value_vars)

#uses

#used before visualization

#used for data transformation

melted = pd.melt(

    students,

    id_vars="Student",

    var_name="Subject",

    value_name="Marks"

)



print(melted)



#pivot()

#definition

#pivot() converts

#long format

#back into wide format

#syntax

#dataframe.pivot(index,columns,values)

#uses

#used to reshape data

#used after melt()

pivoted = melted.pivot(

    index="Student",

    columns="Subject",

    values="Marks"

)



print(pivoted)



#creating another dataframe

sales = pd.DataFrame({

    "City":["Delhi","Delhi","Mumbai","Mumbai"],

    "Product":["Laptop","Mouse","Laptop","Mouse"],

    "Sales":[50000,2000,60000,2500]

})



print(sales)



#set_index()

sales = sales.set_index(

    ["City","Product"]

)



print(sales)



#stack()

#definition

#stack() moves

#column labels

#into row index

#creating a multiindex

#syntax

#dataframe.stack()

#uses

#used for reshaping

#used in advanced analysis

stacked = pivoted.stack()

print(stacked)



#unstack()

#definition

#unstack() moves

#index values

#back into columns

#syntax

#dataframe.unstack()

#uses

#used to reverse stack()

unstacked = stacked.unstack()

print(unstacked)



#important interview points

#melt() converts wide data into long format

#pivot() converts long data into wide format

#stack() converts columns into index

#unstack() converts index into columns

#pivot() fails if duplicate index column combinations exist

#pivot_table() can handle duplicate values