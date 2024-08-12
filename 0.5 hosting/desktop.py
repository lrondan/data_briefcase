import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
from sklearn.linear_model import LinearRegression
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mBox
import webbrowser

#carga de datos obligatoria
with open('0.5 hosting/datas/datalake.csv','r',encoding='utf-8')as carga_de_datos:
    df1 = pd.read_csv(carga_de_datos)
    df1 = pd.DataFrame(data=df1)

class Ventana:
    def __init__(self, interfaz) -> None:
        self.app = interfaz
        self.app.geometry('540x210')
        self.app.title('Hosting')
        self.app.resizable(0,0)
        self.app.config(bg='gray')
        self.Labels()
        self.Entradas()
        self.Botones()
        self.SetPrecios()

    def Labels(self):
        Label(text='Valores en USD', justify=CENTER, font='BOLD',width=12).grid(row=0, column=0)
        Label(text='Dormitorios: ', justify=RIGHT, font='BOLD',width=12).grid(row=1, column=0, sticky=W)
        Label(text='Baños: ', justify=RIGHT, font='BOLD',width=12).grid(row=2, column=0, sticky=W)
        Label(text='Area constr: ', justify=RIGHT, font='BOLD',width=12).grid(row=3, column=0, sticky=W)
        Label(text='Area total: ', justify=RIGHT, font='BOLD',width=12).grid(row=4, column=0, sticky=W)
        Label(text='Parking:', justify=RIGHT, font='BOLD',width=12).grid(row=5, column=0, sticky=W)
        Label(text='', justify=RIGHT, font='BOLD',width=12).grid(row=1, column=1, sticky=W)
        Label(text='Valor USD:', justify=RIGHT, font='BOLD',width=12).grid(row=1, column=3, sticky=W)
        Label(text='Valor UF:', justify=RIGHT, font='BOLD',width=12).grid(row=2, column=3, sticky=W)
        #Label(text='', justify=RIGHT, font='BOLD',width=12).grid(row=5, column=1, sticky=W)
    
    def SetPrecios(self):
        self.ValorUF = IntVar()
        self.ValorUSD = IntVar()
        Entry(textvariable=self.ValorUF, justify=RIGHT, font='BOLD',width=12, relief=SUNKEN).grid(row=1, column=4, sticky=W)
        Entry(textvariable=self.ValorUSD, justify=RIGHT, font='BOLD',width=12, relief=SUNKEN).grid(row=2, column=4, sticky=W)


    def Entradas(self):
        self.Dormitorios = IntVar()
        self.Banos = IntVar()
        self.Area_const = IntVar()
        self.Area_tot = IntVar()
        self.Parking = IntVar()
        Entry(textvariable=self.Dormitorios, justify=RIGHT, width=8, bd=3).grid(row=1, column=1, sticky=W)
        Entry(textvariable=self.Banos, justify=RIGHT, width=8, bd=3).grid(row=2, column=1, sticky=W)
        Entry(textvariable=self.Area_const, justify=RIGHT, width=8, bd=3).grid(row=3, column=1, sticky=W)
        Entry(textvariable=self.Area_tot, justify=RIGHT, width=8, bd=3).grid(row=4, column=1, sticky=W)
        Entry(textvariable=self.Parking, justify=RIGHT, width=8, bd=3).grid(row=5, column=1, sticky=W)

    def Botones(self):
        Button(text='Buscar', width=10, bd=3, command=self.seek_house).grid(row=4, column=2)
        Button(text='Bins', width=10, bd=3, command=self.Binnes).grid(row=4, column=3)
        Button(text='Dashb', width=10, bd=3, command=self.Dashb).grid(row=4, column=4)
        Button(text='Describe UF', width=10, bd=3, command=self.Describe_UF).grid(row=6, column=2)
        Button(text='Describe USD', width=10, bd=3, command=self.Describe_USD).grid(row=6, column=3)
        Button(text='Salir', width=10, bd=3, command=self.Salir).grid(row=6, column=4)


    def seek_house(self):
        #entrenar datos de entrada
        x_values =df1[['Dorms','Baths','Built Area','Total Area','Parking']]
        y_values =df1[['Price_USD','Price_UF']]
        #crear obj
        lr = LinearRegression()
        #entrenar obj
        lr.fit(x_values, y_values)
        # A partir de aqui se crea un nuevo df con los datos de entrada por pantalla
        dormitorios = self.Dormitorios.get()
        banos = self.Banos.get()
        constr_area = self.Area_const.get()
        total_area = self.Area_tot.get()
        parking = self.Parking.get()
        valores = {'Dorms':[dormitorios],'Baths':[banos],'Built Area':[constr_area],'Total Area':[total_area],'Parking':[parking]}
        valores = pd.DataFrame(data=valores)
        #predecir o buscar segun valores de entrada
        Yhat = lr.predict(valores)
        convert1 = Yhat[0]
        precioUF = convert1[0]
        precioUSD = convert1[1]
        try:
            if precioUSD<0 or precioUF<0:
                mBox.showerror('Error','Valores negativos en los precios')
            else:
                self.ValorUF.set(f'{precioUF}')
                self.ValorUSD.set(f'{precioUSD}')
        except EOFError:
            exit()
        
    def Binnes(self):
        binnes = np.linspace(min(df1['Price_USD']), max(df1['Price_USD']), 4)
        agrupar = ['Bajo', 'Medio', 'Alto']
        binned = pd.cut(df1['Price_USD'], binnes, labels=agrupar, include_lowest=True).value_counts()
        binned.plot(kind='bar')
        mpl.title('Bins de los precios')
        mpl.ylabel('precio usd')
        mpl.show()

    def Describe_UF(self):
        describe_de_precios = df1['Price_UF'].describe().astype('int64')
        mBox.showinfo('Describe de UF', f'{describe_de_precios}')

    def Describe_USD(self):
        describe_usd = df1['Price_USD'].describe().astype('int64')
        mBox.showinfo('Describe de USD',f'{describe_usd}')

    def Dashb(self):
        from datas import dash2d

    def Salir(self):
        self.app.quit()
        self.app.destroy()

objeto = Ventana(Tk())
objeto.app.mainloop()