def pairSumSequence(n):
    sum = 0
    for x in sum:
        sum += pairSum(x, x+1)

def pairSum(a, b):
    return a + b

print(pairSumSequence(3))

