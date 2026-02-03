# my_dict = (dict() ()
#            ( ())
# for key, value in my_dict.items():
#     if key == "age":
#         print(f"age: {my_dict['age']}")

# my_dict = [
# {"name": "Nuriddin", "age": 21},
# {"name": "Ali", "age": 23},
# {"name": "Muhriddin", "age": 29},
# ]
# for dict in my_dict:
#     print(f"age: {dict['age']}")

# my_dict = [
#     {"name": "Asad", "ball": 95},#for max=ball[0]
#     {"name": "Nodir", "ball": 73},
#     {"name": "Sardor", "ball": 84},
#     {"name": "Ali", "ball": 59},
# ]

# d = {"ism":"Nodir","yosh":21}
# d2 = dict(ism = "Nodir", yosh = 21)
# d3 = dict([("ism","Nodir"),("yosh", 21)])
# d["ball"]=90
# print(d["ball"])
# print(d2["yosh"])
# print(d3["ism"])

# students = {"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80 }
# max_ball = 0
# for values in students.values():
#     if values > max_ball:
#        max_ball = values
# print(max_ball)

# lst = [1,'alica', 2, 3, 'alica', 'alica']
#
# indice = lst.index('alica')
# indicies = [i for i in range(len(lst))if lst[i] == 'alica']
# print(indicies)

l = []
for x in range(3):
    for y in range(3):
        l.append((x, y))
print(l)
