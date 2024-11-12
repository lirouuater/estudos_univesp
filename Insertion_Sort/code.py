#ordenar um conjunto inserindo os elementos em um subconjunto ordenado# 
def insertion_sort(v):
    for i in range(1, len(v)):
        j = i - 1
        while j >= 0 and v[j] > v[j +1]:
            v[j], v[j + 1] = v[j + 1], v[j]
            j -= 1