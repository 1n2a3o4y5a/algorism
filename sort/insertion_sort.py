# insertion sort


li_insertion = [2, 5, 1, 8, 7, 3]
def insertion(numbers):
    len_numbers = len(numbers)
    
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] >= temp:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = temp
    print(numbers)
        
insertion(li_insertion)