# Carlos Alejandro Mercado Villalvazo
def insertionSort(arr):
    n = len(arr)  # Obtener la longitud del arreglo
     
    if n <= 1:
        return  # Si el arreglo tiene 0 o 1 elementos, ya está ordenado

    for i in range(1, n):  # Iterar desde el segundo elemento
        key = arr[i]  # Almacenar el elemento actual a insertar
        j = i-1
        while j >= 0 and key < arr[j]:  # Mover elementos que son mayores que el key
            arr[j+1] = arr[j]  # Cambiar los elementos hacia la derecha
            j -= 1
        arr[j+1] = key  # Insertar el key en su posición correcta
 
# Ordenar un arreglo de ejemplo
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
