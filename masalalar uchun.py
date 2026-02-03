# g=[1,2,3,4,5,6,7,8,9]
#
#
# print(f"""
#              {g[0]} | {g[1]} | {g[2]}
#             ---+---+---
#              {g[3]} | {g[4]} | {g[5]}
#             ---+---+---
#              {g[6]} | {g[7]} | {g[8]}
# """
#       )
# while True:
#     x=int(input("X sizning navbatingiz X="))
#     g[x-1]='X'
#     print(f"""
#                  {g[0]} | {g[1]} | {g[2]}
#                 ---+---+---
#                  {g[3]} | {g[4]} | {g[5]}
#                 ---+---+---
#                  {g[6]} | {g[7]} | {g[8]}
#     """
#           )
#     if (g[0]==g[1] and g[1]==g[2] or g[3]==g[4] and g[4]==g[5] or g[6]==g[7] and
#             g[7]==g[8] or g[0]==g[3] and g[3]==g[6] or g[1]==g[4] and g[4]==g[7]
#             or g[2]==g[5] and g[5]==g[8] or g[0]==g[4] and g[4]==g[8] or
#             g[2]==g[4] and g[4]==g[6]):
#         print('X Tabriklaymiz siz yutdingiz!')
#         break
#     O = int(input("O sizning navbatingiz O="))
#     g[O - 1] = 'O'
#     print(f"""
#                      {g[0]} | {g[1]} | {g[2]}
#                     ---+---+---
#                      {g[3]} | {g[4]} | {g[5]}
#                     ---+---+---
#                      {g[6]} | {g[7]} | {g[8]}
#         """
#           )
#     if (g[0] == g[1] and g[1] == g[2] or g[3] == g[4] and g[4] == g[5] or g[6] == g[7] and
#             g[7] == g[8] or g[0] == g[3] and g[3] == g[6] or g[1] == g[4] and g[4] == g[7]
#             or g[2] == g[5] and g[5] == g[8] or g[0] == g[4] and g[4] == g[8] or
#             g[2] == g[4] and g[4] == g[6]):
#         print('O Tabriklaymiz siz yutdingiz!')
#         break

# # Foydalanuvchidan son kiritish
# num = int(input("Sonni kiriting: "))
#
# # Yig‘indi o‘zgaruvchisi
# sum_digits = 0
#
# # Sonning raqamlari tugaguncha davom etadi
# while num > 0:
#     last_digit = num % 10  # Oxirgi raqamni olish
#     sum_digits += last_digit  # Yig‘indiga qo‘shish
#     num //= 10  # Sonni 10 ga bo‘lib, oxirgi raqamni olib tashlash
#
# # Natijani chiqarish
# print("Raqamlar yig‘indisi:", sum_digits)

# num = int(input("Sonni kriting : "))
# sum_digits = 0
# while num > 0:
#     last_digit = num % 10
#     sum_digits += last_digit
#     num //= 10
# print("raqamlar yig'indisi:", sum_digits)
#
# color = ""
#
# while color not in ["qizil", "sariq", "yashil"]:
#     color=input("Svetafor rangini kriting :").lower()
#     if color in ["qizil", "sariq", "yashil"]:
#         print("Raxmat to'g'ri keladi!")
#         break
#     else:
#         print("Xato qayta urining.")

login = "admin"
parol = "1234"
yosh = "21"
def login_print(l, p, y):
    print(f"""
    __________________________
    |                        |
    | login: {l}           |
    | parol: {p}            |
    | yosh: {y}               |
    |                        |
    --------------------------
    """)
login_print(login, parol, yosh)

