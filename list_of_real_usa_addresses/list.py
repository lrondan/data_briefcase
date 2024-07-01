import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open('list_of_real_usa_addresses/list_of_real_usa_addresses.json', 'r')as file:
    listas = pd.read_json(file)
    address = listas['address']
    city = listas['city']
    state = listas['state']
    zip = listas['zip']
    datas = [address, city, state, zip]

df1 = pd.DataFrame(data=datas)
df_test_for_city = df1.iloc[1,:233]
df_test_for_state = df1.iloc[2,:233]

#resumen de personas por estados
state_total=df_test_for_state.value_counts()
plt.plot(state_total)
plt.title('cantidad de personas por estados')
plt.xlabel('estados')
plt.ylabel('cantidad de peronas')
plt.show()

#resumen de personas por ciudades
city_total=df_test_for_city.value_counts()
plt.plot(city_total)
plt.title('cantidad de personas por ciudad')
plt.xlabel('ciudades')
plt.ylabel('cantidad de peronas')
plt.show()
