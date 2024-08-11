import pandas as pd
from sklearn.linear_model import LinearRegression
import desktop
from tkinter import messagebox as mBox
#-----------------------------------------------------------
#valores enlazados a la aplicacion
dormitorios = 3
banos = 2
constr_area = 123
total_area = 234
parking = 1
valores = {'Dorms':[dormitorios],'Baths':[banos],'Built Area':[constr_area],'Total Area':[total_area],'Parking':[parking]}
valores = pd.DataFrame(data=valores)
#------------------------------------------------------------
#importar el datalake
with open('0.5 hosting/datas/datalake.csv','r',encoding='utf-8')as carga_de_datos:
    df1 = pd.read_csv(carga_de_datos)
    df1 = pd.DataFrame(data=df1)

x_values =df1[['Dorms','Baths','Built Area','Total Area','Parking']]
y_values =df1[['Price_USD','Price_UF']]

#crear objeto
lr = LinearRegression()
#entrenar los datos MLR
lr.fit(x_values, y_values)
#esperar las respuestas y ver datos en pantalla como prueba
Yhat = lr.predict(valores)
Yhat.astype(int)
#valores vistos segun scoresFUNCT
#mBox.showinfo('Precios USD-UF',f'{Yhat}')


    