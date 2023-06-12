#1.- Leer números enteros de teclado, hasta que el usuario ingrese el 0.
# Finalmente, mostrar la sumatoria de todos los números ingresados.

num = -1
suma = 0
while num!= 0:
  num = int (input( "Ingresa un numero: "))
  suma += num
print ("La suma de los numeros ingresados es: ", suma)
  

#2.- Escriba un algoritmo que lea del teclado un número entero y que compruebe
# si el número es menor que 10. Si no lo está, debe volver a leer el número
# repitiendo la operación hasta que el usuario escriba un valor correcto.
# Finalmente, debe escribir por pantalla el valor leído cuando este sea correcto.

num = 11
menor = 0
while num > 10: 
  num = int (input ("Ingrese un numero: "))
  menor = num
print ("El numero correcto fue: ", menor )


#3.- Modifique el algoritmo del problema anterior para que, en vez de comprobar
# que el número sea menor que 10, compruebe que se encuentre en el rango (0, 20).
num = 21
menor = 0
for num in range (0, 20): 
  num = int (input ("Ingrese un numero: "))
  menor = num
print ("El numero correcto fue: ", menor )

#4.- Modifique el algoritmo del problema anterior para que cuente las veces que ha
# leído un número de teclado y escriba el resultado por pantalla.

