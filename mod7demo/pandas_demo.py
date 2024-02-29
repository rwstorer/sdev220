import pandas as pd

# read top 10 rows
df = pd.read_csv('C:/Users/rwsto/OneDrive/IvyTech/SDEV220-Python/mod7demo/telco_churn.csv')
print(df.head(10))

# print bottom five rows
print(df.tail())

# print all column names
print(df.columns)

# print the data types
print(df.dtypes)

# print statistics--minus objects
print(df.describe())

# print stats w/objects
print(df.describe(include='object'))

# print two columns of data
print(df[['State', 'International plan']])

# print unique values in a column
print(df.Churn.unique())

# print rows that match a column value
print(df[df['International plan']=='No'])

# print rows that match two columns
print(df[(df['International plan']=='No') & (df['Churn']==False)])

# print a specific row number
print(df.iloc[14])

# print a specific row and column
print(df.iloc[14, 0])

# print a specific range of rows
print(df.iloc[23:33])

tempdict: dict = {'col1': [1,2,3], 'col2': [4,5,6],
                  'col3': [7,8,9]}

# convert a dictionary to a dataframe
dictdf: pd.DataFrame = pd.DataFrame.from_dict(tempdict)
print(dictdf.head())

# make a dataframe copy and create an index
state: pd.DataFrame = df.copy()
state.set_index('State', inplace=True)

# print rows on a specific indexed column value
print(state.loc['OH'])

# print the sum of rows where each column has a null
print(df.isnull().sum())

# drop all the null values
df.dropna(inplace=True)

# drop/delete an entire column
df.drop('Area code', axis=1)

# Create a calculated column
df['Sum Minutes'] = df['Total night minutes'] + df['Total intl minutes']
print(df.head())

# update all columns and a single column
df['Sum Minutes'] = 100 # all
df.iloc[0, -1] = 10 # row 0, last column

# add a calculated field using a lambda
df['Curn Binary'] = df['Churn'].apply(lambda x: 1 if x==True else 0)

# df conversions
df.to_csv('output.csv')
df.to_json()
df.to_html()

# delete the df
del df
