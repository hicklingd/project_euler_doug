from datetime import datetime

start = datetime.now()


def my_fn(n, d, iterations, count):

    for i in range(iterations):

        n = n + 2*d
        d = n - d

        if len(str(n)) > len(str(d)):
            count += 1

    return count


print(my_fn(3,2,1000,0))

print(datetime.now() - start)
