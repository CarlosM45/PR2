# Carlos Alejandro Mercado Villalvazo
# Programa por mezcla de 3 vías
def merge(arr, left, mid1, mid2, right):
    
    # Tamaños de los 3 subarreglos
    size1 = mid1 - left + 1
    size2 = mid2 - mid1
    size3 = right - mid2
    
    # Arreglos temporales para las 3 partes
    left_arr = arr[left:left + size1]
    mid_arr = arr[mid1 + 1:mid1 + 1 + size2]
    right_arr = arr[mid2 + 1:mid2 + 1 + size3]
    
    # Combinar los 3 subarreglos en el arreglo original
    i = j = k = 0
    index = left
    
    while i < size1 or j < size2 or k < size3:
        min_value = float('inf')
        min_idx = -1
        
        # Encontrar el valor mínimo entre los 3 subarreglos
        if i < size1 and left_arr[i] < min_value:
            min_value = left_arr[i]
            min_idx = 0
        if j < size2 and mid_arr[j] < min_value:
            min_value = mid_arr[j]
            min_idx = 1
        if k < size3 and right_arr[k] < min_value:
            min_value = right_arr[k]
            min_idx = 2
        
        # Colocar el valor mínimo en el arreglo original
        if min_idx == 0:
            arr[index] = left_arr[i]
            i += 1
        elif min_idx == 1:
            arr[index] = mid_arr[j]
            j += 1
        else:
            arr[index] = right_arr[k]
            k += 1
        
        index += 1

def three_way_merge_sort(arr, left, right):
    
    # Caso base, si la condición se cumple, no hay nada que ordenar
    if left >= right:
        return
    
    # Encontrar dos puntos medios para dividir el arreglo en 3 partes
    mid1 = left + (right - left) // 3
    mid2 = left + 2 * (right - left) // 3
    
    # Ordenar recursivamente la primera tercera parte
    three_way_merge_sort(arr, left, mid1)
    
    # Ordenar recursivamente la segunda tercera parte
    three_way_merge_sort(arr, mid1 + 1, mid2)
    
    # Ordenar recursivamente la última tercera parte
    three_way_merge_sort(arr, mid2 + 1, right)
    
    # Combinar las 3 partes ordenadas
    merge(arr, left, mid1, mid2, right)

if __name__ == "__main__":
    
    # Arreglo de ejemplo
    arr = [5, 2, 9, 1, 6, 3, 8, 4, 7]
    
    # Llamar a la función de ordenamiento 3 vías
    three_way_merge_sort(arr, 0, len(arr) - 1)
    
    # Imprimir el arreglo ordenado
    print(*arr)
    