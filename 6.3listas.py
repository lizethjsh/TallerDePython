milista=[ 6,3,4,21,54,76,1]


#Imprime la lista
print (milista)

# Imprime solo un valor de la lista en este caso el segundo valor
print (milista[2])

# Imprime la cantidad de elementos que tiene la lista
print (len(milista))

# Agrega un valor al final de la lista
milista.append(13)
print (milista)

#Recorremos el arreglo
for elemento in milista:
    print (f"Elemento {elemento}")

#Recorremos un arreglo y usamos enumerate para tener un contador
for count, element in enumerate(milista):
    print(f"Contador {count} elemento {element} ")
    
    
# Buscar un valor en la lista    
if 21 in milista:
    print("Si existe el numero 21 en la lista")
    print(milista.index(21))

# Acomodamos los elementos de la lista de menor a mayor
milista.sort()
print (milista)