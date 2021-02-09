from itertools import permutations
from datetime import datetime
start = datetime.now()


# we know that a number is divisible by three if the sum of its digits
# is divisible by three, so terefore 7 is the highest we can go to

def check_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            return False
    return True

largest = 0
comb1 = permutations('1234567')
for num in list(comb1)[::-1]:
    if int(num[-1])%2!=0:
        number1 = int(''.join(num))
        if check_prime(number1):
            print(number1)
            break

print(datetime.now()-start) 