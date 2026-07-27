#importing pandas library

import pandas as pd



#creating dataframe

students = pd.DataFrame({

    "Student_ID":[101,102,103],

    "Name":["Rahul","Priya","Aman"],

    "Math_2023":[90,85,88],

    "Math_2024":[92,87,91],

    "Science_2023":[86,82,89],

    "Science_2024":[91,85,93]

})



print(students)



#wide_to_long()

#definition

#wide_to_long()

#converts wide format

#into long format

#using common prefixes

#syntax

#pd.wide_to_long(dataframe,stubnames,i,j)

#uses

#used when columns

#follow a naming pattern

#used for yearly data

long_data = pd.wide_to_long(

    students,

    stubnames=["Math","Science"],

    i="Student_ID",

    j="Year",

    sep="_",

    suffix="\d+"

)



print(long_data)



#reset index

long_data = long_data.reset_index()

print(long_data)



#Styler

#definition

#Styler formats

#dataframes

#without changing

#original data

#syntax

#dataframe.style

#uses

#used for reports

#used before exporting

styled = students.style



#highlight maximum value

highlight_maximum = students.style.highlight_max(

    subset=["Math_2024"],

    color="lightgreen"

)



print(highlight_maximum)



#highlight minimum value

highlight_minimum = students.style.highlight_min(

    subset=["Science_2024"],

    color="pink"

)



print(highlight_minimum)



#background gradient

gradient = students.style.background_gradient(

    subset=["Math_2024","Science_2024"]

)



print(gradient)



#format numbers

formatted = students.style.format({

    "Math_2024":"{:.2f}",

    "Science_2024":"{:.2f}"

})



print(formatted)



#hide index

hidden_index = students.style.hide(axis="index")



print(hidden_index)



#important interview points

#wide_to_long() reshapes wide data

#works with repeated column prefixes

#Styler formats dataframe display

#Styler does not modify original data

#Styler is mainly used in reports