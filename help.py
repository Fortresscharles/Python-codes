class MemoryManager:
    def __init__(self, size):
        self.size = size
        self.memory = [None] * size
        self.free_list = []

    def allocate(self, process):
        size = process.size
        if len(self.free_list) == 0:
            # No free space, cannot allocate
            return False
        else:
            # Find the first available pocket of empty space that is large enough to fit the process
            for pocket in self.free_list:
                if pocket[1] >= size:
                    # Allocate the process in the pocket
                    start = pocket[0]
                    end = start + size
                    for i in range(start, end):
                        self.memory[i] = process
                    # Update the free list
                    self.free_list.remove(pocket)
                    if end < pocket[1]:
                        self.free_list.append((end, pocket[1] - size))
                    return True
            # No suitable pocket found, cannot allocate
            return False

    def deallocate(self, process):
        start = None
        end = None
        for i in range(len(self.memory)):
            if self.memory[i] == process:
                if start is None:
                    start = i
                end = i + 1
            elif start is not None:
                break
        if start is not None:
            # Deallocate the process
            for i in range(start, end):
                self.memory[i] = None
            # Update the free list
            self.free_list.append((start, end - start))
            self.free_list = sorted(self.free_list, key=lambda x: x[0])
            # Compact the free spaces
            self.compact()

    def compact(self):
        new_free_list = []
        current_start = None
        current_end = None
        for pocket in self.free_list:
            if current_start is None:
                current_start = pocket[0]
                current_end = pocket[0] + pocket[1]
            elif pocket[0] == current_end:
                current_end += pocket[1]
            else:
                new_free_list.append((current_start, current_end - current_start))
                current_start = pocket[0]
                current_end = pocket[0] + pocket[1]
        new_free_list.append((current_start, current_end - current_start))
        self.free_list = new_free_list
