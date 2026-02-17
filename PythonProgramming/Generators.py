# Generator -- special type of functiona which will return one value a time, on demand

# yield
# Memory efficient
# Use full large state of data
# Files, retries, batching

# normal function

def num():
    return [1,2,3,4,5]
print(num())

# Using the generators
def squares(n):
    for i in range(n):
        yield i * i

res = squares(5)
print(next(res))
print(next(res))
