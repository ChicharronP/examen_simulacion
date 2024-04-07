#!/usr/bin/env python
#
# Primer generador de pseudo aleatorios
#
# Diego Soto
# Marzo/19/2024
# al22760563.AT.ite.dot.edu.dot.mx
#
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from libs.classes.App import App
from libs.fun.common import producto_unicode

class Simulacion9(App):
    def __init__(self, *args):
        super().__init__(*args)
        # Se inicializa la informacion
        #
        # Fecha de nacimiento
        self.fecha = tk.StringVar()  # Estilo formal --> apellidoPaterno
        # correo electronico
        self.correo = tk.StringVar()
        # celular
        self.celular = tk.StringVar()
        #monto solicitado
        self.monto = tk.StringVar()
        # Num Tarjeta
        self.tarjeta = tk.StringVar()
        # Comienza el codigo
        # Crear widgets
        self.crear_widgets()

    def crear_widgets(self):
        # Se recolecta la informacion
        # Fecha de nacimiento
        datos = Frame(self, bg='white', relief=SUNKEN)  # Sunken -> hundido
        datos.pack(fill=tk.X)
        (ttk.Label(datos, text="Fecha de nacimiento (dd/mm/aaaa):",
                  justify=LEFT, background="#C1E1C1").
                  pack(anchor=tk.W,
                       padx=10,
                       pady=10,
                       fill=tk.X))
        nombre = Entry(datos, textvariable=self.fecha, justify=LEFT)
        nombre.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        # Correo electronico
        (ttk.Label(datos, text="Correo electrónico: ", justify=LEFT, background="#C1E1C1").pack(
            anchor=tk.W,
            padx=10,
            pady=10,
            fill=tk.X))
        apellido_paterno = Entry(datos, textvariable=self.correo, justify=LEFT)
        (apellido_paterno.pack(
            anchor=tk.W,
            padx=10,
            pady=5,
            fill=tk.X))

        # Correo electronico
        (ttk.Label(datos, text="Número de celular: ", justify=LEFT, background="#C1E1C1")
         .pack(anchor=tk.W, padx=10, pady=10, fill=tk.X))
        apellido_materno = Entry(datos, textvariable=self.celular, justify=LEFT)
        (apellido_materno.pack(
            anchor=tk.W,
            padx=10,
            pady=5,
            fill=tk.X))

        # Monto Solicitado
        (ttk.Label(datos, text="Monto solicitado: ", justify=LEFT, background="#C1E1C1")
         .pack(anchor=tk.W, padx=10, pady=10, fill=tk.X))
        apellido_materno = Entry(datos, textvariable=self.monto, justify=LEFT)
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

        (ttk.Label(resultados, text="Tarjeta", justify=LEFT).pack(
            anchor=tk.W,
            fill=tk.X,
            padx=5,
            pady=5,
        ))
        tarjeta = Entry(resultados, textvariable=self.tarjeta)
        tarjeta.pack(anchor=tk.W, padx=5, pady=5, fill=tk.X)

    def contabilizar(self):
        fecha = self.fecha.get()
        dd, mm, aaaa = map(int, fecha.split('/'))
        suma = dd + mm + aaaa
        return suma
        
    def correo_usuarios(self):
       consonantes = ('b', 'c', 'd', 'f', 'g', 'h',
                      'j', 'k', 'l', 'm', 'n', 'p',
                      'q', 'r', 's', 't', 'v', 'w', 
                      'x', 'y', 'z', '1', '2', '3', 
                      '4', '5', '6', '7', '8', '9')
       vocales = ('a', 'e', 'i', 'o', 'u')

       correo = self.correo.get()
       correo_usuario = list(correo)
       usuario = []
       # se consiguen los caracteres antes del arroba
       for caracter in correo_usuario:
           if caracter == '@':
               break
           usuario.append(caracter)
        # Se consiguen los valores despues del arroba
       dominio = []
       indice_arroba = correo_usuario.index('@')
       for caracter in correo_usuario[indice_arroba + 1:]:
           dominio.append(caracter)
       # Se suma los valores unicode de las consonantes
       suma1 = 0
       for caracter in usuario:
           if caracter in consonantes:
               suma1 += int(ord(caracter))
       # Se suman los valores unicode de las vocales
       suma2 = 0
       for caracter in dominio:
           if caracter in vocales:
               suma2 += int(ord(caracter))
       # Suma de todos los valores del correo
       mod = len(correo_usuario)
       # Multiplicación del usuario  y dominio
       usr_dom = suma1 * suma2
       return usr_dom % mod
    
    def numero_celular(self):
        celular = [self.celular.get()]
        nuevo = []
        # Elimicacion de simbolos
        for cadena in celular:
            nueva_cadena = ''.join(caracter for caracter in cadena if caracter not in '()-')
            nuevo.append(nueva_cadena)
        # Número sin simbolos
        nuevo1 = nuevo[0]
        numero = list(nuevo1)
        # Multiplicacion del digito por su valor unicode
        suma3 = producto_unicode(numero)
        return suma3

    def monto_solicitado(self):
        monto = self.monto.get()
        monto_lista = list(monto)
        # Se consiguen los digitos enteros
        enteros = []
        for digito in monto_lista:
            if digito == ".":
                break
            enteros.append(digito)
        # Se consiguen los centavos
        centavos = []
        indice_arroba = monto_lista.index('.')
        for caracter in monto_lista[indice_arroba + 1:]:
            centavos.append(caracter)
        # Suma de los enteras
        suma = producto_unicode(enteros)
        # suma de los centavos
        suma1 = producto_unicode(centavos)
        return suma + suma1

    @staticmethod    
    def campos_tarjeta(semilla):
        parametro_a = 1619487
        parametro_b = 3619451
        modulo = 2 ** 31
        x = [semilla]
        for i in range(1,10):
            temp = (parametro_a * x[i-1] + parametro_b) % modulo
            x.append(temp)
        for j in range(len(x)):
            dato = str(x[j])
            x[j] = dato[:4]
        return x

    def crear_tarjeta(self):
        semilla = self.contabilizar() + self.correo_usuarios() + self.numero_celular() + self.monto_solicitado()
        print(semilla)
        valor_temporal = str(semilla)
        codigo_validacion = valor_temporal[-3:]
        cv1 = int(codigo_validacion)
        campo1 = '4' + valor_temporal[:3]
        valores_tarjeta = self.campos_tarjeta(cv1)
        codigo_temporal = valor_temporal[-3:]
        digito2 = int(codigo_temporal[0])
        digito3 = int(codigo_temporal[1])
        digito4 = int(codigo_temporal[2])
        campo2 = valores_tarjeta[digito2] if len(valores_tarjeta[digito2]) == 4 else valores_tarjeta[digito2] + '0'
        campo3 = valores_tarjeta[digito3] if len(valores_tarjeta[digito3]) == 4 else valores_tarjeta[digito3] + '0'
        campo4 = valores_tarjeta[digito4] if len(valores_tarjeta[digito4]) == 4 else valores_tarjeta[digito4] + '0'
        tarjeta = campo1 + '-' + campo2 + '-' + campo3 + '-' + campo4
        # Mostrar resultados
        self.tarjeta.set(tarjeta)

    def simula(self):
        valores = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        bandera = 0
        if not self.fecha.get():
            messagebox.showerror("Error de fecha",
                                 "Se debe de ingresar una fecha")
        else:
            bandera += 1

        if not self.correo.get():
            messagebox.showerror("Error de Correo",
                                 "Se debe de ingresar un correo electronico")
        else:
            if "@" and "." not in self.correo.get():
                messagebox.showerror("Error de correo",
                                     "Ingrese correo de manera correcta "'usuario@dominio.extension'"")
            else:
                texto = self.correo.get().lower()
                self.correo.set(texto)
                bandera += 1

        if not self.celular.get():
            messagebox.showerror("Error de celular", 
                                 "Se debe de ingresar un número de telefonico")
        else:
            bandera += 1
        
        if not self.monto.get():
            messagebox.showerror("Error de monto", 
                                 "Se debe de ingresar un monto")
        else:
            bandera += 1
        if bandera == 4:
            self.crear_tarjeta()


if __name__ == '__main__':
    titulo = "Numero de tarjeta"
    size = "270x530"
    app = Simulacion9(titulo, size)
    app.mainloop()