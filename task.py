import random
import timeit


def insertion_sort(lst):
  for i in range(1, len(lst)):
    key = lst[i]
    j = i-1
    while j >=0 and key < lst[j] :
      lst[j+1] = lst[j]
      j -= 1
    lst[j+1] = key 
  return lst


def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
      if left_half[i] < right_half[j]:
        arr[k] = left_half[i]
        i += 1
      else:
        arr[k] = right_half[j]
        j += 1
      k += 1

    while i < len(left_half):
      arr[k] = left_half[i]
      i += 1
      k += 1

    while j < len(right_half):
      arr[k] = right_half[j]
      j += 1
      k += 1


# Генеруємо випадкові масиви
sizes = [100, 1000, 10000]
arrays = {size: [random.randint(0, size) for _ in range(size)] for size in sizes}

# Функція для вимірювання часу
def measure_time(sort_func, arr):
  return timeit.timeit(lambda: sort_func(arr.copy()), number=10)

# Результати тестування
results = {
  'Merge Sort': {},
  'Insertion Sort': {},
  'Timsort': {}
}

for size in sizes:
  results['Merge Sort'][size] = measure_time(merge_sort, arrays[size])
  results['Insertion Sort'][size] = measure_time(insertion_sort, arrays[size])
  results['Timsort'][size] = measure_time(sorted, arrays[size])

# Вивід результатів
for algo, times in results.items():
  print(f"{algo}:")
  for size, time in times.items():
    print(f"  Size {size}: {time:.6f} seconds")
