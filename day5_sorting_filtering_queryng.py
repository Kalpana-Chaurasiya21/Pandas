#importing pandas library

import pandas as pd



#Sorting, Filtering and Querying Data

#definition

#sorting means arranging data

#in ascending or descending order

#filtering means selecting only those rows

#that satisfy a given condition

#querying means retrieving data

#using readable expressions



#creating dataframe

students = pd.DataFrame({

    "Student_ID":[101,102,103,104,105,106],

    "Name":["Rahul","Priya","Aman","Neha","Riya","Karan"],

    "Marks":[85,92,76,88,95,67],

    "City":["Delhi","Mumbai","Delhi","Lucknow","Pune","Delhi"]

})



print(students)



#--------------------------------------------------

#sort_values()

#definition

#sort_values() sorts dataframe

#based on column values

#ascending=True by default

print(students.sort_values("Marks"))



#sorting in descending order

print(students.sort_values(

    by="Marks",

    ascending=False

))



#sorting by multiple columns

print(students.sort_values(

    by=["City","Marks"],

    ascending=[True,False]

))



#--------------------------------------------------

#sort_index()

#definition

#sort_index() sorts dataframe

#according to row index

print(students.sort_index())



#sorting index in reverse order

print(students.sort_index(

    ascending=False

))



#--------------------------------------------------

#Filtering

#definition

#filtering selects rows

#that satisfy a condition



#students having marks greater than 80

print(

    students[students["Marks"] > 80]

)



#students from Delhi

print(

    students[students["City"] == "Delhi"]

)



#students having marks greater than 80

#and belonging to Delhi

print(

    students[

        (students["Marks"] > 80)

        &

        (students["City"] == "Delhi")

    ]

)



#students from Delhi or Mumbai

print(

    students[

        (students["City"] == "Delhi")

        |

        (students["City"] == "Mumbai")

    ]

)



#--------------------------------------------------

#isin()

#definition

#checks whether values

#are present in a list

print(

    students[

        students["City"].isin(

            ["Delhi","Pune"]

        )

    ]

)



#--------------------------------------------------

#between()

#definition

#checks whether values

#lie within a range

print(

    students[

        students["Marks"].between(80,90)

    ]

)



#--------------------------------------------------

#query()

#definition

#query() filters dataframe

#using readable expressions

print(

    students.query(

        "Marks > 80"

    )

)



print(

    students.query(

        "City == 'Delhi'"

    )

)



print(

    students.query(

        "Marks > 80 and City == 'Delhi'"

    )

)



#--------------------------------------------------

#nlargest()

#definition

#returns top n largest values

print(

    students.nlargest(

        3,

        "Marks"

    )

)



#--------------------------------------------------

#nsmallest()

#definition

#returns top n smallest values

print(

    students.nsmallest(

        2,

        "Marks"

    )

)



#--------------------------------------------------

#real world example

employees = pd.DataFrame({

    "Employee":["Amit","Riya","Neha","Karan","Mohit"],

    "Salary":[25000,60000,45000,80000,35000],

    "Department":["HR","IT","Finance","IT","HR"]

})



#employees with salary above 40000

print(

    employees[

        employees["Salary"] > 40000

    ]

)



#top 2 highest paid employees

print(

    employees.nlargest(

        2,

        "Salary"

    )

)



#important interview points

#sort_values() sorts using column values

#sort_index() sorts using row index

#filtering uses conditions

#& means logical AND

#| means logical OR

#isin() checks multiple values

#between() checks a range

#query() filters using expressions

#nlargest() returns highest values

#nsmallest() returns lowest values