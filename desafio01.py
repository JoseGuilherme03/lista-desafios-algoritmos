"""
1. Escreva um algoritmo para encontrar os números faltantes de um array:
Input : array(1,2,3,6,7,8);
Output : array([3] => 4, [4] => 5);
"""


def encontre_numeros_faltantes(array):
    array.sort()

    intervalos_faltantes = []

    # Percorre o array para identificar os intervalos de números faltantes
    for i in range(len(array) - 1):
        if array[i + 1] - array[i] > 1:
            intervalo = list(range(array[i] + 1, array[i + 1]))
            intervalos_faltantes.append({array[i]: intervalo})

    return intervalos_faltantes


array = [1, 2, 3, 6, 7, 8]
resultados = encontre_numeros_faltantes(array)
print(f"Números faltantes na sequência do array: {resultados}", )
