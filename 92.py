from datetime import datetime
# could be quicker to change around the if and elif statements in the is_89 function 

start = datetime.now()

def is_89(number, past_numbers, past_number_ones_set, past_number_89_set):
    past_numbers.append(number)

    number = sum([int(i)**2 for i in str(number)])
    if number == 1:
        return False, past_numbers
    elif number in past_number_ones_set:
        return False, past_numbers
    elif number == 89:
        return True, past_numbers
    elif number in past_number_89_set:
        return True, past_numbers
    else:
        return is_89(number, past_numbers, past_number_ones_set, past_number_89_set)

def ten_mill_89(n):
    sieve = [True] * n
    set_of_numbers_ones = {1}
    set_of_numbers_89 = {89}
    for i in range(n):
        if i ==0:
            sieve[0] = False
        elif sieve[i]:
            starting_number = i
            is_89_bool, list_of_numbers = is_89(starting_number, [], set_of_numbers_ones, set_of_numbers_89)
            if not is_89_bool:
                set_of_numbers_ones |= set(list_of_numbers)
                for index in list_of_numbers:
                    if index<n:
                        sieve[index] = False
            else:
                set_of_numbers_89 |= set(list_of_numbers)

    return sum(sieve)

print(ten_mill_89(10000000))



print(datetime.now() - start)
