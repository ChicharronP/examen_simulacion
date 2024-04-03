#!/usr/bin/env python
#
# Creacion de tarjetas de credito
# Diego Soto Flores
# Mar/06/2024
# al22760575.AT.ite.dot.edu.dot.mx
#



import locale
import calendar
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import random
from datetime import date
from libs.classes.App import App


class Simulacion9(App):
    def __init__(self, *args):
        super().__init__(*args)
        # Se inicializa la informacion
        #
        # Apellido paterno
        self.appat = tk.StringVar()  # Estilo formal --> apellidoPaterno
        # Apellido materno
        self.apmat = tk.StringVar()
        # Nombre
        self.nombre = tk.StringVar()
        # Vigencia de la tarjeta
        self.vigencia = tk.StringVar()
        # CVV
        self.cvv = tk.StringVar()
        # Num Tarjeta
        self.tarjeta = tk.StringVar()
        # Comienza el codigo
        # Crear widgets
        self.crear_widgets()

    def crear_widgets(self):
        # Se recolecta la informacion
        datos = Frame(self, bg='white', relief=SUNKEN)  # Sunken -> hundido
        datos.pack(fill=tk.X)
        (ttk.Label(datos, text="Nombre: ", justify=LEFT, background="#C1E1C1").pack(
            anchor=tk.W,
            padx=10,
            pady=10,
            fill=tk.X))
        nombre = Entry(datos, textvariable=self.nombre, justify=LEFT)
        nombre.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        (ttk.Label(datos, text="Primer Apellido: ", justify=LEFT, background="#C1E1C1").pack(
            anchor=tk.W,
            padx=10,
            pady=10,
            fill=tk.X))
        apellido_paterno = Entry(datos, textvariable=self.appat, justify=LEFT)
        (apellido_paterno.pack(
            anchor=tk.W,
            padx=10,
            pady=5,
            fill=tk.X))

        (ttk.Label(datos, text="Segundo Apellido: ", justify=LEFT, background="#C1E1C1")
         .pack(anchor=tk.W, padx=10, pady=10, fill=tk.X))
        apellido_materno = Entry(datos, textvariable=self.apmat, justify=LEFT)
        (apellido_materno.pack(
            anchor=tk.W,
            padx=10,
            pady=5,
            fill=tk.X))
        (ttk.Button(datos,
                    text="Crear cuenta",
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
        (ttk.Label(resultados, text="Fecha de Vigencia", justify=LEFT).pack(
            anchor=tk.W,
            fill=tk.X,
            padx=5,
            pady=5,
        ))
        vigencia = Entry(resultados, textvariable=self.vigencia)
        vigencia.pack(anchor=tk.W, padx=5, pady=5, fill=tk.X)

        (ttk.Label(resultados, text="CVV", justify=LEFT).pack(
            anchor=tk.W,
            fill=tk.X,
            padx=5,
            pady=5,
        ))
        cvv = Entry(resultados, textvariable=self.cvv)
        cvv.pack(anchor=tk.W, padx=5, pady=5, fill=tk.X)

        (ttk.Label(resultados, text="Tarjeta", justify=LEFT).pack(
            anchor=tk.W,
            fill=tk.X,
            padx=5,
            pady=5,
        ))
        tarjeta = Entry(resultados, textvariable=self.tarjeta)
        tarjeta.pack(anchor=tk.W, padx=5, pady=5, fill=tk.X)


    def contabilizar(self):
        suma = 0
        vocales = ('A', 'Á', 'À', 'E', 'É', 'È',
                 'I', 'Í', 'Ì', 'O', 'Ó', 'Ò',
                 'U', 'Ú', 'Ù')
        nombre_persona = self.nombre.get() + self.appat.get() + self.apmat.get()
        for caracter in nombre_persona:
            if caracter in vocales:
                suma += ord(caracter)
        return suma 
    

    def vigencia_tarjeta(self):
        """meses_anio = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                      'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        meses_numericos = [i for i in range (1,13)]
        meses = list(zip(meses_numericos, meses_anio))"""
        locale.setlocale(locale.LC_ALL, ("es_MX", "UTF-8"))
        meses = list(calendar.month_name)
        mes_vigencia = random.randint(1,12)
        mes = meses[mes_vigencia].upper()
        # Fecha de vigencia
        hoy = date.today()
        anio_vigencia = hoy.year + 3
        vigencia = mes + '/' + str(anio_vigencia)
        self.vigencia.set(vigencia)
        return mes_vigencia, anio_vigencia
        
    @staticmethod
    def campos_tarjeta(semilla):
        parametro_t = 1619684
        bandera = -1
        modulo = 2 ** 31
        parametro_a = 8 * parametro_t + (bandera * 3)
        x = [semilla]
        for i in range (1, 10):
            temp = (parametro_a * x[i-1]) % modulo
            x.append(temp)
        for j in range(len(x)):
            # convertir a string
            dato = str(x[j])
            # Obtener los cuatro primeros caracteres
            x[j] = dato[:4]
        return x
    

    def crear_tarjeta(self):
        suma_vocales = self.contabilizar()
        mes, anio = self.vigencia_tarjeta()
        valor_total = suma_vocales * mes * anio
        valor_temporal = str(valor_total)
        codigo_validacion = valor_temporal[-3:]
        cv1 = int(codigo_validacion)
        campo1 = '5' + valor_temporal[:3]
        valores_tarjeta = self.campos_tarjeta(cv1)
        codigo_temporal = valor_temporal[:3]
        digito2 = int(codigo_temporal[0])
        digito3 = int(codigo_temporal[1])
        digito4 = int(codigo_temporal[2])
        campo2 = valores_tarjeta[digito2] if len(valores_tarjeta[digito2]) == 4 else valores_tarjeta[digito2] + '0' 
        campo3 = valores_tarjeta[digito3] if len(valores_tarjeta[digito3]) == 4 else valores_tarjeta[digito3] + '0' 
        campo4 = valores_tarjeta[digito4] if len(valores_tarjeta[digito4]) == 4 else valores_tarjeta[digito4] + '0' 
        tarjeta = campo1 + '-' + campo2 + '-' + campo3 + '-' + campo4
        # Mostrar resultados
        self.cvv.set(codigo_validacion)
        self.tarjeta.set(tarjeta)
        

    def simula(self):
        bandera = 0
        if not self.nombre.get():
            messagebox.showerror("Error de nombre",
                                 "Se debe indicar el nombre de cliente")
        else:
            texto = self.nombre.get().upper()
            self.nombre.set(texto)
            bandera +=1

        if not self.appat.get():
            messagebox.showerror("Error de apellido",
                                 "Se debe indicar el primer apellido de cliente")
        else:
            texto = self.appat.get().upper()
            self.appat.set(texto)
            bandera += 1

        if not self.apmat.get():
            texto = 'X'
            self.apmat.set(texto)
        else:
            texto = self.apmat.get().upper()
            self.apmat.set(texto)
        if bandera == 2:
            self.crear_tarjeta()


if __name__ == '__main__':
    titulo = "tarjeta de credito"
    size = "270x490"
    app = Simulacion9(titulo, size)
    app.mainloop()