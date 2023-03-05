import pandas as pd

def leArquivo(fileName):
     
    df = pd.read_excel(fileName)
    
    first_row = df.head(1)
