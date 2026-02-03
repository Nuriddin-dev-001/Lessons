# #Dictionari_mavzusi.
# #1.
# def str_counter(strs):
#     result = {}
#     for s in strs:
#         length = len(s)
#         if length in result:
#             result[length].append(s)
#         else:
#             result[length] = [s]
#     print(result)
# str_counter(["shaftoli", "olma", "nok", "uzum"])

# # 2.
# def merge_list(l1, l2):
#     return dict(zip(l1, l2))
# list_1 = ["a", "b", "c"]
# list_2 = [1, 2, 3]
# result = merge_list(list_1, list_2)
# print(result)

# # 3.
# class Phonebook:
#     def __init__(self):
#         self.contacts = {"Nodir": "+998918602711", "Laziz": "+998908002534"}
#     def add_contact(self, name, phone_number):
#         self.contacts[name] = phone_number
#         print(f"{name} qo'shildi!")
#     def update_contact(self, name, phone_number):
#         if name in self.contacts:
#             self.contacts[name] = phone_number
#             print(f"{name} ning telefoni yangilandi!")
#         else:
#             print(f"{name} topilmadi.")
#     def delete_contact(self, name):
#         if name in self.contacts:
#             del self.contacts[name]
#             print(f"{name} o'chirildi!")
#         else:
#             print(f"{name} topilmadi.")
#     def search_contact(self, name):
#         if name in self.contacts:
#             print(f"{name}: {self.contacts[name]}")
#         else:
#             print(f"{name} topilmadi.")

# phonebook = Phonebook()
# phonebook.add_contact("Ali", "+998911234567")
# phonebook.add_contact("Zarina", "+998922345678")
# phonebook.update_contact("Nodir", "+998919876543")
# phonebook.delete_contact("Laziz")
# phonebook.search_contact("Ali")
# phonebook.search_contact("Laziz")

# # 4.
# def counter_dict(nums):
#     result = {}
#     for num in nums:
#         if num in result:
#             result[num] += 1
#         else:
#             result[num] = 1
#     return result
# print(counter_dict([2, 1, 1, 1]))

# # 5.
 def max_ball_students(talabalar):
    sorted_students = sorted(talabalar.items(), key=lambda x: x[1], reverse=True)
    max_students = {sorted_students[0][0]: sorted_students[0][1], sorted_students[1][0]: sorted_students[1][1]}

    return max_students
print(max_ball_students({"Sardor": 76, "Zafar": 63, "Nodir": 76, "Sanjar": 80}))

