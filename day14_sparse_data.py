#importing pandas library

import pandas as pd

import numpy as np



#creating normal dataframe

sales = pd.DataFrame({

    "Jan":[0,0,0,1200,0,0,1500,0,0,0],

    "Feb":[0,0,0,1300,0,0,1700,0,0,0],

    "Mar":[0,0,0,1400,0,0,1800,0,0,0]

})



print(sales)



#memory usage

#definition

#returns memory

#used by dataframe

#syntax

#dataframe.memory_usage()

print(

    sales.memory_usage(deep=True)

)



#converting to sparse datatype

#definition

#SparseDtype stores

#only non-zero values

#syntax

#astype(pd.SparseDtype())

sales_sparse = sales.astype(

    pd.SparseDtype(

        "float",

        fill_value=0

    )

)



print(sales_sparse)



#printing datatypes

print(

    sales_sparse.dtypes

)



#memory usage after conversion

print(

    sales_sparse.memory_usage(deep=True)

)



#checking sparse density

#definition

#density tells

#how much real

#data exists

print(

    sales_sparse["Jan"].sparse.density

)



#converting back to normal

sales_dense = sales_sparse.sparse.to_dense()



print(sales_dense)



#important interview points

#sparse data

#contains many repeated values

#usually zeros

#SparseDtype saves memory

#to_dense converts

#back to normal dataframe