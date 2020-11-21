#Archivo explicando listas

numeros = [23,89,127,1289,8912]

#Para agregar un elemento a una lista ocupamos append
numero_extra = 33
numero_extra1 = 1223
numero_extra2 = 89

numeros.append(numero_extra)

print(numeros)

numeros.pop() #Elimina 

print(numeros)

numeros.extend([numero_extra1,numero_extra2]) #Agrega los dos números extra que declaramos

print(numeros)