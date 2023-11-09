"""
4. Escreva um algoritmo para encontrar um único número de um array que não se
repita duas vezes:
Input : array(5, 3, 4, 3, 4);
Output : array
(
[0] => 5,
[1] => 3,
[2] => 4,
[3] => 3,
[4] => 4,
);
Single Number: 5
"""


def encontre_numero_nao_repetido_2_vezes(array):
    contagem = {}

    for n in array:
        if n in contagem:
            contagem[n] += 1
        else:
            contagem[n] = 1
            
    for n, frequencia in contagem.items():
        if not frequencia == 2:
            return n

array = [5, 3, 4, 3, 4]
resultado = encontre_numero_nao_repetido_2_vezes(array)
print("Número único no array:", resultado)