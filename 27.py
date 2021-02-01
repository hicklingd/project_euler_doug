from datetime import datetime
start = datetime.now()
primes=set()
def is_prime(number):
    if number in primes:
        return True
    else:
        for c_num in range(2,int((number)**0.5)):
            if number%c_num==0:
                return False
        primes.add(number)
        return True

def check(number3,a,b):
    test_1=number3**2+a*number3+b
    if test_1>0:
        return is_prime(test_1)
    else:
        return False
for i in range(2,1001):
    for num in range(2,i):
        if i%num==0:
            break
    else:
        primes.add(i)
primes_n = {-x for x in primes}
primes_t = primes|primes_n
primes_t = tuple(primes_t)
primes_s=tuple(primes)
highest_n=0
for a in primes_t:
    for b in primes_s:
        if a+b>0:
            n=0
            while check(n,a,b):
                n+=1
            if n>highest_n:
                highest_n=n
                highest_b=b
                highest_a=a
print(highest_a*highest_b)
print(datetime.now()-start)