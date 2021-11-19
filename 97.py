# takes a long time but i cant be bothered to optimise at the moment

from datetime import datetime

start = datetime.now()

num = 28433*(2**7830457)+1


print(str(num)[-10:])

print(datetime.now() - start)