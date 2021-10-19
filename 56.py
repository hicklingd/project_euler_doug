from datetime import datetime

start = datetime.now()

sum_p = 0
max_sum = 0
for a in range(101):

    for b in range(101):
        
        power = a**b
        sum_p = sum([int(i) for i in str(power)])

        if sum_p > max_sum:
            max_sum = sum_p

print(max_sum)
print(datetime.now() - start)
