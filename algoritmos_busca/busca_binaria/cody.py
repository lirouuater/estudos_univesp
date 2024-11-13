#busca binária em python#

def busca_binaria(vetor, elemento): #vetor precisa ser ordenado#
    esquerda = 0              #posição inicial do vetor#
    direita = len(vetor) - 1   #posição final do vetor#

    while esquerda <= direita:
        meio = (esquerda + direita) #posição do meio do vetor#
        
        if vetor[meio] == elemento: #se o elemento esta no meio
            return meio #retorna a posição do elemento
        

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
elemento = 5

posicao = busca_binaria(vetor, elemento)
print(posicao)  # saída: 4  posição







