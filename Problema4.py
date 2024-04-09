#!/usr/bin/env python
#
# Ordenamiento de preguntas de examen
# Diego Soto Flores
# Abril/03/2024
# al22760575.AT.ite.dot.edu.dot.mx
#

from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from datetime import date
from libs.classes.App import App
from libs.fun.common import unicode_nombre

class Problema4(App):
    def __init__(self, *args):
        super().__init__(*args)
        # Se inicializa la informacion
        #
        # Nombre completo del docente
        self.nombre = tk.StringVar()  # Estilo formal --> apellidoPaterno
        # Nombre de la materia
        self.materia = tk.StringVar()
        # Unidad de la materia
        self.unidad = tk.StringVar()
        # Cantidad de preguntas
        self.cantidad = tk.StringVar()
        # Orden de las preguntas del examen
        self.valores = tk.StringVar()
        # Crear widgets
        self.crear_widgets()

    def crear_widgets(self):
        # Se recolecta la informacion
        datos = Frame(self, bg='white', relief=SUNKEN)  # Sunken -> hundido
        datos.pack(fill=tk.X)
        (ttk.Label(datos, text="Nombre del docente: ", justify=LEFT, background="#C1E1C1").pack(
            anchor=tk.W,
            padx=10,
            pady=10,
            fill=tk.X))
        nombre = Entry(datos, textvariable=self.nombre, justify=LEFT)
        nombre.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        (ttk.Label(datos, text="Materia impartida: ", justify=LEFT, background="#C1E1C1").pack(
            anchor=tk.W,
            padx=10,
            pady=10,
            fill=tk.X))
        materia_impartida = Entry(datos, textvariable=self.materia, justify=LEFT)
        (materia_impartida.pack(
            anchor=tk.W,
            padx=10,
            pady=5,
            fill=tk.X))

        (ttk.Label(datos, text="Unidad de la materia: ", justify=LEFT, background="#C1E1C1")
         .pack(anchor=tk.W, padx=10, pady=10, fill=tk.X))
        unidad_materia = Entry(datos, textvariable=self.unidad, justify=LEFT)
        (unidad_materia.pack(
            anchor=tk.W,
            padx=10,
            pady=5,
            fill=tk.X))

        (ttk.Label(datos, text="Número de preguntas: ", justify=LEFT, background="#C1E1C1").pack(
            anchor=tk.W,
            padx=10,
            pady=10,
            fill=tk.X))
        numero_preguntas = Entry(datos, textvariable=self.cantidad, justify=LEFT)
        (numero_preguntas.pack(
            anchor=tk.W,
            padx=10,
            pady=5,
            fill=tk.X))
        
        (ttk.Button(datos,
                    text="Generar",
                    command=lambda: self.simula()).pack(
            side=tk.LEFT,
            padx=10,
            pady=5,
        ))
        (ttk.Button(datos,
                    text="Salir",
                    command=lambda: self.quit()).pack(
            side=tk.RIGHT,
            padx=10,
            pady=5,
        ))
        # Mostar los resultados
        resultados = Frame(self, relief=SUNKEN)
        resultados.pack(fill=tk.X)
        (ttk.Label(resultados, text="Ordenamiento de preguntas", justify=LEFT).pack(
            anchor=tk.W,
            fill=tk.X,
            padx=5,
            pady=5,
        ))
        vigencia = Entry(resultados, textvariable=self.valores)
        vigencia.pack(anchor=tk.W, padx=5, pady=5, fill=tk.X)
    
    def generadorAleatorios(self,n0, y, mod):
        self.preguntas = int(self.cantidad.get())
        x = [n0]
        for i in range(1, (self.preguntas * 5) + 1):
            temp = (y*x[i-1]) % mod
            x.append(temp)
        # Se elimina al elemento mayor
        max_a = x.index(max(x))
        x.pop(max_a)
        return x

    def preguntas_aleatorias(self):
        unidad = self.unidad.get()
        x0 = unicode_nombre(self.nombre.get())
        print(x0)
        y0 = unicode_nombre(self.materia.get())
        print(y0)
        z0 = int(ord(unidad)) * int(unidad)
        print(z0)
        # se generan los aleatorios
        x1 = self.generadorAleatorios(x0, 171, 30269)
        y1 = self.generadorAleatorios(y0, 172, 30307)
        z1 = self.generadorAleatorios(z0, 170, 30323)

        preguntas = []
        for i in range(1, len(x1)):
            u = ((x1[i-1]/30269 + y1[i-1]/30307 + z1[i-1]/30323) % 1)
            print(i-1)
            print(u)
            preguntas.append(u)
        print(preguntas)
        return preguntas
      
    def valores_intervalo(self):
        aletorios = self.preguntas_aleatorias()
        c = self.preguntas - 1
        valores_intervalo = list(map(lambda y: round(c * y + 1), aletorios))
        print(valores_intervalo)
        return valores_intervalo

    def simula(self):
        bandera = 0
        if not self.nombre.get():
            messagebox.showerror("Error de nombre",
                                 "Se debe indicar el nombre del maestro")
        else:
            texto = self.nombre.get().upper()
            self.nombre.set(texto)
            bandera +=1

        if not self.materia.get():
            messagebox.showerror("Error de materia",
                                 "Se debe indicar la materia impartida")
        else:
            texto = self.materia.get().upper()
            self.materia.set(texto)
            bandera += 1

        if not self.unidad.get():
            messagebox.showerror("Error de Unidad",
                                 "se debe especificar la unidad de materia")
        else:
            numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            texto = self.unidad.get()
            for char in texto:
                if char not in numeros:
                    messagebox.showerror("Error de Unidad",
                                         "Se debe representar la unidad con números enteros")
                    break
                else:
                    self.unidad.set(texto)
                    bandera += 1
        
        if not self.cantidad.get():
            messagebox.showerror("Error de No. preguntas",
                                 "Se debe de ingresar la cantidad de preguntas del examen")
        else:
            valor = self.cantidad.get()
            self.cantidad.set(valor)
        if bandera == 3:
            valores = self.valores_intervalo()
            valores_finales = []
            for j in valores:
                if j not in valores_finales:
                    valores_finales.append(j)
            print(valores_finales)
            self.valores.set(valores_finales)


if __name__ == '__main__':
    titulo = "Preguntas aleatorias"
    size = "320x400"
    app = Problema4(titulo, size)
    app.mainloop()