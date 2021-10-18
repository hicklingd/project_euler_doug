from collections import Counter
from datetime import datetime

# got to be less than 1/6, one has to be a multiple of 6,5,4,3,2

start = datetime.now()

i = 1

while True:
    i += 1
    if len(str(i)) == len(str(i * 6)):
        if Counter(str(i * 2)) == Counter(str(i)):
            if Counter(str(i * 3)) == Counter(str(i)):
                if Counter(str(i * 4)) == Counter(str(i)):
                    if Counter(str(i * 5)) == Counter(str(i)):
                        if Counter(str(i * 6)) == Counter(str(i)):
                            print(i)
                            break

print(datetime.now() - start)
