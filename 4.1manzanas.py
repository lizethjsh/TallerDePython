from clear import cleaning
import time 
precioDeManzana:int = int(input("Ingrese el precio de la manzana: "))
cantidadManzanas:int = int(input("Ingrese la cantidad de las manzanas: "))
name:str=input("Cual es su nombre: ")
#Comentarios de una linea 

cleaning()
while cantidadManzanas != 0:
    if cantidadManzanas ==0:
        print("No quieres comprar manzanas ok ta bn")
        break
    
    #Concatenacion diferentes formas 
    print("Las manzanas estan en: " + str(precioDeManzana))
    print("La cantidad de manzanas es:", cantidadManzanas)
    time.sleep(3)
    print(' Nota de venta '.center(50,'='))
    if cantidadManzanas == 18 or name== " Lizeth ":
        descuento=(cantidadManzanas*precioDeManzana)*.2
        print("Tienes un descuento secreto de", descuento)
        print(f"pagaras {(cantidadManzanas*precioDeManzana)-descuento}")
    elif cantidadManzanas> 10:
        descuento=(cantidadManzanas*precioDeManzana)*.1
        print("Tienes un descuento de", descuento)
        print(f"pagaras {(cantidadManzanas*precioDeManzana)-descuento}")
    else:
        print(f"Vas a pagar: {cantidadManzanas * precioDeManzana}")
    break