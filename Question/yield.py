def yieldstatement():
    yield 1
    yield 2
    yield 3

obj = yieldstatement()
print(next(obj))
print(next(obj))
print(next(obj))

def yeildLoop():
    for i in range(1, 4):
        yield i

obj = yeildLoop()
print(next(obj))
print(next(obj))
print(next(obj))

def yieldExpreiment():
    yield 1
    yield from range(10, 20)
    

obj = yieldExpreiment()
print(next(obj))
print(next(obj))
