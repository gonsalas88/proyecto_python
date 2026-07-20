def contar_aprobadas(notas):
    aprobadas = 0 

    for nota in notas:
        if nota >= 5:
            aprobadas += 1
            
    return aprobadas 
    
notas = [8, 4, 7, 3, 9, 6]

resultado = contar_aprobadas(notas)

print("Aprobadas:", resultado) 
