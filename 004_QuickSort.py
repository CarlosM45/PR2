# Carlos Alejandro Mercado Villalvazo
def partition(array, low, high):

    # Elegir el último elemento como pivote
    pivot = array[high]

    # Puntero para el elemento más pequeño
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Arreglo sin ordenar:")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Arreglo ordenado:')
print(data)
