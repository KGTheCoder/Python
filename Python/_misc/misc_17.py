size = 3
window = []

def next(val: int) -> float:
    if len(window) == size:
        window.pop(0)
    window.append(val)
    return sum(window) /  size

next(1)
next(10)
next(3)
print(next(5))