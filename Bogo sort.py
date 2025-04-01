import random
import timeit
#compruebo si la lista esta ordenada
def is_sorted(arr):
    """Verifica si una lista está ordenada."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

#Elijo Bogo Sort para permutar aleatoriamente la lista (aunque sea ineficiente)
def bogo_sort(arr):
    """Implementación del algoritmo Bogo Sort."""
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr) #reaorganizar aleatoriamente
        attempts += 1       #contador para ver los intentos
    return arr, attempts

#pruebo quick sort que divide la lista seleccionado un pivote(mucho mas eficiente que bogo)
def quick_sort(arr):
    """Implementación del algoritmo Quick Sort."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]              #selecciona el pivote y divide la lista en tres:
    left = [x for x in arr if x < pivot]    #elementos menores que el pivote
    middle = [x for x in arr if x == pivot] #iguales al pivote
    right = [x for x in arr if x > pivot]   #mayores al pivote
    return quick_sort(left) + middle + quick_sort(right) #ordenar las sublistas y se unen con middle

def measure_time(sort_function, arr, number=1):
    """Mide el tiempo de ejecución de un algoritmo de ordenación con timeit."""
    return timeit.timeit(lambda: sort_function(arr[:]), number=number) / number

# Pra pedir la lista
user_input = input("Ingrese una lista de números separados por comas: ")
user_list = [int(x) for x in user_input.split(',')]

print("\nProbando Bogo Sort:")
if len(user_list) <= 8:  # Bogo Sort solo para listas pequeñas !!!!
    test_copy = user_list[:]
    sorted_arr, attempts = bogo_sort(test_copy)
    print(f"Lista inicial: {user_list}\nLista ordenada: {sorted_arr} (Intentos: {attempts})\n")
else:
    print("La lista es demasiado grande para Bogo Sort. Pruebe con 8 elementos o menos.\n")

print("\nProbando Quick Sort:")
test_copy = user_list[:]
exec_time = measure_time(quick_sort, test_copy, number=10)
print(f"Lista inicial: {user_list}\nLista ordenada: {quick_sort(user_list)}\nTiempo promedio: {exec_time:.6f} s\n")
