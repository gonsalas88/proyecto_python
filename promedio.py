aprobadas = 0 
suspensas = 0
notas = [8, 4, 7, 3, 9, 6]


for nota in notas: 
    if nota >= 5:
        aprobadas += 1
    else: 
        suspensas += 1 
   
   
print("Aprobadas:", aprobadas)
print("Suspensas:", suspensas)


