#busca linear em python#

def busca_linear(vetor, elemento):           # vetor é a lista e elemento é o valor que estamos procurando#
    for i in range(len(vetor)):              # percorre todos os elementos do vetor#           
        if vetor[i] == elemento:              # verifica se o elemento atual é igual ao elemento procurado #
            return i                          # se for igual, retorna a posição do elemento no vetor# 
    return -1                                  # se não encontrar o elemento, retorna -1 #
    

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(busca_linear(vetor, 5)) # imprimira 4       


vetor = [1, 2, 3, 4, 5]
elemento = 3
print(busca_linear(vetor, elemento))  # imprimirá 2

vetor = [1, 2, 3, 4, 5]
elemento = 6
print(busca_linear(vetor, elemento))  # imprimirá -1