# Memoization, top-down dynamic programming

cache = {}

def fib(n):
    if n <= 1:
        return n

    if n not in cache: # if n is not a key in the cache, then add it
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]
   

for i in range(100):
    print(f'{i:3} {fib(i)}')

# Two argument memoization
# def expensive_function(x,y):

#     key = (x,y)

#     if key not in cache: # if n is not a key in the cache
#         cache[key] = whatever_expensive_thing_here()

#     return cache[key]