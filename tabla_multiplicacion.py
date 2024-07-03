numero = int(input("introducir un numero menor que 10:"))
if numero < 10:
    for i in range (1, 11):
        print(f"{numero} x {i} = {numero * i}")
    else:
        print("el numero debe ser menor que 10")
