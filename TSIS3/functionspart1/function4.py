def is_prime(n):
    if n == 1:
        return True
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Лист простых чисел:", prime_numbers)