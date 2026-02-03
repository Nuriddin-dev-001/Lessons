# 1.
# def name_my(ism):
#     print(f"Salom {ism}!")
# name_my("Nuriddin")
# # 2.
# def son_yigindi(a=1, b=0):
#     print(a+b)
# son_yigindi(3,6)
#
# # 3.
# def son_kvadrat(n):
#     print(n*n)
# son_kvadrat(25,)
#
# # 4.
# def juft_toq(n):
#     if n%2==0:
#         print("Juft!")
#     else:
#         print("Toq")
# juft_toq(8)
#
# # 5.
# def max_son(list):
#     print(max(list))
# list=[]
# max_son(list)
# # 5.1
# def max_son(list):
#     max=list[0]
#     for i in list:
#         if i > max:
#             max=i
#     print(max)
# list=[1,4,8,2,9,12]
# max_son(list)
#
# # 6.
# def teskari_str(str):
#     teskari_matn = str[::-1]
#     print(teskari_matn)
# teskari_str("Salom")
#
# # 7.
# def yosh_user(int):
#     user=int(input("Tug'ilgan yilingiz :"))
#     print(2025 - user)
# yosh_user(int)
#
# # 8.
# def palindron(s):
#     if s == s[::-1]:
#         print("Palindrom!")
#     else:
#         print("Palindrom emas!")
# palindron("alla")
# palindron("salom")
#
# # 9.
# def ekub(a,b):
#     if a % 2 != 0 or b % 2 != 0:
#         print("Tub sonlar uchun ekub mavjud emas!")
#     else:
#         while b!= 0:
#             a, b = b, a % b
#         print(a)
# ekub(12, 4)
#
# # 10.
def faktorial(n):
    if n== 0 or n == 1:
        return 1
    return n*faktorial(n-1)
print(faktorial(5))