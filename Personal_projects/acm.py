import math

n = 5
m = 1

def is_prime(n):
    if(n == 1):
        return False
    if(n==2):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def count_sums(n):
    count = 0

    a = 2
    b = n - a

    if (is_prime(b)):
        count += 1

    for a in range(3, int(n/2 + 1), 2):
        b = n - a
        if (is_prime(a) and is_prime(b)):
            count += 1

    return count


'''
number = 0

while n > 0:
    number += 2
    if (count_sums(number) == m):
        n -= 1
'''

for i in range(2, 101, 2):
    print(str(i) + ' : ' + str(count_sums(i)))