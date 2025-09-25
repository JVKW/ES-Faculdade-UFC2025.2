def converter_km(K):
    return K / 3.6

resp = converter_km(500)

print(f"Km/h → {resp:.2f} m/s")