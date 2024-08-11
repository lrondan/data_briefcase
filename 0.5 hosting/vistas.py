import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

#carga de datos
with open('0.5 hosting/datas/datalake.csv','r',encoding='utf-8')as carga_de_datos:
    df1 = pd.read_csv(carga_de_datos)
    df1 = pd.DataFrame(data=df1)

def UF_prices():
    mediana_de_precios = df1['Price_UF'].median()
    describe_de_precios = df1['Price_UF'].describe()

def USD_prices():
    mediana_de_precios = df1['Price_USD'].median()
    describe_de_precios = df1['Price_USD'].describe()

def bins():
    binnes = np.linspace(min(df1['Price_USD']), max(df1['Price_USD']), 4)
    agrupar = ['Bajo', 'Medio', 'Alto']
    binned = pd.cut(df1['Price_USD'], binnes, labels=agrupar, include_lowest=True).value_counts()
    binned.plot(kind='bar')
    mpl.title('Bins de los precios')
    mpl.ylabel('precio usd')
    mpl.show()
    