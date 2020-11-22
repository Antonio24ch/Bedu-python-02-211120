#Script que calcula la tabla de multiplicar de un numero

#Solicitar numero al usuario por consola
numero = input('que numero quieres multiplicar?')

#Dato ingresado por usuario es una cadena 'str' 
#Debe convertir a numero int para poder multiplicar 
numero = int(numero)

for n in range(10):
    r = numero * (n + 1)
    print(r)

#A continuacion se muestra la tabla de multiplicar del numero <numero>
#----------
# 8 * 1 = 8
# 8 * 2 = 16
# ...
for n in range(10):
    r = numero * (n+1)
    print(f'{numero} * {n+1} = {r}')
 
