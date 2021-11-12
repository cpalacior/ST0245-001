import numpy as np
import csv
import urllib.request
from collections import deque

def bajar():
    url = "https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/datasets/csv/enfermo_csv/0.csv"
    #url = input()
    urllib.request.urlretrieve(url,"Enferma.csv")

def guardarArr():
  arr = np.loadtxt("Enferma.csv", delimiter=",")
  return arr

def sacarTamanio(arreglo):
  filas = np.shape(arreglo)[0]
  columnas = np.shape(arreglo)[1]
  return columnas, filas 


def InterpolacionBilineal(arreglo):
  filas = np.shape(arreglo)[0]
  columnas = np.shape(arreglo)[1]
  nuevo_arreglo = np.zeros([filas//2, columnas//2])
  #filas_nuevas = np.shape(nuevo_arreglo)[0]
  #columnas_nuevas = np.shape(nuevo_arreglo)[1]
  print("filas = ", filas, " columnas = ", columnas) # columnas 480, filas 360
  print("filas = ", filas//2, " columnas = ", columnas//2) # columnas 240, filas 180
  i = 0 
  o = 0 
  while(i < filas):
    j = 0 
    k = 0
    while(j < columnas):
      try: 
        nuevo_arreglo[o][k] = arreglo[i][j] + arreglo[i+1][j] + arreglo[i][j+1] + arreglo[i+1][j+1]
        nuevo_arreglo[o][k] = nuevo_arreglo[o][k] // 4
      except:
        nuevo_arreglo[o][k] = arreglo[i][j] + arreglo[i][j+1]
        nuevo_arreglo[o][k] = nuevo_arreglo[i][j] // 2  
      j += 2
      k += 1
    i += 2
    o += 1
  return nuevo_arreglo

def escribirArchivo(arreglo, filas):
    with open("NuevaEnferma.csv", 'w') as archivo:
        texto = csv.writer(archivo)
        i = 0
        while (i < filas):
          texto.writerow(arreglo[i])
          i += 1
        
def pasarAString(matriz):
  filas = np.shape(matriz)[0]
  columnas = np.shape(matriz)[1]
  cadena = ""
  i = 0 
  while(i < filas):
    j = 0 
    while(j < columnas):  
      entero = int(matriz[i][j])
      cadena = cadena + str(entero)
      j += 1
    i += 1
  return cadena
  
def Lz77Compression(long_ventana, BB, cadena):
  lista = ""
  pos_cursor = 0
  BA = long_ventana - BB
  while(pos_cursor < len(cadena)):
    longitud = 0
    offset = 0
    carat = str(cadena[pos_cursor])
    w = pos_cursor - 1
    temp = BB
    temp2 = 0
    otra = 0
    while(w >= 0 and temp - 1 > 0):
      temp2 = BA
      if(cadena[w] == cadena[pos_cursor]):
        offset_temp = otra + 1
        pos = pos_cursor + 1
        b = w + 1
        lon = 1
        while(pos < len(cadena) and cadena[b] == cadena[pos] and temp2 - 1 > 2):
          b += 1
          lon += 1
          pos += 1
        if(lon >= longitud):
          longitud = lon
          offset = offset_temp
          if(pos == len(cadena)):
            carat = "eof"
          else:
            carat = str(cadena[pos])
      w -= 1
      otra += 1
    lista += "<{},{},{}>".format(offset, longitud, carat)
    pos_cursor += longitud + 1
  return lista

def Lz77Decompression(ca):
  cinta = ""
  pos_inicio = 0
  pos_fin = 0
  i = 0
  while(i < ca.Length-1):
    if (ca[i] == '<'):
      pos_inicio = i + 1
      break
    else:
      cinta += ca[i]
    i += 1
  final = "";
  i = len(ca) - 1
  while(i > 1):
    if (ca[i] == '>' and (ca[i - 2] == ',')):
        pos_fin = i
        break 
    else:
      final += ca[i]
    i -= 1
  lista = deque()            
  cont = 0
  temp = ""
  offset = 0
  lon = 0
  carat = ""
  if (pos_fin - pos_inicio > 4):
    i = pos_inicio
    while(i <= pos_fin):
      if (ca[i] == ',' and cont < 2):
          if (cont == 0):
            offset = int.Parse(temp)
          else:
            lon = int.Parse(temp)
          temp = ""
          cont+=1
      elif (ca[i] == '>' and len(temp) > 0):
        carat = temp
        i+=1
        dat = "Datos(offset, lon, carat)"
        lista.append(dat)
        offset = 0 
        lon = 0 
        carat = "" 
        cont = 0 
        temp = ""
      else:
        temp += ca[i]
      i += 1
  i = 0
  while(i < lista.Count):
    pos = cinta.Length - lista[i].Offset;
    lone = lista[i].Longitud
    cade = ""
    if (lista[i].Cod_carater != "eof"):
      cade = lista[i].Cod_carater
    while (lone - 1 > 0):
      cinta += cinta[pos+1]
    cinta += cade
    i += 1
  cinta += final
  return cinta


def __main__():
  bajar()
  matriz = guardarArr()
  print(matriz)
  print(matriz.size)
  print(matriz[1][1])
  matriz_bilineal = InterpolacionBilineal(matriz)
  print(matriz_bilineal)
  print(matriz_bilineal.size)
  columnas, filas = sacarTamanio(matriz_bilineal)
  print("filas = ", filas)
  print("columnas = ", columnas)
  escribirArchivo(matriz_bilineal, filas)
  #cadena = pasarAString(matriz)
  #print(cadena[0:10])
  #escribirArchivo(cadena, 2)


__main__()
