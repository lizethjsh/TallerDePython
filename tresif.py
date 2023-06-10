#1.- Solicitar al usuario que ingrese dos números y mostrar cuál
# de los dos es menor. Considerar el caso en que ambos números son iguales.

num1 = int( input("Ingresa un numero: " ))
num2 = int( input("Ingresa un segundo numero: " ))

if num1 == num2:
    print("Los dos numeros son iguales")
elif num1 < num2: 
    print("El numero", num1, "es el menor")
elif num2 < num1:
    print("El numero", num2, "es el menor")

#2.- Solicitar al usuario un número de cliente. Si el número es el 1000,
# imprimir "Ganaste un premio".

cliente = int( input( "Ingrese el numero de cliente: "))
if cliente == 1000:
    print("¡Ganaste un premio!")

#3.- Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor.
# No considerar el caso en que ambos números son iguales.

num1 = int( input("Ingresa un numero: " ))
num2 = int( input("Ingresa un segundo numero: " ))

if num1 < num2: 
    print("El numero", num1, "es el menor")
elif num2 < num1:
    print("El numero", num2, "es el menor")

#4.- Hacer un programa que permita saber si un año es bisiesto.
# Para que un año sea bisiesto debe ser divisible por 4 y 
# no debe ser divisible por 100, excepto que también sea divisible por 400

anho = int( input(" Ingresa un año: "))

if anho%4 == 0:
    print("El año ", anho, " es año bisiesto")
    
    if anho%400 == 0:
        print("El año ", anho, " es año bisiesto")
        
        if anho%100 == 0:
            print("El año ", anho, " es año bisiesto") 


#5.- Escriba un programa que pida tres números y que escriba si son los tres iguales,
# si hay dos iguales o si son los tres distintos.
num1 = int( input("Ingresa un numero: " ))
num2 = int( input("Ingresa un segundo numero: " ))
num3 = int( input("Ingresa un tercer numero: " ))

if num1 == num2 :
    if num3 == num2:
        print("Los tres numeros son iguales")    
elif num1 == num3: 
    print("Hay solo dos numeros iguales")
else:
    print("Los tres números son distintos.")