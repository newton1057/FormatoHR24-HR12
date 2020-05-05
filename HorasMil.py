horamilitar = int(input("Escribir hora en formato militar: ")) 

if horamilitar >= 1200:
    auxAP = "PM"
    if horamilitar >= 1300:
        horamilitar = horamilitar - 1200
else:
    auxAP = "AM"

horaNormal = horamilitar // 100
minutosNormal = horamilitar - (horaNormal*100)

print(horaNormal,":",minutosNormal," ",auxAP)