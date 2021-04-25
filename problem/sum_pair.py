#数字のペアの和が任意の数になるもの

def get_pair(numbers, target):
    cache = []
    for num in numbers:
        cache.append(num)
        val = target - num
        if val in cache:
            return (val, num)


def get_pair_half(numbers):
    sum_numbers = sum(numbers)
    if sum_numbers % 2 == 0:
        return
    half_sum = int(sum_numbers / 2)

    cache = []
    for num in numbers:
        cache.append(num)
        val = half_sum - num 
        if val in cache:
            return (val, num)

