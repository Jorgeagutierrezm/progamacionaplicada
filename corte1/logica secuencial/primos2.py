def es_primo(num):
    if num < 2:
        return False
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True

while True:
    value = int(input('Ingrese un valor: '))
    if es_primo(value):
        print(f'{value} es un número primo\n')
    else:
        print(f'{value} NO es un número primo\n')

    continuar = input('¿Desea continuar? Presione 1 para continuar o cualquier otra tecla para salir: ')
    if continuar != '1':
        break
