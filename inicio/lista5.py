#leer un parrafo y contar cuantas oraciones tiene

parrafo_input = input("escribe un parrafo:  ")
#borrar espacios al inicio y al final
if parrafo_input[-1] == ".":
 parrafo = parrafo_input[0 : len(parrafo_input)-1].strip()
else : parrafo = parrafo_input
print(parrafo)
oraciones = parrafo.split(", ")
print(f"el parrafo tiene {len(oraciones)} oraciones")
print(oraciones)
