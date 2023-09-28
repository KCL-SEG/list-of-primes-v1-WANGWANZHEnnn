"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

#def primes(number_of_primes):
#    list = []
#    return list

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        return []

    prime_list = []
    num = 2  # Start with the first prime number, 2

    while len(prime_list) < number_of_primes:
        if is_prime(num):
            prime_list.append(num)
        num += 1

    return prime_list

# Example usage:
result = primes(10)
print(result)  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
