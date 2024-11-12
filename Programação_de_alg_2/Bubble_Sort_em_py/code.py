#Bubble Sorte em Python(ordenação de vetores)#

def bubble_sort(vetor):
    for i in range(len(vetor) - 1, 0, -1):  # gera a contagem decrescente do vetor #
        for j in range(i):                     # compara os elementos adjacentes #
            if vetor[j] > vetor[j + 1]:           # se o primeiro for maior que o segundo, eles trocam de posição # 
                vetor[j], vetor[j + 1]=vetor[j + 1], vetor[j]    # troca os elementos# 