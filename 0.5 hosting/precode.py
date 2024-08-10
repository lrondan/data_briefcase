import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import cross_val_predict, cross_val_score, cross_validate

#cargar datos
set_propiedades1 = open('0.5 hosting/datas/230308PreciosCasas.csv','r')
set_propiedades2 = open('0.5 hosting/datas/230718Propiedades.csv','r')