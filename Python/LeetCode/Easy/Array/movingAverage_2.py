class MovingAverage:
    
    def __init__(self, size: int):
        self.windowSize = size
        self.window = []
    
    def next(self, val: int) -> float:
        if len(self.window) == self.windowSize:
            self.window.pop(0)
        self.window.append(val)
        return sum(self.window) / len(self.window)

obj = MovingAverage(3)
param_1 = obj.next(1)
param_1 = obj.next(10)
param_1 = obj.next(3)
param_1 = obj.next(5)
print(param_1)