import os
import pandas as pd 
import numpy as np
from PIL import Image
import pickle
import time as t 

#creando carpetas
try:
    os.makedirs("file")
except:
    print("F1C")

#   #   Clases

class tiempo():
    dias_inglés =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    def fecha_de_hoy(self):
        fecha_tupla = t.localtime()
        fecha_str = t.strftime('%d-%m-%Y', fecha_tupla)
        return fecha_str

    def día_de_hoy(self):
        dias_inglés = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        #para saber si existe >>'Monday' in dias_inglés   -> devuelve true
        fecha_tupla = t.localtime()
        fecha_str = t.strftime('%A', fecha_tupla)
        #para buscar el índice 
        indice = dias_inglés.index(fecha_str)
        return dias[indice]

    def solo_dia(self):
        fecha_tupla = t.localtime()
        solo_dia = t.strftime('%d', fecha_tupla)
        return solo_dia
    
    def solo_mes(self):
        fecha_tupla = t.localtime()
        solo_mes = t.strftime('%m', fecha_tupla)
        return solo_mes
    
    def solo_año(self):
        fecha_tupla = t.localtime()
        solo_año = t.strftime('%Y', fecha_tupla)
        return solo_año



class base_datos():
    def base_de_datos(self, Nombre, Diccionario):
        self.Nombre = Nombre
        self.Diccionario = Diccionario
        df = pd.DataFrame(Diccionario)
        df.to_csv(f'{Nombre}.csv', index = False)

    def Anadir_datos(self, nombre, lista_agregar):
        self.nombre = nombre
        self.lista_agregar = lista_agregar
        df = pd.read_csv(f'{nombre}.csv')
        df.loc[len(df)+1] = lista_agregar
        df.to_csv(f'{nombre}.csv', index=False)
    
    def ordenar_bdd(self, nombre, parametro, acendente = False):
        data = pd.read_csv(f'{nombre}.csv')
        data = data.sort_values(by = parametro, ascending = acendente)
        data.to_csv(f'{nombre}.csv', index = False)
        data = pd.read_csv(f'{nombre}.csv')
        print(data)


#   #   Funciones







