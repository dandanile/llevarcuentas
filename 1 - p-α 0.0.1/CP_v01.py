from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as TkFont
import os
import time
from PIL import Image
import pandas as pd
import csv



import fn.cus as cus
import fn.fun as fun

#   Funciones

#   Definiciones
tiempo = fun.tiempo()
#   Cromprobar archivos

lista_usuario = []
try:
    lista_usuario = cus.leer_usuario(lista_usuario, donde = 'file/user')
except:
    cus.GUI_crear_usuario(lista_usuario, donde = 'file/user', ICONO = 'ico')
    lista_usuario = cus.leer_usuario(lista_usuario, donde = 'file/user')

BasData = fun.base_datos()

nombre_bbdd_ingresos = 'ins'
bbdd_ingresos = {
    'Fecha':[],
    'Monto':[],
    'Nota':[]
}

nombre_bbdd_gastos = 'gas'
bbdd_gastos = bbdd_ingresos


if nombre_bbdd_ingresos+'.csv' in os.listdir('file'):
    print(f'ddbb {nombre_bbdd_ingresos} existente previamente')
else:
    BasData.base_de_datos('file/' + nombre_bbdd_ingresos,bbdd_ingresos)
    print(f'ddbb {nombre_bbdd_ingresos} creada con exito')

if nombre_bbdd_gastos+'.csv' in os.listdir('file'):
    print(f'ddbb {nombre_bbdd_gastos} existente previamente')
else:
    BasData.base_de_datos('file/' + nombre_bbdd_gastos,bbdd_gastos)
    print(f'ddbb {nombre_bbdd_gastos} creada con exito')




#   Gui

##  Nombre y mas
root = Tk()
root.title(f'MisCuentas - {lista_usuario[0]}')
root.iconbitmap('ico')

##  Menú

##  Presentacion
Zona_Presentacion = Frame(root)
Zona_Presentacion.grid(row = 0, column = 0, padx = 20, pady = 5, sticky = W)

saludo = Label(Zona_Presentacion , text = f'Hola {lista_usuario[0]}!')
saludo.config( font = ('Arial Rounded MT Bold', 12, UNDERLINE))
Fecha1 = Label(Zona_Presentacion , text = tiempo.día_de_hoy())
Fecha1.config( font = ('Arial Rounded MT Bold', 10))
Fecha2 = Label(Zona_Presentacion , text = tiempo.fecha_de_hoy())
saludo.grid( row = 0, column = 0, sticky = W)
Fecha1.grid( row = 1, column = 0, sticky = W)
Fecha2.grid( row = 2, column = 0, sticky = W)

##  Entrada de datos
def com_BT_aceptar_Agregar():
    opcion = int(Ingreso.get())
    dia = variable_dia.get().zfill(2) #esto es para que se cargue como 02 y no como 2
    mes = variable_mes.get().zfill(2)
    ano = variable_Ano.get()
    monto = Entrada_monto.get()
    nota = Entrada_nota.get('1.0', END)
    
    try:
        a1 = type(int(Entrada_monto.get())) is int
    except:
        a1 = False

    a2 = True
    if (Entrada_monto.get() == ''):
        a2 = False

    try:
        a3 = int(variable_dia.get()) in range(1,31)
    except:
        a3 = False
    try:
        a4 = int(variable_mes.get()) in range(1,12)
    except:
        a4 = False

    a5 = True
    rango = range( int(tiempo.solo_año()) - 2 , int(tiempo.solo_año()) + 2)
    try:
        if int(variable_Ano.get()) in rango:
            
            a5 = True
    except:
        a5 = False

    lista_valores = [a1, a2, a3, a4, a5]

    if all(lista_valores):
        milista = [ano+"-"+mes+"-"+dia,int(monto),nota[:len(nota)-1].lower()]
        if opcion == 1:
            BasData.Anadir_datos('file/' + nombre_bbdd_ingresos, milista)
            com_BT_borrar_Abrebar()
            messagebox.showinfo(message="Carga completa", title="Felicidades")
            print('  Base de datos: ingresos\n_________________________')
            BasData.ordenar_bdd('file/' + nombre_bbdd_ingresos, 'Fecha')
        else:
            BasData.Anadir_datos('file/' + nombre_bbdd_gastos, milista)
            com_BT_borrar_Abrebar()
            messagebox.showinfo(message="Carga completa", title="Felicidades")
            print('  Base de datos: gastos\n_______________________')
            BasData.ordenar_bdd('file/' + nombre_bbdd_gastos, 'Fecha')

    else:
        messagebox.askretrycancel(message="Por favor, revise que los datos esten bien escritos.", title="Ha ocurrido un error!")
        
    
    
def com_BT_borrar_Abrebar():
    Entrada_nota.delete('1.0', END) #brra todo lo del text
    Entrada_monto.delete(0, END)

Zona_agregar = LabelFrame(root, text = 'Agregar') #     cambiar este root
Zona_agregar.grid(row = 1, column = 0, padx = 5, pady = 5)

Ingreso = StringVar() 
RB_Ingr = Radiobutton(Zona_agregar, text = 'Ingreso', variable = Ingreso, value = 1, justify = 'left')
RB_Ingr.select()
RB_Gast = Radiobutton(Zona_agregar, text = 'Gasto', variable = Ingreso, value = 2)
RB_Gast.deselect()

RB_Ingr.grid(row = 1, column = 0, sticky = W)
RB_Gast.grid(row = 2, column = 0, sticky = W)


lista_dias = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
lista_meses = [1,2,3,4,5,6,7,8,9,10,11,12]
Ano =int(tiempo.solo_año())
lista_años =[Ano-2, Ano-1, Ano, Ano+1, Ano+2]
variable_dia = StringVar()
combo_dia = ttk.Combobox(Zona_agregar, textvariable = variable_dia,  values = lista_dias, width=5, font = 'Arial 12')
combo_dia.set(int(tiempo.solo_dia()))
variable_mes = StringVar()
combo_mes = ttk.Combobox(Zona_agregar, textvariable = variable_mes,  values = lista_meses, width=5, font = 'Arial 12')
combo_mes.set(int(tiempo.solo_mes()))
variable_Ano = StringVar()
combo_Ano = ttk.Combobox(Zona_agregar, textvariable = variable_Ano,  values = lista_años, width=5, font = 'Arial 12')
combo_Ano.set(Ano)

texto_fecha = Label(Zona_agregar, text = '  Seleccione la fecha')
combo_dia.grid(row = 4, column = 0, padx = 5, pady = 2)
combo_mes.grid(row = 4, column = 1, padx = 5, pady = 2)
combo_Ano.grid(row = 4, column = 2, padx = 5, pady = 2)
texto_fecha.grid(row = 3, column = 0, columnspan = 2, sticky = W)

texto_monto = Label(Zona_agregar, text = '  Ingrese el monto')
Entrada_monto = ttk.Entry(Zona_agregar, justify = CENTER)


texto_monto.grid(row = 5, column = 0, columnspan = 2, sticky = W)
Entrada_monto.grid(row = 6, column = 0, columnspan = 3)


texto_nota = Label(Zona_agregar, text = '  Notas:')

Entrada_nota = Text(Zona_agregar)
Entrada_nota.config(
    width=20,
    height=2.5,
    font=("Arial",12),
    highlightthickness = 1,
    relief = FLAT, #FLAT, RAISED, SUNKEN, GROOVE, RIDGE
    highlightbackground = "#737373", #color normal del nuevo borde
    selectbackground = '#737373', #color del texto al seleccionarlo
    highlightcolor = '#4285f4', #color cuando seleccioanmos el cuadro texto
    insertbackground = 'black',
    wrap=WORD #para que no se corten las palabras
    )

texto_nota.grid(row = 7, column = 0, columnspan = 2, sticky = W)
Entrada_nota.grid(row = 8, column = 0, columnspan = 3,padx=5, pady = 5)

Frame_Botones_Agregar_datos = Frame(Zona_agregar)
Frame_Botones_Agregar_datos.grid(row = 9, column = 0, columnspan = 3,padx=5, pady = 5)

BT_aceptar_Agregar = ttk.Button(Frame_Botones_Agregar_datos, text = 'Agregar', command = com_BT_aceptar_Agregar)
BT_borrar_Abrebar = ttk.Button(Frame_Botones_Agregar_datos, text = 'Borrar', command = com_BT_borrar_Abrebar)

BT_aceptar_Agregar.grid(row = 0, column = 0, padx=5, pady = 5)
BT_borrar_Abrebar .grid(row = 0, column = 1, padx=5, pady = 5)


##  FIN
mainloop()
