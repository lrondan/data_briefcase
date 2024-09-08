import pandas as pd
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import matplotlib.pylab as mpl

conn = sqlite3.Connection('0.8 PornHub/app/data/base_world.sqlite')
df = pd.read_sql('SELECT * FROM actrices', conn)
Cursor = conn.cursor()

#por grid

class Ventana:
    def __init__(self, interfaz):
        self.gui = interfaz
        self.gui.title('PornHub models')
        self.gui.resizable(0,0)
        self.Lab()
        self.Bot()
        self.Sel()

    def Lab(self):
        Label(self.gui, text='Filtro de busqueda por categorias', font=BEVEL).grid(row=0, column=0, sticky=W)
        Label(self.gui, text='Visualizacion', font=BEVEL).grid(row=1, column=0, sticky=W)

    def Bot(self):
        Button(self.gui, text='VER', command=self.Funcion_ver, state='normal').grid(row=2,column=1, sticky=E)
        Button(self.gui, text='Salir', command=self.Salir, state='normal').grid(row=3,column=1, sticky=E)

    def Sel(self):
        self.seleccion = StringVar()
        self.numero = Combobox(self.gui, textvariable=self.seleccion, width=20, state='readonly', values=('pais', 'etnia', 'categoria')).grid(row=0, column=1)

    def Funcion_ver(self):
        if self.seleccion.get() == 'pais':
            category = df['country'].value_counts().nlargest(9)
            category.plot(kind='pie',
              title='Top 9 paises',
              colormap='RdBu',
              ylabel='category',
              legend=True)
            mpl.show()

        elif self.seleccion.get() == 'etnia':
            df_etnia = df['etnia'].value_counts()
            df_etnia.plot(kind='barh',
              title='Cantidad de actrices por etnia',
              xlabel='total',
              colormap='RdBu')
            mpl.show()

        elif self.seleccion.get() == 'categoria':
            category = df['category'].value_counts()
            category.plot(kind='pie',
              title='Cantidad de actrices por category',
              colormap='RdBu',
              ylabel='category',
              legend=True)
            mpl.show()
        else:
            pass

    def Salir(self):
        self.gui.quit()
        self.gui.destroy()

objeto = Ventana(Tk())
objeto.gui.mainloop()