# https://www.youtube.com/watch?v=9Z7wvippeko
# pandas.pydata.org/pandas-docs/stable/io.html

import pandas as pd

df = pd.read_csv('ZILL-N03111_C.csv') # Specify the path
print(df.head())

df.set_index('Date', inplace=True)

# Save our information to a csv
df.to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv', index_col=0) # Specifying "Date" as the index
#print(df)
print(df.head())

# Renaming columns
df.columns = ['stuff']
print(df.head())

df.to_csv('newcscv3.csv')
df.to_csv('newcsv4.csv', header=False) # write to csv with no header added

df = pd.read_csv('newcsv4.csv', names=['Date','stuff'], index_col=0)
# names = columns
# set index to 0 (index_col=0)

# can use pandas to convert b/w different data types
# csv, etc..

df.to_html('example.html')
df = pd.read_csv('newcsv4', names=['Date','Austin_HPI']) # example of renaming columns (?)
print(df.head())

df.rename(columns={'Austin_HPI':'770asdfasdf'}, inplace=True)
print(df.head()) # above is to rename the 'Austin_HPI' column to '770asdfasdf...'
