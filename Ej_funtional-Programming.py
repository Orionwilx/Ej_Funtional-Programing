numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Función que verifica si un número es par
def es_par(numero):
    return numero % 2 == 0

# Función que calcula el cuadrado de un número
def cuadrado(numero):
    return numero ** 2

# Usando programación funcional para calcular la suma de los cuadrados de los números pares
suma_cuadrados_pares = sum(map(cuadrado, filter(es_par, numeros)))

print(suma_cuadrados_pares)
