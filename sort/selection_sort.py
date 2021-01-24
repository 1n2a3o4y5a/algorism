# selection sort O(n^2)


li_selection = [2, 5, 1, 8, 7, 3]
def selection(numbers: li):
    len_numbers = len(numbers)
    
    for i in range(len_numbers):
        mini_index = i
        for j in range(i + 1, len_numbers):
            if numbers[j] < numbers[mini_index]:
                mini_index = j
        numbers[i], numbers[mini_index] = numbers[mini_index], numbers[i]
        
    print(numbers)
    
selection(li_selection)