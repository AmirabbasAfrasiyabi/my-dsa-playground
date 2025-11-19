# ---------------------------------------------------------------
#                            تعریف متغیر
# ---------------------------------------------------------------

# مقداردهی
# -------
x_int = 2
x_float = 2.3
x_bool = False
x_str1 = "i am a string"
x_str2 = 'i am a string too'
x_str3 = """i am a 
alsdkfjaskldjfal
;alsdfjlasd;jdflsajkf
very long string"""

# نوع متغیر
# -------
# print(type(x_int))
# print(type(x_str1))
# print(type(x_float))
# print(type(x_bool))
# print(isinstance(x_str3, str))

# # عملیات
# # -------
# print(x_int + x_float)
# print(x_str1 + x_str2)


# دسترسی به اندیس‌ها
# -------
s = 'this is a python workshop'
# print(s[0])
# print(s[-1])
# print(s[1:4])
# print(s[1:6:2])
# print(s[9:5])
# print(s[9:5:-1])
      
# # ************************************************
# # تمرین
# # برنامه‌ای بنویسید که یک رشته و دو عدد i و j بگیرد.
# # سپس معکوس زیر رشته از اندیس کوچکتر تا عدد بزرگتر را چاپ کند.
# # بدون استفاده از if
# # ************************************************

# # ************************************************
# # جواب:

# s = input()
# i, j = int(input()), int(input())
# higher = (i > j) * i + (j > i) * j
# lower = (i > j) * j + (j > i) * i
# print(s[higher:lower:-1])
# # ************************************************

# # رشته‌های فرمت‌دار
student_id = '96543210'
class_id = 40124
time = '13:30 - 15'
day = 'Saturday - Monday'

# print("hello %s" % student_id,)
# print("hello %s, welcome to %d" % (student_id, class_id))
# print("hello {}, welcome to {}, class is at {}, on {}".format(student_id, class_id, time, day))
# print("hello {student}, welcome to {class_no}, class is at {time}, on {day}".format(
#     student=student_id, class_no=class_id, time=time, day=day
# ))

# # توابع ویژه در رشته‌ها
# # -------
s = 'this is a workshop. have FUNNNNNN!'
# print(s.lower())
# print(s.upper())
# print(s.split(' '))
# print(s.index('work'))
# print(s.find('work'))
# print(s.count('a'))

# # ************************************************
# # تمرین
# # برنامه‌ای بنویسید که
# # در خط اول رشته‌ی S را ورودی بگیرد.
# # و در خط دوم دو کلمه‌ی S1 و S2 که با فاصله از هم جدا شده اند را از ورودی بگیرد.
# # سپس زیررشته‌ای از S، که از S1 شروع شود و به S2 ختم شود را چاپ کند.
# # مثال:
# # S = 'salam aleikom, hale shoma chetore? che khabara?'
# # S1 = 'aleikom' S2 = 'shoma'
# # output = 'aleikom, hale shoma'
# # ************************************************

# # ************************************************
# # جواب:
# S = input()
# S1, S2 = input().split(" ")
# start, end = S.find(S1), S.find(S2) + S2.__len__()
# # or
# start, end = S.find(S1), S.find(S2) + len(S2)
# S[start:end]
# # ************************************************

# # ---------------------------------------------------------------
# #                     ساختارهای شرطی و حلقه
# # ---------------------------------------------------------------

# # شرط
# # --------
# s = 'salam aleikom, aleikomossalam'
# if len(s) < 20:
#     pass
# elif len(s) < 30:
#     print("s is kinda short")
# else:
#     print("s isn't short")

# # حلقه
# # --------

# # 1: while
# i = 1
# while i < 10:
#     print(i)
#     i += 1

# # 2: for
# # ۱: روی آرایه
s = 'python workshop'
# for char in s:
#     print(char, end=":")

# # ۲: روی iterable
# for i in range(0, 10):
#     print(i, end="/")

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(9, -1, -1):
#     print(i)

# # ************************************************
# # تمرین
# # برنامه‌ای بنویسید که دو رشته با طول برابر دریافت کند
# # به عنوان خروجی رشته‌ای شامل حروف بزرگتر هر جایگاه را چاپ کند
# # ************************************************

# # ************************************************
# # جواب:
# x, y = input(), input()
# output = ""

# x,y = input() , input()
# output = ""

# ## 1
# for i in range(len(x)):
#     output += x[i] if x[i] > y[i] else y[i]

# ## 2
# for (xi, yi) in zip(x, y):
#     output += xi if xi > yi else yi
# # ************************************************


# # ---------------------------------------------------------------
# #                            لیست‌ها
# # ---------------------------------------------------------------

# # تعریف
# # -------
l = [1, 6, -4, 4.2, 19 + 2j, 'workshop']


# # ۱: اضافه کردن به لیست
# print(l.append(100))
# print(l)
# print(l.insert(5, 201))
# print(l)


# # # ۲: حذف کردن از لیست
# print(l.remove(19 + 2j))
# print(l)
# print(l.pop(5))
# print(l)

# # # ۳: سایر توابع
# print(l.reverse())
# print(l)
# print(l.sort())
# print((l))
# print(l.count(2))
# print(l)

# # ۱: کپی کردن

# l1 = l.copy()
# l1[0] = 394
# print(l1)
# print(l)  # ^_^

# # ۲: مقداردهی اولیه

# a = [0] * 10
# a[2] = a[4] = a[5] = 123
# print(a)

# a = [0, 1, 2] * 5
# a[0] = 123
# print(a)  # بازم منطقی

# a = [[0, 1, 2]] * 5
# print(a)
# a[0][0] = 123
# print(a)  # !!!!

# a = [[0, 1, 2] for i in range(5)]
# print(a)
# a[0][0] = 123
# print(a)  # ^_^


# # ************************************************
# # تمرین
# # برنامه‌ای بنویسید که در دو خط، دو آرایه‌ی n بعدی از ورودی بگیرد.
# # در خروجی یک آرایه‌ی دوبعدی n در 2 از آن بسازد
# # ************************************************

# # ************************************************
# # جواب:
# a = list(map(int, input().split(" ")))
# b = list(map(int, input().split(" ")))

# # 1
# output = []
# for (ai, bi) in zip(a, b):
#     output += [[ai, bi]]

# # 2
# output = []
# for (ai, bi) in zip(a, b):
#     output.append([ai, bi])

# # 3
# output = [[a[i], b[i]] for i in range(len(a))]
# # ************************************************


# # ---------------------------------------------------------------
# #                   چند‌تایی‌های مرتب، مجموعه‌ها و دیکشنری
# # ---------------------------------------------------------------

# # چندتایی‌های مرتب: لیست غیرقابل تغییر
# # ----------------------------
z = (10, 9, 8)  # کاربردش را بعدا خواهیم دید

print(z[0])
print(z[-1])


# # مجموعه‌ها: لیست‌ با اعضاء متمایز
# # ------------------------
# s = {1, 2, 3, 3, 3, 3, (1, 2), "helloooooo"}
# print(s)
# print(4 in s)
# print(3 in s)

# # ۱: اضافه کردن به مجموعه
# s.add(54)
# print(s)

# # ۲. حذف کردن از مجموعه
# s.remove(3)
# print(s)

# # دیکشنری
# # ------
# a = {'salam': 'hello',
#      40124: 'madaar',
#      (1, 2, 3): [2, 4, 6],
#      1: 10,
#      'salam': 'hi'}  # مقادیر متمایز. آخرین مقدار قرار میگیره.

# for key, value in a.items():
#     print(key, ":", value)

# # اضافه کردن به دیکشنری
# a['khodafez'] = 'bye'
# print(a)

# # ************************************************
# # تمرین
# # برنامه‌ای بنویسید که معکوس یک دیکشنری را بدست بیاورد
# # سپس از روی طول آن بفهمد که تابع نگاشت یک به یک بوده یا نه
# # ************************************************

# # ************************************************
# # جواب:
# a = {3: 9, -3: 9, 4: 16, 5: 25, 2: 4, -2: 4}
# # 1
# b = {}
# for key, value in a.items():
#     b[value] = key

# # ************************************************


# # ************************************************
# # تمرین
# # برنامه‌ای بنویسید که تعدادی اسم و فامیل از ورودی بخواند
# # سپس تشخیص بدهد در هر فامیل چند نفر متمایز هستند.
# # ************************************************


# # ************************************************
# # جواب:
names = [['shabnam', 'sheikhha'], ['sheida', 'sheikhha'], ['abbas', 'sheikhha'], ['maria', 'faghihi']]
count = {}
     
# for name, family in names:
#     if family in count:
#         count[family] += 1
#     else:
#         count[family] = 1
# print(count)


# # توابع
# # ------

# # تعریف
# def function_name(arg1, arg2, arg3="default_value"):
#     # code
#     return -1  # return value


# def is_prime(num):
#     for i in range(2, num // 2):
#         if num % i == 0:
#             return False
#     return True

# # کلاس‌ها
# # ------
# class student:
#     def __init__(self, id):
#         self.id = id
#         self.classes = {}

#     def add_class(self, class_no):
#         self.classes[class_no] = -1

#     def give_mark(self, class_no, mark):
#         if class_no in self.classes.keys():
#             self.classes[class_no] = mark
#         else:
#             print("student " + str(self.id) + " does not have this course.")

# s = student(96106543)
# s.add_class(40124)
# s.add_class(40425)
# s.give_mark(40124, 16)
# s.give_mark(20123, 20)