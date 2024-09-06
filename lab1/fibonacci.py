def fib(k):
    if k <= 0:
        return []
    elif k == 1:
        return [0]
    elif k == 2:
        return [0, 1]
    else:
        fib_seq = fib(k - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

k = int(input("Введіть кількість чисел Фібоначчі: "))

fibonacci_numbers = fib(k)
print(f"{k} чисел Фібоначчі: {fibonacci_numbers}")
