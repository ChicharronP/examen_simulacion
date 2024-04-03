from libs.fun.common import sumar_unicodes, unificar

palabra = "Gatito123"

palabra_ordenada = list(palabra)
palabra_original = list(palabra)
posicion = len(palabra_ordenada) - 1
palabra_ordenada.insert(0, palabra_ordenada[posicion])
palabra_ordenada.pop(-1)
suma1 = sumar_unicodes(palabra_original)
suma2 = sumar_unicodes(palabra_ordenada)
suma_total = unificar(suma1, suma2)














    




