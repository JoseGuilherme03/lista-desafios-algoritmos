"""
2. Escreva um algoritmo para encontrar três números consecutivos de um array que
somados o resultado é igual a zero:
Input : array(-1,0,1,2,-1,-4);
Output : array([0] => -1 + 0 + 1 = 0);0
"""


def encontra_soma_zero(array):
    lista_resultado = []
    for i in range(0, len(array) - 2):
        resultado = array[i] + array[i + 1] + array[i + 2]

        if resultado == 0:
            string = f"{array[i]} + {array[i + 1]} + {array[i + 2]} = 0"
            lista_resultado.append({i: string})

    return lista_resultado


array = [-1, 0, 1, 2, -1, -4]
print(f"3 números consecutivos com soma igual a zero: {encontra_soma_zero(array)}")
