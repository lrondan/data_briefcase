import pandas as pd
import numpy as np
import json

variablescambientea = '1995-02-22'
n=4


with open('0.4 NASA  json/Raw_Data/file1995-02-22.json','r')as file:
    archivo = json.load(file)


objeto_near_earth = archivo['near_earth_objects']
obj = objeto_near_earth[variablescambientea]
obj0 = obj[n]
#name----------------------------------------
name = obj0['name']
neo_ref = obj0['neo_reference_id']
magnitud_absol= obj0['absolute_magnitude_h']
potentially_hazard = obj0['is_potentially_hazardous_asteroid']
#Estimate_diameter----------------------------
diameter = obj0['estimated_diameter']
diameter = diameter['kilometers']
estimated_diameter_min = diameter['estimated_diameter_min']
estimated_diameter_max = diameter['estimated_diameter_max']
#orbital data
orbital =obj0['orbital_data']
velocidad = obj0['close_approach_data']
velocidad = velocidad[0]
velocidad = velocidad['relative_velocity']
velocidad = velocidad['kilometers_per_hour']
#diatancia
distance = obj0['close_approach_data']
distance = distance[0]
body = distance['orbiting_body']
distance = distance['miss_distance']
distance = distance['kilometers']


variable = name, magnitud_absol, potentially_hazard, velocidad,distance, body

data = pd.DataFrame(data=variable)
print(data)

