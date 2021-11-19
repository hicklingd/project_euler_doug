from datetime import datetime
start = datetime.now()


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    return [2] + [i for i in range(3, n, 2) if sieve[i]]


index = 0
sum = 1

list_of_primes = primes(200)
while sum<1000000:
    sum*=list_of_primes[index]
    if sum < 1000000:
        last_sum = sum
    index+=1

print(last_sum)
print(datetime.now() - start)
