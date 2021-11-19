from datetime import datetime
from math import gcd
start = datetime.now()


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount


def evens(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n

    sieve[1::2] = [False] * len(sieve[::2])

    return [i for i in range(2, n) if sieve[i]]

highest_critical = 0
target_n = 0
for even in evens(100000):
    phi_number = phi(even)


    critical_value = even/phi_number
    if critical_value > highest_critical:
        target_n = even
        highest_critical = critical_value

print(highest_critical)
print(target_n)


print(datetime.now() - start)
