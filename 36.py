from datetime import datetime
start = datetime.now()
#only odd numbers
total = 0
for num in range(1,1000000,2):
    if str(num) == str(num)[::-1] and bin(num)[2:]==bin(num)[2:][::-1]:
        total+=num

print(total)
print(datetime.now()-start) 