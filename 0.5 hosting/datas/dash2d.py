import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import webbrowser

#load data
hosting_data = pd.read_csv('0.5 hosting/datas/datalake.csv', encoding='ISO-8859-1')
app = dash.Dash()
#diseno de la app layout
app.layout = html.Div(children=[html.H1('Hosting :', style={'TextAlign':'center', 'font-size':40}), 
                                html.Div(['Input', dcc.Input(id='Input-price',
                                                             value='15000', type='number')],
                                         style={'font-size':40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id = 'bar-plot'))])

@app.callback(Output(component_id='bar-plot', component_property='figure'),
              Input(component_id='Input-price', component_property='value'))

def get_graph(entered_price_usd):
    #select data
    with open('0.5 hosting/datas/datalake.csv','r',encoding='utf-8')as carga_de_datos:
        df1 = pd.read_csv(carga_de_datos)
        df1 = pd.DataFrame(data=df1)
        df1['Price_USD']==int(entered_price_usd)
    #agrupar data
    grupo1 = df1.groupby(['Dorms'])['Price_USD'].sum().nlargest(15).reset_index()
    #plot data
    fig1 = px.bar(grupo1, x='Dorms', y='Price_USD', 
                  title='Ascenso total de los precios de las casas por dormitorios')
    fig1.update_layout()
    return fig1


def servicio():
    webbrowser.open(url='http://127.0.0.1:8802/')
    


if __name__ == '__main__':
    servicio()
    app.run_server(port=8802, host='127.0.0.1', debug=True)


    
