#!/usr/bin/env python
#
# Encriptación de contraseñas
#
# Diego Soto
# Feb/21/2024
# al22760575.AT.ite.dot.edu.dot.mx
#
import math
import numpy as np
import argparse
from libs.fun.common import unicodes, unificar

class Verificacion(object):
    def __init__(self, tipo_redondeo, **kwargs):
        self.tipo_redondeo = tipo_redondeo
        self.palabra = ''
        for key, value in kwargs.items():
            if key == "contrasenia":
                self.contrasenia = value[0].strip()
                palabra_ordenada = list(self.contrasenia)
                palabra_original = list(self.contrasenia)
                posicion = len(palabra_ordenada) - 1
                palabra_ordenada.insert(0, palabra_ordenada[posicion])
                palabra_ordenada.pop(-1)
                print(palabra_ordenada)
                suma1 = unicodes(palabra_original)
                suma2 = unicodes(palabra_ordenada)
                suma_total = unificar(suma1, suma2)
                self.semilla = suma_total
            if key == "redondeo":
                self.tipo_redondeo = value

class Encriptar(Verificacion): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.encriptar()


    @staticmethod
    def cambiardigitos(digitos): 
        decimales = [10, 11, 12, 13, 14, 15, 16, 17]
        hexadecimal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for c in range(9):
            if digitos == decimales[c - 1]:
                digitos = hexadecimal[c - 1]
        return digitos

    def decimalhexadecimal(self, decimal):
        hexadecimal = ""
        while decimal !=0:
            rem = self.cambiardigitos(decimal % 18)
            hexadecimal = str(rem) + hexadecimal
            decimal = int(decimal / 18)
        return hexadecimal 

        
    def encriptar(self):
        # Se genera una nueva instancia de rng (random number generator)
        rng = np.random.default_rng(self.semilla)
        # Se crean los valores aleatorios
        valores_aleatorios = rng.random(len(self.contrasenia))
        terminos = list(
            map(
                lambda x,y: int(round(x * ord(y), 0))
                if self.tipo_redondeo == 1 else math.floor(x * ord(y))
                if self.tipo_redondeo == 2 else math.ceil(x * ord(y)),
                valores_aleatorios, self.contrasenia
            )
        )
        print(terminos)
        for termino in terminos:
            self.palabra += self.decimalhexadecimal(termino)
    
    def __str__(self):
        return self.palabra



def main(**kwargs):
    #Tipo de redondeo por emplear
    tipo_redondeo = 2
    inicio = Encriptar(tipo_redondeo, **kwargs)
    print(inicio)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='simulacion8.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=""" 
            Encriptacion de contraseña. El usuario debe indicar la contraseña que desea ser
            encriptada como 
                                --palabra <texto>
        """,
        epilog="""
        Opcionalmente el usuario podrá indicar el tipo de redondeo por emplear
        1 redondeo estandar
        2 Redondeo tipo floor (default)
        3 redondeo tipo ceil
        """
    )
    parser.add_argument('-p', '--palabra',
                        dest="contrasenia", help="Contraseña por encriptar",
                        type=str, nargs=1, required=True)
    parser.add_argument('-o', '--opcion', default= 2, choices = [1, 2, 3],
                        dest="redondeo", help="Tipo de redondeo por emplear (default %(default)s)",
                        type=int, nargs='?', required=False)
    datos_entrada = {k: v for k, v in vars(parser.parse_args()).items() if v is not None}  # para crear un diccionario
    main(**datos_entrada)