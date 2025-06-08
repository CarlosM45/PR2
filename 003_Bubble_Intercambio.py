# Carlos Alejandro Mercado Villalvazo
def bubble_sort(arr):
  
    # Bucle externo que recorre el arreglo
    for n in range(len(arr) - 1, 0, -1):
        
        # Inicializar una variable para verificar si se realizaron intercambios
        swapped = False  

        # Bucle interno que compara elementos adyacentes
        for i in range(n):
            if arr[i] > arr[i + 1]:
              
                # Intercambiar los elementos si están en el orden incorrecto
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                # Marcar que se realizó un intercambio
                swapped = True
        
        # Si no sucedieron intercambios en la pasada, el arreglo ya está ordenado
        if not swapped:
            break


# Lista de ejemplo para ordenar
arr = [6,6,2]
print("La lista sin ordenar es:")
print(arr)

bubble_sort(arr)

print("La lista ordenada es:")
print(arr)
