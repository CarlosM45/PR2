# Carlos Alejandro Mercado Villalvazo
def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # Los elementos ordenados se guardarán en output[]
    output = [0] * (n) 
  
    # Inicializar el conteo de ocurrencias
    count = [0] * (10) 
  
    # Almacenar el conteo de ocurrencias de los dígitos
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
  
    # Cambiar count[i] para que count[i] contenga la posición real de este dígito en output[]
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Construir el arreglo de salida
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
  
    # Copiar el arreglo de salida a arr[], para que arr[] ahora contenga los números ordenados según el dígito actual
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 

# Método para Radix Sort
def radixSort(arr):

    # Encontrar el valor máximo para saber el número de dígitos
    max1 = max(arr)

    # Hacer un conteo de dígitos para cada posición
    exp = 1
    while max1 // exp > 0:
        countingSort(arr,exp)
        exp *= 10

# Código de prueba
arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)

for i in range(len(arr)):
    print(arr[i],end=" ")
