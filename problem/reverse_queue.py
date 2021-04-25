from collections import deque

def reverse(queue):
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())
    return new_queue   