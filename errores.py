try:
    edad = int(input("Escribir tu edad: "))
    print("El proximo anos tendras", edad + 1)
except ValueError:
    print("Debes escribir un numero entero") 
