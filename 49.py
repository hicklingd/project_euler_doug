from datetime import datetime
start = datetime.now()

def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
            #sieve[i*i::2*i], (start:end:step)
            #goes forward and removes all multiples of the number i 
    return [2] + [i for i in range(3,n,2) if sieve[i]]

primes_l = primes(10000)
primes_l_2 = set()
for num in primes_l:
    if num>=1000:
        primes_l_2.add(num)
ar_prim = set()
abc=True
while abc == True:
    for num1 in primes_l_2:
        for gap in range(1,((10000-num1)//2)):
            if num1+gap in primes_l_2:
                if num1+2*gap in primes_l_2:
                    if sorted(str(num1))==sorted(str(num1+gap))==sorted(str(num1+2*gap)):
                        if num1==1487:
                            continue
                        print(str(num1)+str(num1+gap)+str(num1+2*gap))
                        abc=False




#max gap is 5000




print(datetime.now()-start)