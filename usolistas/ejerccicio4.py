#Dado un número, generar una lista con sus divisores.

def obtener_divisores(n):
    return [i for i in range(1, n + 1) if n % i == 0]


numero = 12
resultado = obtener_divisores(numero)
print(resultado)
