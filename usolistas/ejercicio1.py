#Crear una lista de cadenas y concatenarlas en una sola, separadas por un espacio.

def concatenar_cadenas(lista):
    return " ".join(lista)

lista_ejemplo = ["Hola", "mundo", "esto", "es", "Python"]
resultado = concatenar_cadenas(lista_ejemplo)
print(resultado)
