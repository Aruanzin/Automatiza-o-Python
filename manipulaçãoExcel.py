import pandas as pd
import math
import numpy as np
from Principal import principal



def leArquivo(fileName, map):
     
    df = pd.read_excel(fileName)

    #firstLine = df.columns
    #tSigla = firstLine[0]


    
    Sigla = 'Endereço-ID'
    dados = ['Cidade', 'Logradouro', 'FORNECEDOR', 'TIPO']
    localizacao = ['Latitude', 'Longitude']


    listaSigla = []
    listaConteudo = []
    listaLoc = []

    for index, row in df.iterrows():
        if row[dados].isnull().values.any() or pd.isna(row[Sigla]):
            raise ValueError(f"Valor vazio na linha {index}")
        else:
            sigla = row[Sigla]
            locationArray = [str (item) for item in row[localizacao] ]
            # conteudoArray = row[dados]
            loc = ' '.join(locationArray)
            conteudo = ' '.join(row[dados])

            # conteudoSemNull = list(filter(lambda x: not math.isnan(x), conteudo))

            listaSigla.append(sigla)
            listaConteudo.append(conteudo)
            listaLoc.append(loc)

    principal(listaSigla, listaConteudo, listaLoc, map)    
    # print("SIGLAS: ", listaSigla,"CONTEUDOS: ", listaConteudo, "LOCALIZACOES: ",listaLoc)        
