nombre = "fernando"
apellido = "jimenez"
nombre_completo = nombre + " " + "apellido"
print(nombre_completo)
nombre_c = f"{nombre}{apellido}"
print(nombre_c)

#concatenar

nombreCompleto =" ". join([nombre, apellido])
print(nombreCompleto)


lista = []
lista.append(nombre)
lista.append(apellido)
nombreCompleto = " ".join(lista)
print(nombreCompleto)
