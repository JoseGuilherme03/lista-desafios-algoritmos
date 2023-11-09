"""
3. Escreva um algoritmo para encontrar três números consecutivos de um array que
somados o resultado é igual a um outro número fornecido:
"""


def encontra_soma_numero_x(array, numero):
    lista_resultado = []
    for i in range(0, len(array) -2):
        resultado = array[i] + array[i + 1] + array[i + 2]

        if resultado == numero:
            string = f"{array[i]} + {array[i + 1]} + {array[i + 2]} = {numero}"
            lista_resultado.append({i: string})

    return lista_resultado

array = [2, 7, 7, 1, 8, 2, 7, 8, 7]
numero = 16
print(f"3 números consecutivos com soma igual {numero}: {encontra_soma_numero_x(array, numero)}")