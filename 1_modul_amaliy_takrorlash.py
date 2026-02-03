# # 1.1
# user = input("Ismingiz ")
# print(user[:: -1])
# # 1.2
# matn = input("So'z kiriting ")
# print(matn.title())
# # 2.1
# num = [1,2,3,4,5,6,7,8,9]
# juft = [n for n in num if n % 2==0]
# print(juft)
# # 2.2
# num = [12,34,43,3,67,33,17,93]
# print(max(num),min(num))
# # 2.3
# num = [1,2,2,3,4,5,5,6,7,7,8,9,9,]
# print(list(set(num)))
# # 3.1
# students = {"Ali": 75, "Vali": 55, "Sami": 90}
# natija = {key:("0'tdi" if value >=60 else "O'tolmadi") for key,value in students.items()}
# print(natija)
# # 3.2
# students = {"Ali": 75, "Vali": 55, "Sami": 90}
# ball = list(students.values())
# ball.sort(reverse=True)
# print(ball[:2])
# # 3.3
# students = {"Ali": 75, "Vali": 55, "Sami": 90}
# ism =input("Ism kiriting :")
# print("Bor"if ism in students else "Yo'q" )
# # 4.1
# num = int(input("Son kiriting: "))
# print("Musbat"if num % 2==0 else "Manfiy")
# # 4.2
# for i in range(1, 101):
#     if i % 3==0 and i % 5==0:
#         print(i)
# # 4.3
# parol = "1234"
# while True:
#     p = input("Parolni kriting :")
#     if p==parol:
#         break
# print("Xush kelibsiz!")
# # 5.1
# numbers = [n for n in range(1, 21)if n % 2!=0]
# print(numbers)
# # 5.2
# text = "hello"
# print([s for s in text])
# # 5.3
# print([n*n for n in [1,2,3,4]])
# # 6.1
# num = lambda a,b:a*b
# print(num(3,5))
# # 6.2
# nums = [1,2,3,4]
# print(list(map(lambda n:n*2,nums)))
# # 6.3
# from functools import reduce
# nums = [1, 2, 3, 4, 5, 6]
# print(reduce(lambda x,y:x*y,nums))
# # 7.1
# a, b = 0, 1
# for _ in range(64):
#     print(a,)
#     a, b = b, a + b
# # 7.2
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1)+fib(n-2)
# print([fib(i)for i in range(10)])
# # 7.3
def fact(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
print(fact(10))
# # 7.4
# def fact(n):
#     if n == 0:
#         return 1
#     return n = n-1 *2
# print(fact(10))
# 8.1










