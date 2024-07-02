import pandas as pd
import csv

archivo = '0.5 PornHub models/Models by country.csv'
with open(archivo,'r')as file:
    datas = pd.read_csv(file)
    df = pd.DataFrame(data=datas)

countries = df['Countries'].value_counts()

print(countries)