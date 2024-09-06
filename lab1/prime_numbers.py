def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(a, b):
    if a > b:
        a, b = b, a
    primes = [num for num in range(a, b + 1) if is_prime(num)]
    return primes

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

primes = find_primes(a, b)
print(f"Прості числа між {a} та {b}: {primes}")
