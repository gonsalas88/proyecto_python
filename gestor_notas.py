notas = []

def calcular_resumen(notas):
    promedio = sum(notas) / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)
    
    return promedio, nota_maxima, nota_minima
while True:
    try:
        nota = float(input("Escribe una nota 0 -1 para terminar : "))
        
        if nota == -1:
            break 
            
        if 0 <+ nota <+ 10:
            notas.append(nota)
        else: 
            print("La nota debe estar entre 0 y 10")
            
    except ValueError:
        print("Debes escribir un numero")

if len(notas) > 0:
    promedio = sum(notas) / len(notas) 
    
    reporte = ( 
        f"Notas: {notas}\n"
        f"Promedio: {promedio}\n"
        f"Nota mas alta: {max(notas)}\n"
        f"Nota mas baja: {min(notas)}\n"
    )
    promedio, nota_maxima, nota_minima = calcular_resumen(notas) 
    
    with open("reporte_notas.txt", "w") as archivo:
        archivo.write(reporte)
        
    print("Reporte guardado en reporte_notas.txt")
        
    print("Promedio:", promedio)
    print("Nota mas alta:", max(notas))
    print("Nota mas baja:", min(notas))
else: 
    print("No se registraron notas")
    
    
