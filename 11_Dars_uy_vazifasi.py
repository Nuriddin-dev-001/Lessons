# # while siki
# # 1.
# ranglar = ["qizil", "sariq", "yashil"]
#
# while True:
#      rang = input("Svetofor ranglarini kiriting: ")
#      if rang in ranglar:
#          print(f"Rahmat, to'g'ri keladi: {rang}")
#          break
#      else:
#          print("Xato, qaytadan kitiring")

# # 2.
# import random
#
# son = random.randint(1, 10)
#
# while True:
#     taxminson = int(input("1 dan 10 gacha bo'lgan sonni toping: "))
#
#     if son == taxminson:
#         print("Tabriklaymiz, siz topdingiz!")
#         break
#     else:
#         print("Noto'g'ri, qayta urinib ko'ring!")
#
# # 3.
# dostlar = []
#
# while True:
#     ism = input("Do'stlaringizning ismini kiriting: ")
#
#     if ism.lower() == "stop":
#         break
#     dostlar.append(ism)
#
# print("Do'stlaringiz:")
# for ism in dostlar:
#     print(ism)

# # 4.
# kurs = 12600
#
# while True:
#
#     summa = input("So'm miqdorini kiriting (stop deb yozsangiz dastur to'xtaydi): ")
#
#     if summa.lower() == "stop":
#         print("Dastur to'xtatildi.")
#         break
#     try:
#         summa = float(summa)
#
#         dollar = summa / kurs
#         print(f"{summa} so'm = {dollar:.2f} dollar")
#     except ValueError:
#         print("Iltimos, to'g'ri raqam kiriting.")

