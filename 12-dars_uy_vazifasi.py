# # 12-dars
# # formula

# # 1.
# def user_data(first_name, last_name, age):
#     print(f"Ism: {first_name}")
#     print(f"Familiya: {last_name}")
#     print(f"Yosh: {age}")

# first_name = input("Ismni kiriting: ")
# last_name = input("Familiya kiriting: ")
# age = input("Yoshingizni kiriting: ")

# user_data(first_name, last_name, age)

# # 2.
# def find_max(a, b, c):
#     max_vals = [a]

#     if b > max_vals[0]:
#         max_vals = [b]
#     elif b == max_vals[0]:
#         max_vals.append(b)

#     if c > max_vals[0]:
#         max_vals = [c]
#     elif c == max_vals[0]:
#         max_vals.append(c)

#     max_vals_str = " va ".join([f"= A {val}" for val in max_vals])
#     print(f"Eng katta son - {max_vals_str}")

# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# c = float(input("Uchinchi sonni kiriting: "))

# find_max(a, b, c)

# # 3.
# def find_letter_count(word, letter):
#     count = word.lower().count(letter.lower())
#     print(f'"{word}" so\'zida "{letter}" dan {count} ta.')

# word = input("So'zni kiriting: ")
# letter = input("Qidirmoqchi bo'lgan harfni kiriting: ")

# find_letter_count(word, letter)
#
# # 4.
# def list_sum(myList):
#     total = sum(myList)
#     print(f"Listning elementlar yig'indisi = {total}")
#
# myList = [2, 4, 6, 8, 12]
# list_sum(myList)

# # 5.
# def daraja(a, b):
#     result = a ** b
#     print(f"{a} ni {b} darajasi = {result}")

# a = float(input("Sonni kiriting: "))
# b = int(input("Darajani kiriting: "))

# daraja(a, b)

# # 6.
# def daraja4(a, b, c, d):
#     result_b = a ** b
#     result_c = a ** c
#     result_d = a ** d
#     print(f"{a} ni {b} darajasi = {result_b}")
#     print(f"{a} ni {c} darajasi = {result_c}")
#     print(f"{a} ni {d} darajasi = {result_d}")

# a = float(input("Sonni kiriting: "))
# b = int(input("Birinchi darajani kiriting: "))
# c = int(input("Ikkinchi darajani kiriting: "))
# d = int(input("Uchinchi darajani kiriting: "))

# daraja4(a, b, c, d)

# # 7.
# def digit_count_and_sum(word):
#     count = 0
#     total = 0
#     for char in word:

# # 8.
# def add_right(a, b, c):
#     print(f"Natija: {a+b+c}")
# s=input("A son: ")
# d=input("B son: ")
# f=input("C son: ")

# add_right(s,d,f)

# # 9.
# def add_left(a, b, c):
#     print(f"Natija: {c+b+a}")
# s=input("A son: ")
# d=input("B son: ")
# f=input("C son: ")

# add_left(s,d,f)

# # 10.
# def work_with_list(a):
#     min_value = min(a)
#
#     a = [x * min_value for x in a]
#
#     print(a)
# a = [3, 6, 4, 2, 5]
# work_with_list(a)


# # 11.
# def big_sales(sales):
#     return max(sales, key=sales.get)
# print(big_sales(sales={
#         'yanvar':12000,
#         'mart':6000,
#         'aprel':15000,
#         'sentyabr':9000,
#         'dekabr':10000
#     }))

# #12.
# def min_max(numbers,max_num,min_num):
#     maxi=max(numbers)
#     mini=min(numbers)
#     if maxi==max_num:
#         print(f"Ha, {maxi} katta!")
#     if mini==min_num:
#         print(f'Ha, {mini} kichik!')
#     else:
#         print(f'Xato! eng kattasi {maxi}, eng kichigi {mini}')
# numbers=list(map(int,input('Sonlar: ').split()))
# max_num=int(input('Katta son: '))
# min_num=int(input('Kichik son: '))
# min_max(numbers,max_num,min_num)

# #13.
# def expensiveProducts(products):
#     product=products[0]
#     for i in products:
#         if i['price'] > product["price"]:
#             product=i
#             print(f"Eng qimmat telefon nomi: <<{product['name']}>>")
#
# products=[
#   {
#     "name": "Iphone X",
#     "price": 600
#   },
#   {
#     "name": "Iphone 12",
#     "price": 1500
#   },
#   {
#     "name": "Samsung Note 9",
#     "price": 800
#   },
#   {
#     "name": "Samsung S10",
#     "price": 1100
#   },