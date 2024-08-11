from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mBox

class Ventana:
    def __init__(self, interfaz) -> None:
        self.app = interfaz
        self.app.geometry('500x200')
        self.app.title('Hosting')
        self.app.resizable(0,0)
        self.app.config(bg='gray')
        self.Labels()
        self.Entradas()
        self.Botones()

    def Labels(self):
        Label(text='Valores en USD', justify=CENTER, font='BOLD',width=12).grid(row=0, column=0)
        Label(text='Dormitorios: ', justify=RIGHT, font='BOLD',width=12).grid(row=1, column=0, sticky=W)
        Label(text='Baños: ', justify=RIGHT, font='BOLD',width=12).grid(row=2, column=0, sticky=W)
        Label(text='Area constr: ', justify=RIGHT, font='BOLD',width=12).grid(row=3, column=0, sticky=W)
        Label(text='Area total: ', justify=RIGHT, font='BOLD',width=12).grid(row=4, column=0, sticky=W)
        Label(text='Parking:', justify=RIGHT, font='BOLD',width=12).grid(row=5, column=0, sticky=W)


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
        Button(text='OK', width=8, bd=3, command=self.seek_house).grid(row=6, column=1)

    def seek_house(self):
        pass

objeto = Ventana(Tk())
objeto.app.mainloop()