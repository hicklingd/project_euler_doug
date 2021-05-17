from datetime import datetime
start = datetime.now()
total=0
for i in range(1,1000):
    total+=i**i

print(str(total)[-10:])
print(datetime.now()-start)