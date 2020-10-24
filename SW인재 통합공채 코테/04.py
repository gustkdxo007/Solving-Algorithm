import math
def isPrime(N):
    arr = []
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            arr.append(i)
            return i
    return 1

print(isPrime(37961921))