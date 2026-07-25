#importing pandas library

import pandas as pd



#creating dataframe

employees = pd.DataFrame({

    "Department":["IT","IT","HR","HR","Finance","Finance"],

    "City":["Delhi","Mumbai","Delhi","Mumbai","Delhi","Mumbai"],

    "Employee":["Rahul","Priya","Aman","Neha","Riya","Karan"],

    "Salary":[50000,70000,45000,60000,80000,65000]

})



print(employees)



#MultiIndex

#definition

#multiindex means using

#more than one index column

#instead of a single index

#it creates hierarchical indexing

#syntax

#dataframe.set_index(["column1","column2"])

#uses

#used for hierarchical data

#used for grouping reports

#used in large datasets



employees = employees.set_index(

    ["Department","City"]

)



print(employees)



#loc[]

#definition

#loc[] is used

#to access rows

#using index labels

#syntax

#dataframe.loc[index]

#uses

#used to retrieve

#specific records



print(

    employees.loc["IT"]

)



print(

    employees.loc[("IT","Delhi")]

)



#reset_index()

#definition

#reset_index()

#converts index

#back into normal columns

#syntax

#dataframe.reset_index()

#uses

#used before exporting data

#used before merging



normal_dataframe = employees.reset_index()



print(normal_dataframe)



#swaplevel()

#definition

#swaplevel() exchanges

#the order of index levels

#syntax

#dataframe.swaplevel()

#uses

#used for reporting

#used before sorting



swapped = employees.swaplevel()



print(swapped)



#sort_index()

#definition

#sort_index()

#sorts the dataframe

#based on index values

#syntax

#dataframe.sort_index()

#uses

#used after creating multiindex



sorted_dataframe = employees.sort_index()



print(sorted_dataframe)



#xs()

#definition

#xs means cross section

#it extracts data

#from one level

#of a multiindex

#syntax

#dataframe.xs(value,level="column")

#uses

#used to filter

#specific groups



print(

    employees.xs(

        "Delhi",

        level="City"

    )

)



#groupby() with multiindex

#definition

#grouping data

#using index levels

salary_summary = employees.groupby(

    level="Department"

)["Salary"].mean()



print(salary_summary)



#important interview points

#multiindex uses multiple indexes

#set_index() creates multiindex

#reset_index() removes multiindex

#swaplevel() exchanges index levels

#sort_index() sorts hierarchical index

#xs() extracts cross sections

#groupby(level=) groups index levels