def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(number):
    next_number = number + 1  # Start checking from the next number
    while True:
        if is_prime(next_number):
            return next_number
        next_number += 1

# Example usage:
start_number = 11
next_prime_number = next_prime(start_number)
print("The next prime number after", start_number, "is:", next_prime_number)
