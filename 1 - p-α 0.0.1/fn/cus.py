from tkinter import *
from tkinter import ttk
import numpy as np
import random
import pickle
import os
import time





def leer_usuario(lista_usuario, donde = 'user'):
        fichero_usuario = open(donde,'rb')
        lista_usuario = pickle.load(fichero_usuario)
        return lista_usuario
    
def crear_usuario(lista_usuario, donde = 'user'):
        fichero_usuario = open(donde,"wb")
        nombre =   str(input('Nombre: '))
        apellido = str(input('Apellido: '))
        correo =   str(input('Correo: '))
        lista_usuario.append(nombre.capitalize())
        lista_usuario.append(apellido.capitalize())
        lista_usuario.append(correo)
        pickle.dump(lista_usuario, fichero_usuario)
        fichero_usuario.close()
        del(fichero_usuario)

def GUI_crear_usuario(lista_usuario, ICONO = '', donde = 'user'):

    def get_datos():
        fichero_usuario = open(donde,"wb")
        nombre = E_Nombre.get()
        apellido = E_Apellido.get()
        correo = E_Correo.get()
        lista_usuario.append(nombre.capitalize())
        lista_usuario.append(apellido.capitalize())
        lista_usuario.append(correo)
        pickle.dump(lista_usuario, fichero_usuario)

        fichero_usuario.close()
        del(fichero_usuario)
        time.sleep(0.5)
        root.destroy()

    def limpiar_campos():
        pass

    root = Tk()
    root.iconbitmap(ICONO)
    root.title('Registro')
    root.resizable(0,0)

    frame_registro = Frame(root)
    frame_registro.grid(row = 0, column = 0, padx = 10, pady = 10)

    L_Nombre = Label(frame_registro, text = 'Nombre', font = ('Arial',13))
    L_Nombre.grid(row = 1, column = 1, padx = 5, pady = 5)
    L_Apellido = Label(frame_registro, text = 'Apellido', font = ('Arial',13))
    L_Apellido.grid(row = 2, column = 1, padx = 5, pady = 5)
    L_Correo = Label(frame_registro, text = 'Correo', font = ('Arial',13))
    L_Correo.grid(row = 3, column = 1, padx = 5, pady = 5)

    E_Nombre = Entry(frame_registro, justify = CENTER, font = ('Arial',13))
    E_Nombre.grid(row = 1, column = 2, padx = 5, pady = 5)
    E_Apellido = Entry(frame_registro, justify = CENTER, font = ('Arial',13))
    E_Apellido.grid(row = 2, column = 2, padx = 5, pady = 5)
    E_Correo = Entry(frame_registro, justify = CENTER, font = ('Arial',13))
    E_Correo.grid(row = 3, column = 2, padx = 5, pady = 5)

    frame_Botones = Frame(root)
    frame_Botones.grid(row = 2, column = 0, padx = 10, pady = 10)

    styleb1  = ttk.Style()
    styleb1.configure('B1.TButton', background   ="#7FBA00", font = ('Arial',13))
    styleb2  = ttk.Style()
    styleb2.configure('B2.TButton', background   ="#F25022", cursor = 'hand1', font = ('Arial',13))

    Boton_Aceptar = ttk.Button(frame_Botones, text = 'Aceptar',style='B1.TButton', cursor = 'hand2', command = get_datos)
    Boton_Limpiar = ttk.Button(frame_Botones, text = 'Limpiar campos',style='B2.TButton', cursor = 'hand2', command = limpiar_campos)
    Boton_Aceptar.grid(row = 1, column = 1, padx = 5, pady = 5)
    Boton_Limpiar.grid(row = 1, column = 2, padx = 5, pady = 5)

    mainloop()

