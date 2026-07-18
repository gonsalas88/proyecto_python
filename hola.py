numero1 = int(input("Primer numero: "))
numero2 = int(input("Segundo numero: "))
suma = numero1 + numero2 
resta = numero1 - numero2 
multiplicacion = numero1 * numero2 

suma = numero1 + numero2 
resta = numero1 - numero2 
multiplicacion = numero1 * numero2 

print("La suma es", suma)
print("La resta es", resta)
print("La multiplicacion es", multiplicacion)

if numero2 != 0:
    division = numero1 / numero2 
    print("La division es", division) 
else: 
    print("No se puede dividir entre cero")
    
if numero1 > numero2:
    print("El numero es mayor")
elif numero1 < numero2:
    print("El segundo numero es mayor")
else: 
    print("Los numeros son iguales") 
