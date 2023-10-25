# первое задание
# class Point3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f"({self.x}, {self.y}, {self.z})"
#
# coordinate1 = Point3D(1, 2, 3)
# coordinate2 = Point3D(4, 5, 6)
# coordinate3 = Point3D(7, 8, 9)
#
# print(f"Точка 1: {coordinate1}\nТочка 2: {coordinate2}\nТочка 3: {coordinate3}")
#
#
# coordinate1.z = 10
#
# print("\nПосле изменения")
# print(f"Точка 1: {coordinate1}\nТочка 2: {coordinate2}\nТочка 3: {coordinate3}")
#
# coordinate2.x = 100
# print("\nПосле изменения 2")
# print(f"Точка 1: {coordinate1}\nТочка 2: {coordinate2}\nТочка 3: {coordinate3}")



# Вторая задача
# class Square:
#     def __init__(self, length):
#         self.length = length
#
#     def area(self):
#         return self.length ** 2
#
#     def perimeter(self):
#         return 4 * self.length
#
#
# length = 5
# square = Square(length)
# area = square.area()
# perimeter = square.perimeter()
#
# print(f"Площадь квадрата: {area}\nПериметр квадрата: {perimeter}")



# Третья задача
# import math
# class Triangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.hypotenuse = math.sqrt(a ** 2 + b ** 2)  # гипотенузa
#
#     def area(self):
#         area = 0.5 * self.a * self.b
#         return area
#
#     def perimeter(self):
#         perimeter = self.a + self.b + self.hypotenuse
#         return perimeter
#
#
# tri = Triangle(3, 5)
#
# area = tri.area()
# perimeter = tri.perimeter()
#
# print(f"Площадь треугольника: {area}\nПериметр треугольника: {perimeter}")



# Четветая задача
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, coordinate):
        return math.sqrt((self.x - coordinate.x) ** 2 + (self.y - coordinate.y) ** 2)


class Triangle:
    def __init__(self, coordinate_a, coordinate_b, coordinate_c):
        self.point_a = coordinate_a
        self.point_b = coordinate_b
        self.point_c = coordinate_c

    def perimeter(self):
        side_ab = self.point_a.distance(self.point_b)
        side_bc = self.point_b.distance(self.point_c)
        side_ca = self.point_c.distance(self.point_a)
        return side_ab + side_bc + side_ca


coordinate_a = Point(2, 4)
coordinate_b = Point(6, 9)
coordinate_c = Point(6, 0)

triangle = Triangle(coordinate_a, coordinate_b, coordinate_c)

perimeter = triangle.perimeter()
print("Периметр треугольника ABC:", perimeter)



# Шестая задача
# class CPerson:
#     def __init__(self, name, surname, patronymic, birthday, floor):
#         self.name = name
#         self.birthday = birthday
#         self.surname = surname
#         self.patronymic = patronymic
#         self.floor = floor
#
#     def register(self):
#         self.name, self.surname, self.patronymic = map(str, input('ФИО: ').split())
#         self.birthday = input('Когда вы роделись?: ')
#         self.floor = input('Ваш пол: ')
#
#     def hello(self):
#         print(f'Ваш профиль:\nФИО: {self.name} {self.surname} {self.patronymic}\nРоделись: {self.birthday}\nПол: {self.floor}')
#
#
# bob = CPerson('', '', '', '', '', )
# bob.register()
# bob.hello()



# седьмая задача
# class Reader:
# def __init__(self, full_name, ticket_number, faculty, birth_date, phone):
# self.full_name = full_name
# self.ticket_number = ticket_number
# self.faculty = faculty
# self.birth_date = birth_date
# self.phone = phone
#
# def takeBook(self, book_count):
# print(f"{self.full_name} взял {book_count} книги")
#
# def returnBook(self, book_count):
# print(f"{self.full_name} вернул {book_count} книги")
#
# reader1 = Reader("Петров В. В.", "12345", "Информатика", "01.01.1990", "123-456-7890")
# reader1.takeBook(3)
# reader1.returnBook(2)
