# -*- coding: utf-8 -*-
"""TP POD - 02/NumPy/Individual - 2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J4zahfU8SKL8dPvmnwShL8_4VuvLDqLJ

*   **Año:** [2024]
*   **Alumno/a:** [Antonella Robiolio]
*   **Legajo:** [42904775]

# NumPy
A continuación, cada celda va a pedir algo distinto. Por favor, realizarlo con la menor cantidad de lineas posibles y con NumPy.

Importar `numpy` con el alias `np` e imprimir la versión instalada.
"""

import numpy as np
print(np.__version__)

"""Setear el "seed" de la librearia en 0."""

np.random.seed(0)

"""Crear un vector vacio (en ingles, *empty*) para subir 100 imagenes de 100x600 pixeles. Imprimir el shape de dicho vector."""

vector = np.empty((100, 100, 600))
print(vector.shape)

"""Crear dos vectores vacios donde uno tiene 1,000 elementos y el otro tiene 100,000 elementos. Imprimir el tamaño ocupado en memoria de cada arreglo en bytes."""

vector_1 = np.empty(1000)
vector_2 = np.empty(100000)
print("Tamaño en memoria del vector con 1,000 elementos:", vector_1.nbytes, "bytes")
print("Tamaño en memoria del vector con 100,000 elementos:", vector_2.nbytes, "bytes")

"""Crear un vector vacío con 10 elementos. El quinto elemento tiene que ser igual a 1. Imprimir el vector."""

vector = np.empty(10)
vector[4] = 1
print(vector)

"""Generar un arreglo con los valores desde 10 hasta 35 en pasos de 2. Imprimir el arreglo."""

arreglo = np.arange(10, 36, 2)
print(arreglo)

"""Generar un arreglo con los valores desde -1 hasta -1 en pasos de 0.25. Luego, revertirlo. Imprimir el arreglo."""

import numpy as np
arreglo = np.arange(-1, 1.25, 0.25)
arreglo_revertido = arreglo[::-1]
print(arreglo_revertido)

"""Generar un arreglo que va desde -10 y 10 y que tenga 2,878 elementos. Imprimir el primer, último y 198º elemento."""

import numpy as np
arreglo = np.linspace(-10, 10, 2878)
primer_elemento = arreglo[0]
ultimo_elemento = arreglo[-1]
elemento_198 = arreglo[197]
print("Primer elemento:", primer_elemento)
print("Último elemento:", ultimo_elemento)
print("198º elemento:", elemento_198)

"""Generar una matriz 5x5 y con valores de 0 a 24. Imprimir la matriz."""

import numpy as np
matriz = np.arange(25).reshape(5, 5)
print(matriz)

"""Generar una lista de 10,000 elementos que vengan de una distribucion uniforme entre la constante de euler y π. (Nota: utilizar constantes de `numpy`). Dibujar la distribución con `matplotlib` en forma de histograma e imprimir el tipo de dato del arreglo."""

import matplotlib.pyplot as plt
lista = np.random.uniform(np.e, np.pi, 10000)

plt.hist(lista, bins=50, edgecolor='black')
plt.title("Distribución Uniforme entre e y π")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
print("Tipo de dato del arreglo:", type(lista))

"""Generar una lista de 20 elementos que vengan de una distribucion uniforme entre 0 y 1 e imprimirlo ordenado."""

lista = np.random.uniform(0, 1, 20)
lista_ordenada = np.sort(lista)
print(lista_ordenada)

"""Lo mismo que el punto anterior pero con una distribución normal con media 160 y desvío estandar 30."""

lista_normal = np.random.normal(160, 30, 20)
lista_normal_ordenada = np.sort(lista_normal)
print(lista_normal_ordenada)

"""Lo mismo que el punto anterior pero con una distribución normal con media 50 y desvío estandar 1. Imprimir el valor mas cercano (es decir, el de menor distancia) a 20 de los números generados."""

lista_normal_50 = np.random.normal(50, 1, 20)
lista_normal_50_ordenada = np.sort(lista_normal_50)
valor_mas_cercano = lista_normal_50_ordenada[np.abs(lista_normal_50_ordenada - 20).argmin()]

print("Lista ordenada:", lista_normal_50_ordenada)
print("Valor más cercano a 20:", valor_mas_cercano)

"""Teniendo en cuenta la declaración de la siguiente variable, imprimir la suma, la media, el máximo, y el mínimo de sus elementos."""

arreglo_dummy = np.array([1,9,10,23,45,78,94,78,10,23,65,47])

suma = np.sum(arreglo_dummy)
media = np.mean(arreglo_dummy)
maximo = np.max(arreglo_dummy)
minimo = np.min(arreglo_dummy)

print("Suma:", suma)
print("Media:", media)
print("Máximo:", maximo)
print("Mínimo:", minimo)

"""Hacer lo mismo que el punto anterior pero... con un arreglo particular. Imprimir el resultado y encontrarle una explicación."""

arreglo_weird = np.array([1,9,10,23,45,78,94,np.nan,10,23,65,47])

suma = np.nansum(arreglo_weird)
media = np.nanmean(arreglo_weird)
maximo = np.nanmax(arreglo_weird)
minimo = np.nanmin(arreglo_weird)

print("Suma:", suma)
print("Media:", media)
print("Máximo:", maximo)
print("Mínimo:", minimo) #El conjunto tiene valores en nan, para que ninguno de los calculos resulten en Nan debemos ejecutar el codigo "ignorando" los valores nan.

"""Generar un conjunto de 100 numeros ***enteros*** entre 0 y 10. Imprimir la cantidad de numeros pares que se generaron e imprimir el tipo de dato del arreglo."""

conjunto = np.random.randint(0, 11, 100)
cantidad_pares = np.sum(conjunto % 2 == 0)
tipo_de_dato_conjunto = type(conjunto)
print("Cantidad de números pares:", cantidad_pares)
print("Tipo de dato del arreglo:", tipo_de_dato_conjunto)

"""Generar un conjunto de 100 numeros enteros entre 0 y 10. Imprimir la cantidad de numeros mayores a 4 que se generaron."""

conjunto = np.random.randint(0, 11, 100)
cantidad_mayores_a_4 = np.sum(conjunto > 4)
print("Cantidad de números mayores a 4:", cantidad_mayores_a_4)

"""Generar un conjunto de 100 numeros enteros entre 0 y 10. Imprimir la cantidad de numeros mayores a 6 e impares que se generaron."""

conjunto = np.random.randint(0, 11, 100)
cantidad_mayores_a_6_impares = np.sum((conjunto > 6) & (conjunto % 2 != 0))
print("Cantidad de números mayores a 6 e impares:", cantidad_mayores_a_6_impares)

"""Supongamos que hay elecciones nacionales en un país y la cantidad de votos fueron los siguientes:


|Candidato 1|Cantidato 2|Cantidato 3|
|--|--|--|
|1,772,322  |1,102,669|2,100,978 |

Con `numpy`, calcular el porcentaje correspondiente a cada candidato y redondear a 2 dígitos. Imprimir los porcentajes finales y el numero del candidato ganador (aunque sea obvio, responder con lógica de `numpy`).
"""

votos = np.array([1772322, 1102669, 2100978])
total_votos = np.sum(votos)
porcentajes = np.round((votos / total_votos) * 100, 2)
candidato_ganador = np.argmax(votos) + 1

print("Porcentajes de votos:", porcentajes)
print("Candidato ganador:", candidato_ganador)

"""Generar un arreglo de 1,000 numeros de una distribución uniforme entre 0 y 1. Luego, generar otro arreglo que contenga todos los numeros del primer arreglo que son mayores a 0.7. Imprimir la media del "sub" arreglo."""

arreglo = np.random.uniform(0, 1, 1000)
sub_arreglo = arreglo[arreglo > 0.7]
media_sub_arreglo = np.mean(sub_arreglo)

print("Media del subarreglo:", media_sub_arreglo)

"""# Operación vectorizada vs. Operación loopeada
`numpy` no es solo poderoso por la gama de operaciones que podemos hacer en pocas lineas de código. Sino que por su eficiencia.

Supongamos que tenemos la función $f(x)=10*(x^2/e^x)$. Evaluar la función (en celdas apartes) entre -1 y 1 con 100,000 valores (i) con y (ii) sin un loop `for`. Medir tiempos de cada celda y sacar conclusiones.
"""

import numpy as np
import time

x = np.linspace(-1, 1, 100000)
start_time_vectorized = time.time()
f_vectorized = 10 * (x**2 / np.exp(x))
end_time_vectorized = time.time()
vectorized_time = end_time_vectorized - start_time_vectorized

print("Tiempo de operación vectorizada:", vectorized_time, "segundos")

start_time_loop = time.time()
f_loop = np.zeros_like(x)
for i in range(len(x)):
    f_loop[i] = 10 * (x[i]**2 / np.exp(x[i]))
end_time_loop = time.time()
loop_time = end_time_loop - start_time_loop

print("Tiempo de operación loopeada:", loop_time, "segundos")

"""**La operación vectorizada en numpy es significativamente más rápida que usar un loop for. En este caso, la evaluación vectorizada es aproximadamente 64 veces más eficiente. Esto demuestra por qué numpy es poderoso y eficiente para manejar grandes cantidades de datos: realiza operaciones en bloques optimizados en lugar de iterar elemento por elemento**

El resultado de la celda anterior (aprovechar lo obtenido), graficarlo como gráfico de lineas.
"""

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.plot(x, f_vectorized, label="Vectorizada", color='blue', alpha=0.7)
plt.plot(x, f_loop, label="Loopeada", color='red', linestyle='--', alpha=0.5)

plt.title("Comparación de Resultados: Vectorizada vs. Loopeada")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

"""# Análisis de imagenes

Matematicamente hablando, las imagenes son arreglos. Si una imagen es de blanco y negro, tenemos una imagen de un canal y puede ser interpretado como una simple matriz (`.shape=2`). Si tiene varios canales, tenemos una matriz asignada para cada canal (`.shape=3`).

[Lenna](https://en.wikipedia.org/wiki/Lenna) es una imagen ampliamente utilizada en ciencias de la computación. Se volvió un icono. La idea va a ser analizar a la imagen y tratarla para varios propositos. Corra la siguiente celda para descargar la imagen y guardala como arreglo `numpy` en la variable `image`. Utilizar esta variable en las siguientes celdas.
"""

!wget https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png
from PIL import Image
image = Image.open('Lenna_(test_image).png')
image = np.asarray(image)

"""Arranquemos con mostrar la imagen. Para eso, utilice `matplotlib.pyplot`."""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open('Lenna_(test_image).png')
image = np.asarray(image)

plt.imshow(image)
plt.axis('off')
plt.title("Imagen de Lenna")
plt.show()

"""¿Cual es la dimensión de la imagen y que ancho y alto tiene?"""

dimensiones = image.shape
ancho, alto = dimensiones[1], dimensiones[0]
print("Dimensiones de la imagen:", dimensiones)
print("Ancho:", ancho)
print("Alto:", alto)

"""Recorte la imagen en ancho entre (tomando como referencia los ejes de la imagen vista anteriormente) los 100 y 350 pixeles y en alto entre 200 y 400 pixeles. Mostrar el resultado."""

image_recortada = image[200:400, 100:350]

plt.imshow(image_recortada)
plt.axis('off')
plt.title("Imagen Recortada")
plt.show()

"""Muestre cada uno de los canales de la imagen."""

canal_rojo = image[:, :, 0]
canal_verde = image[:, :, 1]
canal_azul = image[:, :, 2]

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(canal_rojo, cmap='Reds')
plt.axis('off')
plt.title("Canal Rojo")
plt.subplot(1, 3, 2)
plt.imshow(canal_verde, cmap='Greens')
plt.axis('off')
plt.title("Canal Verde")
plt.subplot(1, 3, 3)
plt.imshow(canal_azul, cmap='Blues')
plt.axis('off')
plt.title("Canal Azul")
plt.show()

"""Calcule el minimo, el máximo, y el promedio de los valores de la imagen."""

minimo = np.min(image)
maximo = np.max(image)
promedio = np.mean(image)
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Promedio:", promedio)

"""La verdad que tener todos los colores de la imagen es muy redundante. Paselo a blanco y negro. Para ello, tome el promedio de los canales en cada pixel. Muestre la imagen en blanco y negro."""

imagen_bn = np.mean(image, axis=2).astype(np.uint8)
plt.imshow(imagen_bn, cmap='gray')
plt.axis('off')
plt.title("Imagen en Blanco y Negro")
plt.show()

"""Por último, vamos a proceder a "binarizar" la imagen. Es decir, vamos a setear en 1 TODOS los pixeles donde la intensidad (es decir, el valor del pixel) sea mayor a 200. El resto, lo seteamos a 0. Mostrar el resultado."""

imagen_binarizada = (imagen_bn > 200).astype(int)
plt.imshow(imagen_binarizada, cmap='gray')
plt.axis('off')
plt.title("Imagen Binarizada")
plt.show()

"""# Análisis de datos

`boston.csv` es un archivo csv ampliamente utilizado como 'juguete' en proyectos de Machine Learning. Para descargarlo, corra la siguiente celda.
"""

!wget https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/MASS/Boston.csv

"""Lea el archivo csv (sin `pandas` pero se puede usar `csv`) y quedese con todas las columnas que son numericas. Inspeccionarlo puede hacer el trabajo bastante facil.

Nota: Aunque `numpy` tenga una libreria para leer archivos, en este caso no no es útil por que todas las columas constan de diferentes tipo de dato y ademas el encabezado es `string`.
"""

import csv
with open('Boston.csv', 'r') as file:
    reader = csv.reader(file)
    encabezado = next(reader)
    datos = [fila for fila in reader]

print("Encabezado:", encabezado)
columnas_numericas = [[float(fila[i]) for i in range(1, len(encabezado))] for fila in datos]

print("Ejemplo de las columnas numéricas:", columnas_numericas[:2])

"""*Una* vez procesado el archivo csv, proceda a convertirlo en una matriz de `numpy`."""

matriz_numerica = np.array(columnas_numericas)
print("Forma de la matriz numérica:", matriz_numerica.shape)

"""Reporte el promedio de todas las columnas."""

promedios_columnas = np.mean(matriz_numerica, axis=0)

print("Promedios de todas las columnas:", promedios_columnas)

"""Reporte la división entre una columna y otra (a elección cuales)"""

columna_1 = matriz_numerica[:, 1]
columna_2 = matriz_numerica[:, 2]
division = columna_1 / columna_2
print("División entre la segunda y tercera columna:", division)