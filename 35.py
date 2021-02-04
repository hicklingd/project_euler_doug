from datetime import datetime
start = datetime.now()

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
            #sieve[i*i::2*i], (start:end:step)
            #goes forward and removes all multiples of the number i 
    return [2] + [i for i in range(3,n,2) if sieve[i]]

lis_prim = set(primes(1000001))
lis_prim_t = tuple(lis_prim)
for num1 in lis_prim_t:
    num_s=str(num1)
    for ni in range(len(num_s)-1):
        if int(num_s[ni])%2==0 or int(num_s[ni])%5==0:
            lis_prim.remove(num1)
            break
total=0

for num in lis_prim:
    if lis_prim==500000:
        print('r')
    num_s= str(num)
    number=num_s
    n=0   
    for i in range(len(num_s)):
        num_r = number[1:]+number[0]
        number=num_r
        if int(number) in lis_prim:
            n+=1
            if n == len(num_r):
                total+=1
print(total)
print(datetime.now()-start) 