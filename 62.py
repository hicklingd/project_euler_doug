from datetime import datetime


start = datetime.now()

from collections import Counter

cubes_list = [dict(Counter(str(i ** 3))) for i in range(10000)]

for index, i in enumerate(cubes_list):
    if cubes_list.count(i) == 5:
        print((index)**3)
        break

print(datetime.now() - start)
