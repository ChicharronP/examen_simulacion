#!/usr/bin/env python
#
# Primer generador de pseudo aleatorios
#
# Diego Soto
# Marzo/19/2024
# al22760563.AT.ite.dot.edu.dot.mx
#
import csv
import argparse
import sys
from enum import Enum
from libs.fun.common import crear_archivo
from libs.fun.common import campos, semilla


# mensajes de error del programa
class Errores(Enum):
    PARAMETROA = "El parametro A debe ser de al menos 5 digitos"
    PARAMETROB = "El parametro B debe ser de al menos 5 digitos "
    TAMANIO = "La longitud del campo debe de ser al menos 5 caracteres"


class Aleatorios(object):
    def __init__(self, parametro_a, parametro_b, modulo, campo1, campo2, campo3, **kwargs):
        self.parametro_a = parametro_a
        self.parametro_b = parametro_b
        self.modulo = modulo
        self.campo1 = campo1
        self.campo2 = campo2
        self.campo3 = campo3
        for key, value in kwargs.items():
            if key == 'a':
                try:
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores.PARAMETROA.value)
                    sys.exit()
                self.parametro_a = value
            if key == 'b':
                try:
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores.PARAMETROB.value)
                    sys.exit()
                self.parametro_b = value
            if key == 'c':
                try:
                    assert (self.validar_tamanio(value))
                except AssertionError:
                    print(Errores.TAMANIO.value)
                    sys.exit()
                self.campo1 = value
            if key == 'd':
                try:
                    assert (self.validar_tamanio(value))
                except AssertionError:
                    print(Errores.TAMANIO.value)
                    sys.exit()
                self.campo2 = value
            if key == 'e':
                try:
                    assert (self.validar_tamanio(value))
                except AssertionError:
                    print(Errores.TAMANIO.value)
                    sys.exit()
                self.campo3 = value

    @staticmethod
    def validar_dato(valor):
        return True if valor >= 10000 else False

    @staticmethod
    def validar_tamanio(valor):
        return True if len(valor) <= 5 else False


class GenerarAleatorios(Aleatorios):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def generar_claves(self):
        nuevo1 = self.campo1.upper()
        nuevo2 = self.campo2.upper()
        nuevo3 = self.campo3.upper()

        # Es el nuevo parametro A
        nuevo_c = campos(nuevo1, self.parametro_a)
        # Es es nuevo parametro B
        nuevo_d = campos(nuevo2, self.parametro_b)
        # Es la semilla
        nuevo_e = semilla(nuevo3)

        # Se inicializa el arreglo
        pseudoAleatorios = [nuevo_e]
        for i in range(1, 10):
            temp = (nuevo_c * pseudoAleatorios[i-1] + nuevo_d) % self.modulo
            pseudoAleatorios.append(temp)
        pseudoAleatorios.pop(0)
        crear_archivo(pseudoAleatorios)
        return pseudoAleatorios

    def primer_campo(self):
        claves = self.generar_claves()

        primeros_valores = []
        for elemento in claves:
            clave_str = str(elemento)
            primeros_valores.append(clave_str[:2])

        campo1_final = []
        for elemento in primeros_valores:
            primer_digito = int(elemento)
            if primer_digito % 2 == 0:
                campo1_final.append(str(primer_digito)[0])
            else:
                suma_digitos = sum(int(digito) for digito in elemento)
                consonante_unicode = chr(suma_digitos + ord('`'))
                campo1_final.append(consonante_unicode)

        # Unir los resultados en una sola cadena
        return ''.join(campo1_final).upper()

    def ultimo_campo(self):
        claves = self.generar_claves()
        ultimos_valores = []

        for elemento in claves:
            clave_str = str(elemento)
            ultimos_valores.append(clave_str[-2:])
        campo2_final = []
        for elemento in ultimos_valores:
            primer_digito = int(elemento)
            if primer_digito % 2 == 0:
                campo2_final.append(str(primer_digito)[0])
            else:
                suma_digitos = sum(int(digito) for digito in elemento)
                consonante_unicode = chr(suma_digitos + ord("@"))
                campo2_final.append(consonante_unicode)

        # Unir los resultados en una sola cadena
        return ''.join(campo2_final).upper()
    
    @staticmethod
    def crea_archivo(valores):
        data = []  # Arreglo donde estara la informacion que se manda al archivo
        header = ['Num', 'Aleatorio']
        for i in range(len(valores)):
            data.append([i + 1, valores[i]])
        with open('generadorAleatorios.csv', 'w', encoding='utf-8', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(header)
            writer.writerows(data)
        print('El archivo ha sido creado satisfactoriamente')


def main(**kwargs):
    parametro_a = kwargs.get('a', 15169)
    parametro_b = kwargs.get('b', 19146)
    modulo = 2 ** 31
    campo1 = kwargs.get('c', "1Q133")
    campo2 = kwargs.get('d', "J6UP8")
    campo3 = kwargs.get('e', "488T3")
    iniciar = GenerarAleatorios(parametro_a, parametro_b, modulo, campo1, campo2, campo3, **kwargs)
    archivo = crear_archivo(iniciar.generar_claves())
    print(f"La clave final del producto es: {iniciar.primer_campo()[:5]}-{campo1}-{campo2}-"
          f"{campo3}-{iniciar.ultimo_campo()[-5:]} ")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='problema1.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=""" 
        Clase para generar claves de productos, empleando el metodo congruencial:
        X_(n + 1) = (aXn + b) mod(m)

        Donde:
        a = Termino multiplicativo
        b = Valor independiente
        c = Campo 2 de la clave
        d = Campo 3 de la clave
        e = Campo 4 de la clave
        Los valores 'a' y 'b' deben de ser enteros positivos de al menos 5 digitos
        A partir de un dato inicial (semilla), los tres campos de las claves tambien tienen
        que ser iguales a 5,  que debe estár escrito en mayusculas y de no contener 
        simbolos.
        """,
        epilog="""
        En caso de no declarar ningun valor, el sistema ya cuenta con valores declarados
        por omision (default).
        La clave final será impresa en la terminal
        """
    )
    parser.add_argument('-a', '--terminoA', default=15169,
                        dest="a", help="Termino multiplicativo (default: %(default)s)",
                        type=int, nargs=1, required=False)

    parser.add_argument('-b', '--terminoB', default=19146,
                        dest="b", help="Valor independiente (default: %(default)s)",
                        type=int, nargs=1, required=False)

    parser.add_argument('-c', '--campo1', default="1Q133",
                        dest="c", help="Valor independiente (default: %(default)s)",
                        type=str, nargs='?', required=False)

    parser.add_argument('-d', '--campo2', default="J6U8P",
                        dest="d", help="Valor independiente (default: %(default)s)",
                        type=str, nargs='?', required=False)

    parser.add_argument('-e', '--campo3', default="488T3",
                        dest="e", help="Valor independiente (default: %(default)s)",
                        type=str, nargs='?', required=False)
    datos_entrada = {k: v for k, v in vars(parser.parse_args()).items() if v is not None}  # para crear un diccionario
    main(**datos_entrada)
