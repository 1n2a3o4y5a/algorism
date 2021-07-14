import sys

class MiniHeep(object):

    def __init__(self) -> None:
        self.heep = [-1 * sys.maxsize]
        self.current_size = 0

    def parent_index(self, index: int) -> int:
        return index // 2
    
    def left_child_index(self, index: int) -> int:
        return index * 2
    
    def right_child_index(self, index: int) -> int:
        return (index * 2) * 1
    
    def swap(self, index1 : int, index2: int) -> None:
        self.heep[index1], self.heep[index2] = self.heep[index2], self.heep[index1]

    def heepfy_up(self, index: int) -> None:
        while self.parent_index(index) > 0:
            if self.heep[index] < self.heep[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)
    
    def push(self, value: int) -> None:
        self.heep.append(value)
        self.current_size += 1
        self.heepfy_up(self.current_size)