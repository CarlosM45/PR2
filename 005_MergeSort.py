# Carlos Alejandro Mercado Villalvazo
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # Crear dos arreglos temporales
    L = [0] * (n1)
    R = [0] * (n2)

    # Copiar los datos a los arreglos temporales L[] y R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Combinar los arreglos temporales
    i = 0     # Index inicial del primer subarreglo
    j = 0     # Index inicial del segundo subarreglo
    k = l     # Index inicial del subarreglo combinado

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar los elementos restantes de L[], si hay alguno
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar los elementos restantes de R[], si hay alguno
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l es el índice izquierdo, r es el índice derecho


def mergeSort(arr, l, r):
    if l < r:

        # Mismo que (l+r)//2 para evitar desbordamiento de enteros
        m = l+(r-l)//2

        # Ordenar la mitad izquierda y derecha
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


# Código de prueba
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Arreglo sin ordenar es:")
for i in range(n):
    print("%d" % arr[i],end=" ")

mergeSort(arr, 0, n-1)
print("\n\nArreglo ordenado es:")
for i in range(n):
    print("%d" % arr[i],end=" ")
