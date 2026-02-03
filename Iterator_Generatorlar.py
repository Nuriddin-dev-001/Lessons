# # 17-mavzu Iterator va Generator
# l = [1,2,3,4,5]
# l_iter= iter(l)
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
#
# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# gen= my_generator()
# print(iter(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# def count_up_to(n):
#     count =1
#     while count <= n:
#         yield count
#         count += 1
#
# for num in count_up_to(5):
#     print(num)
#
# def infinite_numbers():
#     num = 1
#     while True:
#         yield num
#         num += 1
#
# gen = infinite_numbers()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# gen = fibonacci()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# gen = (x**2 for x in range(5))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# def sub_generator():
#     yield 1
#     yield 2
#     yield 3
# def main_generator():
#     yield from sub_generator()
#     yield 4
# gen = main_generator()
# print(list(gen))
#
# # 1
# l = [10, 20, 30, 40, 50]
# l_iter = iter(l)
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter)) #yana bir marta chaqirilsa StopIteration xatoligini chiqaradi
#
# # 2
# class Counter:
#     def __init__(self, max_value):
#         self.max_value = max_value
#         self.current = 1
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current > self.max_value:
#             raise StopIteration
#         value = self.current
#         self.current += 1
#         return value
# counter = Counter(10)
# for num in counter:
#     print(num)
#
# class Fibonacci: #1 dan 10 gacha sonlar fibonaccilari ketma ketligini chiqaradi.
#     def __init__(self):
#         self.a, self.b = 0, 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         value = self.a
#         self.a, self.b = self.b, self.a + self.b
#         return value
#
# fib = Fibonacci()
# for _ in range(10):
#     print(next(fib))
#
# def generator_numbers(): #1 dan 10 gacha sonlar ketma ketligini chiqaradi.
#     for i in range(11):
#         yield i
# gen = generator_numbers()
# for num in gen:
#     print(num)
#
# def square_numbers(i): #1 dan 10 gacha sonlar kvadratlari ketma ketligini chiqaradi.
#     for i in range(1, i+1):
#         yield i ** 2
# gen = square_numbers(10)
# print(list(gen))
#
# def Fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# gen = Fibonacci()
# for _ in range(10):
#     print(next(gen))
#
# def prime_generator():
#     def is_prime(number):
#         if number < 2:
#             return False
#         for i in range(2, int(number**0.5) + 1):
#             if number % i == 0:
#                 return False
#         return True
#
#     number = 2
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1
#
# primes = prime_generator()
# for _ in range(6):
#     print(next(primes))
#
