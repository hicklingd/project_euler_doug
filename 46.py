from datetime import datetime
start = datetime.now()

def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5+1),2):
            if n % i == 0:
                return False
        return True

number = 3

primes = set([2,3])

while True:
    if is_prime(number):
        primes.add(number)
    else:
        for i in primes:
            if ((0.5*(number-i))**0.5)%1==0:
                break
        else:
            print(number)
            break

    number += 2



print(datetime.now()-start)