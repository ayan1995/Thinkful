def prime(number):
    i = 2
    while i * i < number:
        while number % i == 0:
            number = number / i
        i = i + 1
    return number

print(prime(600851475143))
