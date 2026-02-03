# # 1. List Comprehension
# # Masalalar:
# #1. 1 dan 20 gacha bo‘lgan juft sonlardan iborat ro‘yxat yarating.
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print([i for i in l if i%2==0])

# 2. Berilgan ro‘yxatdagi har bir so‘zning uzunligini hisoblab,
# yangi ro‘yxat hosil qiling.
l=[]
# 3. 1 dan 50 gacha bo‘lgan sonlar ichidan 3 ga karralilarining kvadratlarini
# toping.
#
# 2. Lambda
# Masalalar:
#
# 1. Ikki sonning ko‘paytmasini hisoblovchi lambda funksiyasini yozing.
# 2. Berilgan sonning toq yoki juftligini qaytaruvchi lambda funksiya yarating.
# 3. So‘z uzunligini qaytaruvchi lambda funksiya yozing.
#
# 3. Map
# Masalalar:
#
# 1. Berilgan ro‘yxatdagi sonlarni kvadratga oshiring.
# 2. Berilgan ro‘yxatdagi harflarni katta harfga aylantiring.
# 3. Berilgan ro‘yxatdagi barcha sonlarni 2 barobar oshiring.
#
# 4. Reduce
# Masalalar:
#
# 1. Berilgan ro‘yxatdagi barcha sonlarning ko‘paytmasini hisoblang.
# 2. Berilgan ro‘yxatdagi eng katta sonni toping.
# 3. Berilgan ro‘yxatdagi so‘zlarni bitta matnga birlashtiring.
#
# 5. Filter
#
# Masalalar:
#
# 1. Ro‘yxatdan faqat juft sonlarni ajratib oling.
# 2. Ro‘yxatdan uzunligi 5 ta belgidan uzun so‘zlarni tanlang.
# 3. Ro‘yxatdan musbat sonlarni ajratib oling.
# oling
# #
# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b,ab
#
# fibonacci = fibonacci_generator()
# for _ in range(10):
#     print(next(fibonacci))
##print("Besh ikkidan katta")
# x = 5
# y = "Salom dunyo"
# print(x,y)
# x = 5
# y = "Python"
# print(x,y)
#print(y)
def fibonacci_fast(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(fibonacci_fast(62))