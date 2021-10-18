from datetime import datetime

start = datetime.now()


def is_palindrome(number, iteration, list_tried):
    iteration += 1

    number = number + int(str(number)[::-1])

    if str(number) == str(number)[::-1]:
        return list_tried
    elif iteration == 50:
        return []
    else:
        if number < 10000:
            list_tried.append(number)
        return is_palindrome(number, iteration, list_tried)


def lychrel(n):
    sieve = [True] * n
    for i in range(n):

        if sieve[i]:
            starting_number = i
            list_of_non_lychrel = is_palindrome(starting_number, 0, [starting_number])
            for index in list_of_non_lychrel:
                sieve[index] = False

    return [i for i in range(n) if sieve[i]]


print(len(lychrel(10000)))

print(datetime.now() - start)
