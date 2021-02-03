from itertools import permutations
from math import factorial
from datetime import datetime
start = datetime.now()
#9!=362880 so max can be assumed to be 7 digits
factorials = tuple([factorial(digit) for digit in range(10)])
sumn=0
for number5 in range(10,2177280):
    total=0
    number5_s = [int(nu) for nu in str(number5)]
    for digit in number5_s:
        total+=factorials[digit]
    if total==number5:
        sumn+=number5
print(sumn)
print(datetime.now()-start) 