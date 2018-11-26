import time

def fib(n):
    # assume n is a non negative integer
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# test cases
print(fib(0), fib(1), fib(5), fib(9), fib(11))

# use wrapper function that times functions or use generators
def time_fun(n, fun):
    start = time.time()
    fun(n)
    return time.time() - start

print('time for fib(30): ' + str(time_fun(30, fib)))

def dpfib(n):
    # yet again assume n is a non negative integer
    cache = []
    cache.append(0)
    cache.append(1)
    for i in range(n - 1):
        cache.append(cache[-1] + cache[-2])
    return cache[n] 

print(dpfib(0), dpfib(1), dpfib(5), dpfib(9), dpfib(11))
print('dpfib(100): ' + str(dpfib(100)))
print('time for dpfib(30): ' + str(time_fun(30, dpfib)))
print('time for dpfib(1000): ' + str(time_fun(1000, dpfib)))
