import pandas as pd

with open('UFO_USA_STATES/UFOs_coord.csv', 'r')as file:
    archivo = pd.read_csv(file)
    df1 = pd.DataFrame(data=archivo)

Shape = df1['Shape']
city = df1['City']
Country = df1['Country']
totalShape = Shape.value_counts()
totalcity = city.value_counts()
totalcountry = Country.value_counts()

totalcountry.to_csv('UFO_USA_STATES/UFOxcountry.csv')
totalShape.to_csv('UFO_USA_STATES/UFOxshape.csv')
totalcity.to_csv('UFO_USA_STATES/UFOxcity.csv')