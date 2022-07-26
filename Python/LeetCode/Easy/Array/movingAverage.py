class MovingAverage:
    """
    def __init__(self, size: int):
        self.size = size
        self.queue = []
    
    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)
    """
    def __init__(self, size: int):
        self.array = []
        self.size = size
    
    def next(self, val: int) -> float:
        self.array.append(val)
        return sum(self.array[-self.size:]) / min(len(self.array), self.size)

MA = MovingAverage(3)
print(MA.next(1))
print(MA.next(10))
print(MA.next(3))
print(MA.next(5))


