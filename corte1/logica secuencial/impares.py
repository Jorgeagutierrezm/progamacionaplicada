#Jorge Andres Gutierrez este ejercicio vale por una decima del corte.
times = input("Enter a number of times: ")
times = int(float(times))  # Convertimos a float y luego a int para evitar errores
print(type(times))
print(times)

if times == 0:
    print("Don't do anything")
else:
    for i in range(1, times + 1):
        if i % 2 != 0:  # Condición para números impares
            print(f"{i}")
