# Importing required libraries.
import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
#matplotlib inline 
sns.set(color_codes=True)

from a_create_database import create_database
# Create the database
create_database()

#Step 1: Read JSON File into a Pandas DataFrame
df = pd.read_json("tweets_extraction.json")

#Cleaning the hashtag field, since it is a list and myssql doesn't support list
def clean(x):
    x = ','.join(x)
    return str(x)

df['hashtags'] = df['hashtags'].apply(clean)

# To display the rows
print("\n\nTo display Rows\n")
print(df.shape)

# To display the top 10 rows
print("\n\nTo display the top 10 rows\n")
print(df.head(10))

# Checking the data type
print("\n\nChecking the data type\n")
print(df.dtypes)

# Total number of rows and columns
print("\n\nTotal number of rows and columns:",df.shape)

# Rows containing duplicate data
duplicate_rows_df = df[df.duplicated()]
print("\n\nNumber of duplicate rows: ", duplicate_rows_df.shape)

# Used to count the number of rows before removing the data
print("\n\nUsed to count the number of rows before removing the data:\n",df.count())

# Dropping the duplicates
df = df.drop_duplicates()
print("\n\nDropping the duplicates",df.head(5))
print("\n\nUsed to count the number of rows before removing the data:\n",df.count())

# Dropping the missing values.
df = df.dropna()
print("\n\nDropping the missing values.\n",df.count())

# After dropping the values
print("",df.isnull().sum())
print("\n\nAfter dropping the values:\n",
df.head(5),"\n\n",df.tail(5))

# Total number of rows and columns
print("\n\nTotal number of rows and columns:",df.shape[0])

#Insert the data into the database
from b_insert_table_into_mysql import insert_table
insert_table("tweets",df)




    
