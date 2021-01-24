# binary_search


li = [2, 5, 1, 8, 7, 3]
li.sort()

def binary_search(nums, value):
    left, right = 0, len(nums) - 1

    while right >= left:
        mid = (right + left) // 2
        
        if nums[mid] == value:
            return mid
        elif nums[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return -1

binary_search(li, 5)