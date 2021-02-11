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

primes1 = primes(700)

def is_product(number,prime_f):
    if number ==1 and len(prime_f)==4:
        return True
    while number!=1:
        for num1 in primes1:
            if number%num1==0:
                prime_f.add(num1)
                return is_product(number//num1, prime_f)
        else:
            return False


number1=210
count=0

while True:
    if is_product(number1,set())==True:
        number1+=1
        count+=1
        if count==4:
            print(number1-4)
            break
    else:
        number1+=1
        count=0



print(datetime.now()-start)