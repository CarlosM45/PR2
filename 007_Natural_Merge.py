# Carlos Alejandro Mercado Villalvazo
my_list = [-1, -5, -40, 100, 589, 27, -95]# Inicializando la lista
 
def merge_runs(left, right):# Función para fusionar dos listas ordenadas
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])# Añadiendo el resto de 'left' a la lista 'merged'
    merged.extend(right[j:])# Añadiendo el resto de 'right' a la lista 'merged'
    return merged
 
def natural_merge_sort(my_list):
    if len(my_list) <= 1:# Verificando si la lista ya está ordenada
        return my_list
    runs = []
    start = 0
    end = 1
    while end < len(my_list):# Localizando las corridas naturales
        if my_list[end] < my_list[end-1]:
            runs.append(my_list[start:end])
            start = end
        end += 1
    runs.append(my_list[start:end])
    while len(runs) > 1:# Combinando las corridas naturales
        merged_runs = []
        i = 0
        while i < len(runs)-1:
            merged_runs.append(merge_runs(runs[i], runs[i+1]))
            i += 2
        if len(runs) % 2 == 1:
            merged_runs.append(runs[-1])
        runs = merged_runs
    return runs[0]
 
print(natural_merge_sort(my_list))
