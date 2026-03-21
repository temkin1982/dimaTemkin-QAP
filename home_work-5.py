def generator(n):
    for i in range(n+1):
        pass
        yield i

obj_gen = generator(10)

while True:
    try:
        print(next(obj_gen))
    except StopIteration:
        break    