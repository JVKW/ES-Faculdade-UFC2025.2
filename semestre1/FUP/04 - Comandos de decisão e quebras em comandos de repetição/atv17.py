while True:
  num = float(input("Digite n: "))
  if num > 0:
    print(f"{num**2:.2f}")
    print(f"{num**3:.2f}")
    print(f"{num**0.5:.2f}")
  else:
    break