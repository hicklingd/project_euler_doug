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

prime = primes(1000000)
breaker = True
#while breaker ==True:
'''
for num1 in range(len(prime)):
    for num2 in range(num1+length,last_num2)
'''
total_s = set()
total=0
length=0
largest = 0
lastj = len(prime)
for i in range(len(prime)):
    for j in range(i+length, lastj):
        total = sum(prime[i:j])
        if total < 1000000:
            if total in prime:
                length = j-i
                largest = total
        else:
            lastj = j+1
            break

print(largest)

'''
for prime_n in prime:

        
        if total+prime_n<1000000:
            total+=prime_n
            total_s.add(total)
            if len(total_s)>highest_length and total in prime:
                highest_length = len(total_s)
                highest=total
        while total+prime_n>1000000:
        
highest_length = len(total_s)
'''

'''
highest_prime = 0
total_s = [] 
total=0
#work it out once then minus smallest prime from all numbers next time
for i in range(300):
    for prime_n in prime[i:]:
        total+=prime_n
        if total<1000000:
            total_s.append(total)
    for num3 in total_s[::-1]:
        if num3 in prime and i>highest_prime:
            highest_prime = num3 
            break
'''

print(datetime.now()-start)