# Ejemplo de programación funcional en Python

# Definición de una lista de números
numeros = [1, 2, 3, 4, 5]

# Función para elevar un número al cuadrado
def elevar_al_cuadrado(x):
    return x ** 2

# Utilizando la función map para aplicar la función a cada elemento de la lista
cuadrados = list(map(elevar_al_cuadrado, numeros))

# Filtrando solo los números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Función para sumar dos números
def suma(x, y):
    return x + y

# Utilizando la función reduce para aplicar la función de suma a la lista
from functools import reduce
suma_total = reduce(suma, numeros)

# Imprimiendo resultados
print("Lista original:", numeros)
print("Cuadrados:", cuadrados)
print("Números pares:", pares)
print("Suma total:", suma_total)
