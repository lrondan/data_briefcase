import pandas as pd
with open('0.7 Canada immegration/new_train.csv','r')as file:
    archi = pd.read_csv(file)
    df = pd.DataFrame(data=archi)
    
Cont = df['Etiquetas de fila']
v00 = df['Suma de 2000']
v01 = df['Suma de 2001']
v02 = df['Suma de 2002']
v03 = df['Suma de 2003']
v04 = df['Suma de 2004']
v05 = df['Suma de 2005']
v06 = df['Suma de 2006']
v07 = df['Suma de 2007']
v08 = df['Suma de 2008']
v09 = df['Suma de 2009']
v10 = df['Suma de 2010']
v11 = df['Suma de 2011']
v12 = df['Suma de 2012']
v_comparable_13 = df['Suma de 2013']
print(v_comparable_13)