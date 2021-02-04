from itertools import permutations
from math import factorial
import math
from datetime import datetime
start = datetime.now()
#9!=362880 so max can be assumed to be 7 digits
factorials = tuple([factorial(digit) for digit in range(10)])
sumn=0
def digits(n):
	s = 0
	while n:
		s += factorials[n%10]
		n //= 10
	return s
for number5 in range(10,100000):
    total=0 
    total = digits(number5)
    if total==number5:
        sumn+=number5
print(sumn)
print(datetime.now()-start) 