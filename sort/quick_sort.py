# quick sort O(n log n)

li_quick = [2, 5, 1, 8, 7, 3]

def partition(numbers, low, high):
    i = low -1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
            
    numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]
    return i + 1

def quick(numbers):
    def inner_quick(numbers, low, high):
        if low < high:
            partition_index = partition(numbers, low, high)
            inner_quick(numbers, low, partition_index - 1)
            inner_quick(numbers, partition_index + 1, high)
            
    inner_quick(numbers, 0, len(numbers) - 1)
    
quick(li_quick)