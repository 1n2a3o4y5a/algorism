# buble sort O(n^2)

li_buble = [2, 5, 1, 8, 7, 3]


def buble(numbers):
    len_numbers = len(numbers)
    
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                
    return numbers

buble(li_buble)