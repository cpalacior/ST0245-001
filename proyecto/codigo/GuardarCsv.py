import urllib.request
from collections import deque

def bajar():
    url = input()
    urllib.request.urlretrieve(url,"Enferma.csv")

def leerArchivoComoCadena():
    with open("Enferma.csv","r") as archivo:
        texto = archivo.read()
        return texto

def pasarAListaEnlazada(texto):
    lineas = texto.split("\n")
    lista = deque()
    for linea in lineas:
        if linea != "":
            lista.insert(0,linea.split(","))
    return lista    

def __main__():
    bajar()
    texto = leerArchivoComoCadena()
    lista = pasarAListaEnlazada(texto)
    print(lista)

__main__()