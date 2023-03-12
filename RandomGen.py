import random

def generate_random_numbers(n, start, end):
    return [random.randint(start, end) for _ in range(n)]

print(generate_random_numbers(10, 1, 100))
