from datetime import datetime
start = datetime.now()
#less neat in order to be faster
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
            #sieve[i*i::2*i], (start:end:step)
            #goes forward and removes all multiples of the number i 
    return [2] + [i for i in range(3,n,2) if sieve[i]]

primes1 = primes(1000000)
lis_prim = set(primes1)
for num2 in primes1:
    num2_s = str(num2)
    for ni in range(1,len(num2_s)-1):
        if int(num2_s[ni])%2==0:
            lis_prim.remove(num2)
            break
        elif int(num2_s[ni])%5==0:
            lis_prim.remove(num2)
            break

def check_left(number_c):
    if number_c in {2,3,5,7}:
        return True
    if int(str(number_c)[:-1]) in primes1:
        number_c=int(str(number_c)[:-1])
        return check_left(number_c)
    else:
        return False

def check_right(number_c):
    if number_c in {2,3,5,7}:
        return True
    if int(str(number_c)[1:]) in primes1:
        number_c=int(str(number_c)[1:])
        return check_right(number_c)   
    else:
        return False    
total=0
primes1 = list(lis_prim)
for number in primes1[4:]:
    if True == check_right(number):
        if check_left(number):
            total+=number

print(total)

print(datetime.now()-start) 