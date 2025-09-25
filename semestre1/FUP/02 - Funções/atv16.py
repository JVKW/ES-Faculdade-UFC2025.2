def calc_tempo(segundos):
    hor = segundos // 3600
    min = (segundos % 3600) // 60
    seg = segundos % 60
    
    return hor, min, seg

print("Horário: ", calc_tempo(12600))