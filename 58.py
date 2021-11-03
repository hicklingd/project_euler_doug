from datetime import datetime

# i would assume some optimization can be made in checking if it is a prime.
# maybe by creating them rather than checking??

# i skip bottom right corner as it will never be prime


start = datetime.now()


def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5+1),2):
            if n % i == 0:
                return False
        return True


count_side = 0
side_length = 4

numerator = 3
denominator = 5
number_c = 9
update = 0

while True:

    if count_side == 3:
        count_side = 0
        side_length += 2

        number_c += side_length + side_length - 2
        denominator += 1

    else:
        number_c += side_length
    count_side += 1

    if is_prime(number_c):
        numerator += 1

    denominator += 1

    if numerator / denominator <= 0.1:
        print(side_length + 1)
        break

print(datetime.now() - start)
