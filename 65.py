from datetime import datetime
from fractions import Fraction


start = datetime.now()
total = 0
final_number = Fraction(0,1)
for i in range(1,47):
    denominator = 1
    for num in range(1,i+1):
        denominator *= num
    fraction_temp = Fraction(1,denominator)
    final_number = final_number+fraction_temp

print(sum([int(i) for i in str(final_number.numerator)]))


# or

e = [2,]

i = 1

while len(e) < 100:
    e.extend([1, 2*i, 1])
    i += 1

numerator = 1

denominator = e.pop()

for i in e[::-1]:
    denominator, numerator = (denominator * i + numerator, denominator)


print(sum([int(digit) for digit in str(denominator)]))


print(datetime.now() - start)
