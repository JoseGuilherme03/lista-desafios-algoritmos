"""
Escreva um algoritmo para encontrar um único número de um array onde cada
número repete três vezes, exceto um:
"""


def encontre_numero_nao_repetido_3_vezes(array):
    contagem = {}

    for n in array:
        if n in contagem:
            contagem[n] += 1
        else:
            contagem[n] = 1

    for n, frequencia in contagem.items():
        if not frequencia == 3:
            return n


array = [5, 3, 4, 3, 5, 5, 3]
resultado = encontre_numero_nao_repetido_3_vezes(array)
print(f"Unico número que não repete 3 vezes no array: {resultado}", )
