# def faktorial(n):
#     if n == 0:
#         return 1
#     return n * faktorial(n - 1)
# print(faktorial(5))

def fibonacci(n):
    if n <= 8:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))  # Natija: 8