from datetime import datetime
import itertools

# 13 5197 5701 6733

# five numbers need to work with five numbers
# lots of optimization to be done here!!!

# need to somehow record which ones dont work together

# each step we only need to compare the new combinations

# could create a recursive function

start = datetime.now()


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5 + 1), 2):
            if n % i == 0:
                return False
        return True


limit = 9999
list_of_primes = primes(limit)

list_of_primes_str = [str(i) for i in list_of_primes]
set_of_primes_str = {str(i) for i in list_of_primes}


# def two_concatinated_prime(num1, num2):
#     num_12 = num1 + num2
#     num_21 = num2 + num1
#     if int(num_21) < limit and int(num_12) < limit:
#         return {num_12, num_21}.issubset(set_of_primes_str)
#     else:
#         return is_prime(int(num_12)) and is_prime(int(num_21))


# this is quicker than above
def two_concatinated_prime(num1, num2):
    return is_prime(int(num1 + num2)) and is_prime(int(num2 + num1))

def finder_fn(list_of_primes_str):

    for count_1, prime_1 in enumerate(list_of_primes_str):

        for count_2, prime_2 in enumerate(list_of_primes_str[count_1 + 1:]):

            if two_concatinated_prime(prime_1, prime_2):
                count_2_t = count_1 + count_2 + 1
                for count_3, prime_3 in enumerate(list_of_primes_str[count_2_t:]):
                    testing_1 = [[prime_3, prime_1], [prime_3, prime_2]]


                    if all([two_concatinated_prime(x[0], x[1]) for x in testing_1]):

                        count_3_t = count_2_t + count_3
                        for count_4, prime_4 in enumerate(list_of_primes_str[count_3_t:]):

                            testing_2 = [[prime_4, prime_1], [prime_4, prime_2], [prime_4, prime_3]]


                            if all([two_concatinated_prime(y[0], y[1]) for y in testing_2]):

                                count_4_t = count_3_t + count_4
                                for count_5, prime_5 in enumerate(
                                        list_of_primes_str[count_4_t:]):

                                    testing_3 = [[prime_5,prime_1], [prime_5,prime_2], [prime_5,prime_3], [prime_5,prime_4]]

                                    if all([two_concatinated_prime(z[0], z[1]) for z in testing_3]):

                                        return int(prime_1) + int(prime_2) + int(prime_3) + int(prime_4) + int(prime_5)

print(finder_fn(list_of_primes_str))

print(datetime.now() - start)
