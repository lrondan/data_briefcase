from sklearn.linear_model import LinearRegression
import pandas as pd

with open('0.6 weather/clima_canada.csv','r')as file1:
    df = pd.read_csv(file1)
    df = pd.DataFrame(data=df)

lr = LinearRegression()
z = df[['UV']]
y = df['Visibilidad']
lr.fit(z,y)

#Ingresar el valor de la medicion de rayos UV
nuevo_uv = float(input('Ingrese el valor de UV:'))
nuevo = {'UV':[nuevo_uv]}
nuevodf = pd.DataFrame(data=nuevo)

Visib_esperada = lr.predict(nuevodf)
print(f'La visibilidad esperada es de :{Visib_esperada}')