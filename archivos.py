with open("mensaje.txt", "r") as archivo:
    contenido = archivo.read()
    
print(contenido) 

with open("mensaje.txt", "a") as archivo:
    archivo.write("\nEstoy aprendiendo Python.")
    
