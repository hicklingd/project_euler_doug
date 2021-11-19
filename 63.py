from datetime import datetime

start = datetime.now()

count = 0

for i in range(1,10):
    power = 1
    while True:
        if power == len(str(i**power)):
            count +=1

        else:
            break
        power +=1

print(count)

print(datetime.now() - start)
