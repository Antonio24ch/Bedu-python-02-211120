
#Generar una lista con valores aleatorios
from random import randint

#Lista vacia
lista_aleatoria = []

#Solicitar cuantos valores
elementos = input('Cuantos elementos necesitas?')
elementos = int(elementos)

contador = 1

while contador <= elementos:
    #Generar valor aleatorio
    matriz = randint(1,100)
    #Numero aleatorio multiplicado por el numero del usuario
    valor = matriz * elementos
    #Guardar valor aleatorio en lista
    lista_aleatoria.append(valor)
    #Sumar a contador para la siguiente vuelta
    contador = contador + 1

    print(lista_aleatoria)
