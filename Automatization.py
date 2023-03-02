import pandas as pd

# Replace 'example.xlsx' with the name of your Excel file.
df = pd.read_excel('PROGRAMAÇÃO SC - CLAUDIO.xlsx')

# Define a lambda function to combine the values in four columns into a single column.
combine_columns = lambda row: ', '.join([str(row['Column1']), str(row['Column2']), str(row['Column3']), str(row['Column4'])])

# Apply the lambda function to each row in the DataFrame to create a new column.
df['GroupedColumn'] = df.apply(combine_columns, axis=1)

# Print the updated DataFrame to the console.
print(df)
