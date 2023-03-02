# import pandas as pd

# # Replace 'example.xlsx' with the name of your Excel file.
# df = pd.read_excel('/home/johnatas/Documentos/workspace/python/Automatiza-o-Python/data.xlsx')

# # Define a lambda function to combine the values in four columns into a single column.
# combine_columns = df[['Cidade', 'Logradouro', 'FORNECEDOR', 'TIPO']]
# print(combine_columns.head())
# Apply the lambda function to each row in the DataFrame to create a new column.

# Print the updated DataFrame to the console.

import pandas as pd

# Read the Excel file into a pandas dataframe
df = pd.read_excel('/home/johnatas/Documentos/workspace/python/Automatiza-o-Python/data.xlsx')

# Group the data by the first four columns
dados = ['Cidade', 'Logradouro', 'FORNECEDOR', 'TIPO']
localizacao = ['Latitude', 'Longitude']
# Iterate over each group and concatenate the row values
for index, row in df.iterrows():
    conteudo = ' '.join(row[dados])
    locationArray = [str (item) for item in row[localizacao] ]
    loc = ' '.join(locationArray)
    print(conteudo, loc)