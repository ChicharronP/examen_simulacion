#!/usr/bin/env python
import csv
import datetime
import math

# Determina si un valor es positivo o no
def validar_dato(valor):
    return True if valor > 0 else False


# Determinar en caso de los decimales
def validar_decimales(valor):
    return True if valor >= 0 else False

def campos(campos, parametro):
    s = campos
    n = []
    for i in s:
        n.append(ord(i))
    suma_ord = sum(n)
    return suma_ord * parametro

def semilla(campo):
    s = campo
    n = []
    for i in s:
        n.append(ord(i))
    suma_ord = sum(n)
    return suma_ord

def producto_unicode(lista):
    suma = 0
    for caracter in lista:
        suma += int(ord(caracter)) * int(caracter)
    return suma

def unicodes(lista):
    suma = []
    for caracter in lista:
        suma.append(ord(caracter))
    return suma

def unicode_nombre(nombre):
    suma = 0
    for char in nombre:
        suma += ord(char)
    return suma

def unificar(arreglo1, arreglo2):
    producto = []
    for valor in range(len(arreglo1)):
        producto.append(arreglo1[valor] * arreglo2[valor])
    suma = 0
    for valor in producto:
        suma += valor
    return suma

# Archivo para calificaciones
def crear_archivo(*args, **kwargs):
    valores, = args
    nombre_archivo = "Simulacion.csv" if kwargs.get("archivo") is None else kwargs["archivo"]
    header = ['No', 'aleatorios'] if kwargs.get("Encabezado") is None else kwargs["Encabezado"]
    bandera = 0 if kwargs.get("bandera") is None else kwargs["bandera"]
    ingresos = None if kwargs.get("ingresos") is None else kwargs["ingresos"]
    costos = None if kwargs.get("costos") is None else kwargs["costos"]
    data = [] # Arreglo donde estará la información que se manda al archivo
    datos = []  # Arreglo donde estara la informacion que se manda al archivo
    header = header
    for i in range(len(valores)):
        if bandera == 1: 
            ahora = datetime.datetime.now()
            temp = ahora.microsecond
            valor = 0 if round(round(math.log(temp) + (temp % 7 + i), 3) % 5, 0) == 0 else valores[i]
            datos.append([i+1, valor])
        elif bandera == 2:
            datos.append([i + 1, ingresos[i], costos[i], valores[i]])
        else:
            datos.append([i + 1, valores[i]])
    with open(nombre_archivo, 'w', encoding='utf-8', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(header)
        writer.writerows(datos)
    print('El archivo ha sido creado satisfactoriamente')

