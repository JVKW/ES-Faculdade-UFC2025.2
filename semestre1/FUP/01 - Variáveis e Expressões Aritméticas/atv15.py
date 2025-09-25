seg = int(input("Segundos: "))

print(f"Horas: {seg // 3600}")
print(f"Minutos: {(seg % 3600) // 60}")
print(f"Segundos: {seg%60}")