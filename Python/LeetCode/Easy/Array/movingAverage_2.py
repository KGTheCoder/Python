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
param_1 = obj.next(4)
print(param_1)