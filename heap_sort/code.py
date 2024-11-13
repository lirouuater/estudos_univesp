def heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)

    # Construa um heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Remova o elemento máximo e heapify
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

# Exemplo de uso
arr = [12, 11, 13, 5, 6, 7]
print("Array original:", arr)
print("Array ordenado:", heap_sort(arr))