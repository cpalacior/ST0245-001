import numpy as np
import csv
import urllib.request

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


def escalar(arreglo):
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
        



def __main__():
  bajar()
  matriz = guardarArr()
  print(matriz)
  print(matriz.size)
  #print(matriz [42][5])
  matriz_bilineal = escalar(matriz)
  print(matriz_bilineal)
  print(matriz_bilineal.size)
  columnas, filas = sacarTamanio(matriz_bilineal)
  #print("filas = ", filas)
  #print("columnas = ", columnas)
  escribirArchivo(matriz_bilineal, filas)


__main__()
