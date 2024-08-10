import pandas as pd

with open('0.5 NASA asteroids/datas/nasa.csv', 'r')as file:
    df = pd.read_csv(file)
    df = pd.DataFrame(data=df)

#creacion de un nuevo dataframe
grupo = df.groupby(df['Hazardous']).value_counts()

print(grupo)
