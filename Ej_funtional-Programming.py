numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Función que verifica si un número es par
def is_par(num):
    return num % 2 == 0

# Función que calcula el cuadrado de un número
def scuared(num):
    return num ** 2

# Usando programación funcional para calcular la suma de los cuadrados de los números pares
sum_scuared_pairs = sum(map(scuared, filter(is_par, numbers)))

print(sum_scuared_pairs)
