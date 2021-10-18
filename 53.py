from datetime import datetime
import math

start = datetime.now()


# combinations are symmetric so we can work from there


def combinations_fn(n, r):
    comb = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

    return comb

count = 0

for n in range(23,101):
    for r in range(1,n):
        if combinations_fn(n,r) > 1000000:
            count+=1

print(count)

print(datetime.now() - start)
