import pandas as pd

with open('0.4 NASA  json/nuevos_sets/nset.csv', 'r')as file:
    df = pd.read_csv(file)
    df = pd.DataFrame(data=df)

print('*****************************************************************')
print('**************EL ID EMPIEZA A PARTIR DEL NUMERO [2]**************')
print('*****************************************************************')
lectura = int(input('elegir nombre id del obj: '))

if lectura > 28 or lectura <2:
    print('Error')
    exit()
else:
    seleccion = df.loc[lectura]
    if seleccion['potencial2'] == 1 and seleccion['tiempo']<1500:
        print('Peligro Potencial [[ALTO]]')
    elif seleccion['potencial2']==1 and seleccion['tiempo']>=1500:
        print('Peligro potencial [[Mid]]')
    elif seleccion['potencial2']==0:
        print('Sin peligro')
    else:
        print('Ocurrio algun error...')
        exit()