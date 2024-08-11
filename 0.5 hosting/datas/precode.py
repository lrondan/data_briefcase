import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import cross_val_predict, cross_val_score, cross_validate

#cargar datos y convertir df
with open('0.5 hosting/datas/230308PreciosCasas.csv','r',encoding='utf-8')as file1:
    set_propiedades1 = pd.read_csv(file1)
    set_propiedades1 = pd.DataFrame(data=set_propiedades1)
    
with open('0.5 hosting/datas/230718Propiedades.csv','r',encoding='utf-8')as file2:
    set_propiedades2 = pd.read_csv(file2)
    set_propiedades2 = pd.DataFrame(data=set_propiedades2)

#crear almacen de datos
datos1 = set_propiedades1[['Price_UF','Price_USD','Dorms','Baths','Built Area','Total Area','Parking']]
datos2 = set_propiedades2[['Price_UF','Price_USD','Dorms','Baths','Built Area','Total Area','Parking']]

#pegar un dataframe a continuacion de otro
datalake = pd.concat([datos1, datos2], axis=0)
#exportar el dataframe como datalake
#exportar datalake como datalake.csv
datalake.to_csv('0.5 hosting/datas/datalake.csv')