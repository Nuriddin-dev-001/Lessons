# 1.1
# user=input("so`z kriting ;")
# user2=user[0:4]
# print(user2)
# 1.2
user = input("Sonlar kiriting : ")
sonlar = list(map(int, user.split()))

juft_sonlar = []
for son in sonlar:
    if son % 2 == 0:
        juft_sonlar.append(son)

print(juft_sonlar)
# 1.3
# user=input("so`z kriting")
# s="".join(reversed(user))
# print(s)
# 1.4
# x=[1,2,3,4,5,6,7]
# x2=x[4:8]
# print(x2)
# 1.5
# user=input("matn kriting :")
# user2="  ".join(user)
# print(user2)
#
# 2.1
# age=int(input("yoshingiz :"))
# if age >=18:
#     print("Siz balog'at yoshidasiz!")
# else:
#     print("Siz hali voyaga yetmagansiz")
# 2.2
# num=int(input("son kriting :"))
# if num > 0:
#     print("Musbat")
# elif num == 0:
#     print("Nolga teng")
# else:
#     print("Manfiy")
# 2.3
# a=int(input("son kriting"))
# b=int(input("son kriting"))
# if a<b:
#     print(f"{b} Katta")
# elif b<a:
#     print(f"{a} Katta")
# else:
#     print("Ikkalasi teng")
# 2.4
# kun=int(input("Hafta kun raqami :"))
# if kun == 1:
#     print("Dushanba")
# elif kun == 2:
#     print("Seshanba")
# elif kun == 3:
#     print("Chorshanba")
# elif kun == 4:
#     print("Payshanba")
# elif kun == 5:
#     print("Juma")
# elif kun == 6:
#     print("Shanba")
# elif kun == 7:
#     print("Yakshanba")
# else:
#     print("Unday hafta kuni yo'q")
# 2.5
# user=input("Parol kriting :")
# if user == "qwer":
#     print("Xush kelibsiz!")
# else:
#     print("Parol noto'g'ri")
#
# 3.1
# user=int(input("Son kriting :"))
# if user > 10 or user < -5:
#     print("Maqbul diapazondan tashqarida")
# else:
#     print("Maqbul diapazon ichida")
# 3.2
# user1=int(input("Son kriting :"))
# user2=int(input("Son kriting :"))
# user3=int(input("Son kriting :"))
# if user1>0 and user2>0 and user3>0:
#     print("Barcha son musbat!")
# else:
#     print("False")
# 3.3
# user=input("Ismingiz :")
# if user == "Ali" or user == "Vali":
#     print("Salom do'stim!")
# else:
#     print("Biz tanish emasmiz")
# 3.4
# user=input("Pythonga doir matn kriting :")
# if " python " in user:
#     print("Bu matn pyhon bilan bog'liq")
# else:
#     print("Pythonga aloqasi yo'q")
# 3.5
# user=input("Telefon raqamingizni kriting :")
# if "998" in user:
#     print("O'zbekiston raqami")
# else:
#     print("Boshqa davlatga tegishli raqam")
#
# qiziqish=input("Nimaga qiziqasiz :").lover()
# if "kitob" in qiziqish:
#     janr=input("Sizga qaysi janrdagi kitoblar yoqadi?")
#     if "diniy" in janr:
#         print("Sizga 'Hadis va hayot' kitoblar to'plamini sovg'a qilamiz!")
#     elif "detektiv" in janr:
#         print("Sizga 'Shaytanat' kitobini sovg'a qilamiz!")
# elif "sport" in qiziqish:
#     tur=input("Sizga qaysi sport turi yoqadi?")
#     if "futbol" in tur:
#         club=input("Qaysi clubga muhlislik qilasiz?")
#         if "real" in club or "barsa" in club:
#             print("Sizga elclassicoga chipta sovg'a qilamiz!")


# qiziqish = input("Nimaga qiziqasiz: ").lower()
# if "kitob" in qiziqish:
#     janr = input("Sizga qaysi janrdagi kitoblar yoqadi? ").lower()
#     if "diniy" in janr:
#         print("Sizga 'Hadis va hayot' kitoblar to'plamini sovg'a qilamiz!")
#     elif "detektiv" in janr:
#         print("Sizga 'Shaytanat' kitobini sovg'a qilamiz!")
#     else:
#         print("Sizga qiziq bo'lishi mumkin bo'lgan turli kitoblarimiz bor!")
# elif "sport" in qiziqish:
#     tur = input("Sizga qaysi sport turi yoqadi? ").lower()
#     if "futbol" in tur:
#         club = input("Qaysi klubga muhlislik qilasiz? ").lower()
#         if "real" in club or "barsa" in club or "barcelona" in club:
#             print("Sizga El Clasico o'yiniga chipta sovg'a qilamiz!")
# # else larni GPT maslahat berdi tepani o'zim yozdim
#         else:
#             print("Sizga sevimli jamoangizning maxsus sovg'asini beramiz!")
#     else:
#         print("Sizning sportga qiziqishingiz biz uchun qiziq, sovg'a tayyorlaymiz!")
# else:
#     print("Ajoyib! Sizning qiziqishingizni bilish biz uchun muhim!")

# user = ["Doe","Jon","Ali"]
# password = "qwer"
#
# while True:
#     ism = input("ismingiz: ")
#     parol = input("parol: ")
#
#     if ism in user and parol == password:
#          print("Xush kelibsiz")
#          break
#     else:
#          print("xato qayta urining")
def my_is_digit(my_str):
    sanoq = 0
    s = 0
    for i in my_str:
        if i.isdigit():
            sanoq += 1
            s += int(i)

    return sanoq,s

print(my_is_digit("my243number"))


