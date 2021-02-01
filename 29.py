total = set()
for i in range(2,101):
    for b in range(2,101):
        number=i**b
        total.add(number)
print(len(total))