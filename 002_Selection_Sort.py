# Carlos Alejandro Mercado Villalvazo
def selectionSort(array, size):
   
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # Seleccionar el elemento más pequeño
            if array[j] < array[min_index]:
                min_index = j
         # Cambiar el elemento más pequeño con el elemento actual
        (array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('El arreglo tras ordenar por selección es:')
print(arr)
