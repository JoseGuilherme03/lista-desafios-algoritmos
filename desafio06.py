def fibonacci(n):
    a = 1
    b = 1
    resultado = []

    for _ in range(n):
        resultado.append(a)
        a, b = b, a + b

    return resultado


numero = 6
print(f"Fibonacc: {fibonacci(numero)}")
