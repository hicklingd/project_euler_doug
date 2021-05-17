'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''
from datetime import datetime
start = datetime.now()
from itertools import permutations
# cant be final digit
# iterate over diffferent sized numbers and different sized fixed numbers.
def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
            #sieve[i*i::2*i], (start:end:step)
            #goes forward and removes all multiples of the number i 
    return [2] + [i for i in range(3,n,2) if sieve[i]]

prime_list = primes(10000000)
#three or more repeated digits
primes_list_3 = [num for num in prime_list if (len(str(num))-len(set(str(num)))) >=3]

def family(number_22):
    num_2=str(number_22)
    num_22 = list(num_2)
    d_num_22 = list(set(num_22))
    for i in d_num_22:
        num_22_n = num_22
        num_22_n.remove(i)
    to_9 = ['0','1','2','3','4','5','6','7','8','9']
    num_perm = []
    for num_d in num_22_n:
        num_perm.append([num_2.replace(num_d,i) for i in to_9])
    return num_perm
checked = set()

def primes_c(list_num):
    for list_n in list_num:
        list_prime_c = [num_12 for num_12 in list_n if int(num_12) in prime_list]
        for num_c in list_prime_c:
            checked.add(int(num_c))
        if len(list_prime_c)>7:
            return(list_prime_c[0])
breaker=0
n=150
while breaker ==0:
    number_1 = primes_list_3[n]
    if number_1 not in checked:
        print(number_1)
        families = family(number_1)
        result= primes_c(families)
        if result:
            print(result)
            breaker=1
    #print(checked)
    n+=1


print(datetime.now()-start)