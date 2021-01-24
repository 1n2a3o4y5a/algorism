# merge sort  O(n log n)


li_merge = [2, 5, 1, 8, 7, 3]

def merge(numbers):
    if len(numbers) <= 1:
        return numbers
    
    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]
    merge(left)
    merge(right)
    
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j] :
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1
    
    return numbers
    
merge(li_merge)