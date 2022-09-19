# def reverseList(A, start, end): #reversing the array
#     while start < end:
#         A[start], A[end] = A[end], A[start]
#         start += 1
#         end -= 1
#
#
# A = [1,2,3,4,5,6,8]
# print(A)
# reverseList(A, 3, 4)
# print(A)
# reversing the array


# def reverse(A, start, end):
#     while start < end:
#         A[start], A[end] = A[end], A[start]
#         start += 1
#         end -= 1
#
# t = int(input())
# for i in range(t):
#     n = int(input())
#     l = input().strip().split()
#     l.reverse()
#     for i in l:
#         print(i, end=" ")
#     print()

# Recursion Python code for reversing the string
# def revrseList(A, start, end):
#     if start >= end:
#         return
#     A[start], A[end] = A[end], A[start]
#     reverseList(A, start + 1, end - 1)
#
#
# A = [1, 3, 5, 4, 6, 5]
# reverseList(A, 0, 4)
# print(A)

# List Slicing Python code for reversing the string
# list = [1, 2, 3, 4, 5, 6]
# print(list[2::-1] + list[3:6])

# Generate parenthesis
# class Solution:
#     def generateParenthesis(self, n: int) -> list[str]:
#         stack = []
#         res = []
#
#         def backtrack(openN, closeN):
#             if openN == closeN == n:
#                 res.append("".join(stack))
#                 return
#
#             if openN < n:
#                 stack.append("(")
#                 backtrack(openN, closeN + 1)
#                 stack.pop()
#         backtrack(0, 0)
#         return res


# for printing an array by taking the input
# arr = list(map(int, input().strip().split()))
# print(arr)
#                OR
# arr = [int(x) for x in input().split()]
# print(arr)

# class Book:
#     def __init__(self, title, author, pages, price):
#         self.title = title
#         # add properties
#         self.author = author
#         self.pages = pages
#         self.price = price
#         self.__secret = "This is a secret attribute."
#
#     # create instance methods
#     def getprice(self):
#         if hasattr(self, "_discount"):
#             return self.price - (self.price * self._discount)
#         else:
#             return self.price
#
#     def setdiscount(self, amount):
#         self._discount = amount
#
#
# # create some book instances
# b1 = Book("War and Peace", "Leo Tolstoy", 1225, 30.65)
# b2 = Book("War and Fire", "Tolstoy", 225, 10.65)
#
# # print the price of book1
# # print(b1.getprice())
# #
# # # try setting the discount
# # print(b2.getprice())
# # b2.setdiscount(0.12)
# # print(b2.getprice())
#
#
# # Properties with double underscores are hidden by the interpreter
# # print(b2.__secret)
# # output: AttributeError: 'Book' object has no attribute '__secret' as it cannot be accessed outside the class
# print(b2._Book__secret)
# # output: This is a secret attribute.

# Checking class types and instances
# class Book:
#     def __init__(self, title):
#         self.title = title
#
#
# class Newspaper:
#     def __init__(self, name):
#         self.name = name
#
#
# # create some instances of classes
# b1 = Book("War and Peace")
# b2 = Book("War and Fire")
# n1 = Newspaper("The washington Post")
# n2 = Newspaper("The New York Times")

# Use type() to inspect the object type
# print(type(b1))
# print(type(n1))
# output: <class '__main__.Book'>
# <class '__main__.Newspaper'>


# compare two types together(to make sure two instance of the same class or not)
# print((type(b1)) == type(b2))
# print((type(b1)) == type(n2))
# output: True
#         False

# use isinstance() to compare a specific instance to a known type
# print(isinstance(b1, Book))
# print(isinstance(n1, Newspaper))
# print(isinstance(n2, Book))
# print(isinstance(n2, object)) #in python everything is a subclass of the object class
# output: True
# True
# False
# True


# # Using class-level and static method
# class Book:
# # Properties defined at the class level are shared by all instances
#     BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
#
#
# # double underscore propertoes are hidden fron other classes
#     __booklist = None
#
#
# # create a class method (class method works on entire class)(@classmethod is a deriater)
#     @classmethod
#     def getbooktypes(cls):
#         return cls.BOOK_TYPES
#
# # create a static method
#     @staticmethod
#     def getbooklist():
#         if Book.__booklist == None:
#             Book.__booklist = []
#         return Book.__booklist
#
#
# # instance methods receive a specific object as an argument
# # and operate on data specific to that object instance
#     def serTitle(self, newtitle):
#         self.title = newtitle
#
#     def __init__(self, title, booktype):
#         self.title = title
#         if(not booktype in Book.BOOK_TYPES):
#             raise ValueError(f"{booktype} is not a valid book type")
#         else:
#             self.booktype = booktype
#
#
# # Access the class attribute
# print("Book types: ", Book.getbooktypes())
#
#
# # Create some book instances
# b1 = Book("Title 1", "HARDCOVER")
# b2 = Book("Title 2", "PAPERBACK")
#
#
# # Use the statice method to access a singleton object
# thebooks = Book.getbooklist()
# thebooks.append(b1)
# thebooks.append(b2)
# print(thebooks)
# output: [<__main__.Book object at 0x000001A7A0A06F40>, <__main__.Book object at 0x000001A7A0A1D190>]


# INHERITANCE
# understanding class inheritance
# class Book:
#     def __init__(self, title, author, pages, price):
#         self.title = title #doublycay
#         self.price = price #doublycay (to remove all these we will use the base class)
#         self.author = author
#         self.pages = pages
#
#
# class Magazine:
#     def __init__(self, title, publisher, price, period):
#         self.title = title #doublycay
#         self.price = price #doublycay
#         self.period = period
#         self.publisher = publisher
#
#
# class Newspaper:
#     def __init__(self, title, publisher, price, period):
#         self.title = title #doublycay
#         self.price = price #doublycay
#         self.period = period
#         self.publisher = publisher
#
#
# b1 = Book("War and Peace", "Potato", 345, 20.0)
# n1 = Newspaper("NY times", "The washington Post", 6.0, "Daily")
# m1 = Magazine("Apple","The New York Times", 5.99, "Monthly")
#
# print(b1.author)
# print(n1.publisher)
# print(b1.price, m1.price, n1.price)

# class Publication:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#
#
# class Periodical(Publication):
#     def __int__(self, title, publisher, price, period):
#         super().__init__(title, price)
#         self.period = period
#         self.publisher = publisher
#
#
# class Book(Publication):
#     def __init__(self, title, author, pages, price):
#         super().__init__(title, price)
#         self.author = author
#         self.pages = pages
#
#
# # class Magazine(Periodical):
# #     def __init__(self, title, publisher, price, period):
# #         super().__init__(title, price, period, publisher)
#
#
# class Newspaper:
#     def __init__(self, title, publisher, price, period):
#         super().__init__(title, publisher, price, period)
#
#
# b1 = Book("War and Peace", "Potato", 345, 20.0)
# n1 = Newspaper("NY times", "The washington Post", 6.0, "Daily")
# # m1 = Magazine("Apple", "The New York Times", 5.99, "Monthly")
#
# print(b1.author)
# print(n1.publisher)
# # print(b1.price, m1.price, n1.price)

# # using Abstract Base classes to enforce class constraints
# from abc import ABC, abstractmethod
#
# class GraphicShape(ABC):
#     def __init__(self):
#         super().__init__()
#
#     @abstractmethod
#     def calcArea(self):
#         pass
#
#
# class Circle(GraphicShape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calcArea(self):
#         return 3.14 * (self.radius ** 2)
#
#
# class Square(GraphicShape):
#     def __init__(self, side):
#         self.side = side
#
#     def calcArea(self):
#         return self.side * self.side
#
#
# # g = GraphicShape()
#
# c = Circle(10)
# print(c.calcArea())
# s = Square(12)
# print(s.calcArea())
#
# output: 314.0
# 144

# # Understanding Multiple Inheritance
# class A:
#     def __init__(self):
#         super().__init__()
#         self.foo = "foo"
#
#
# class B:
#     def __init__(self):
#         super().__init__()
#         self.bar = "bar"
#
#
# class C(A, B):           # method to inherit from more the one class
#     def __init__(self):
#         super().__init__()
#
#     def showprops(self):
#         print(self.foo)
#         print(self.bar)
#
#
# c = C() # C object is created
# c.showprops() # calling the method after C object is created
#
# output: foo
# bar

# # Understanding Multiple Inheritance
# class A:
#     def __init__(self):
#         super().__init__()
#         self.foo = "foo"
#         self.name = "Class A"
#
# class B:
#     def __init__(self):
#         super().__init__()
#         self.bar = "bar"
#         self.name = "Class B"
#
#
# class C(A, B):           # method to inherit from more the one class
#     def __init__(self):
#         super().__init__()
#
#     def showprops(self):
#         print(self.foo)
#         print(self.bar)
#         print(self.name)
#
#
# c = C() # C object is created
# c.showprops() # calling the method after C object is created
#
# # output:foo
# # bar
# # Class A (bcoz python use method resolution class "class C(A, B):" class C(B, A): output will changes to class B)
# print(C.__mro__)
# To check the Method resolution order: (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


# Using Abstract Base Classes to implement interfaces
# from abc import ABC, abstractmethod
#
# class JSONify(ABC): # this class works as an InterFace
#     @abstractmethod
#     def toJSON(self):
#         pass
#
# class GraphicShape(ABC):
#     def __init__(self):
#         super().__init__()
#
#     @abstractmethod
#     def calcArea(self):
#         pass
#
#
# class Circle(GraphicShape, JSONify):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calcArea(self):
#         return 3.14 * (self.radius ** 2)
#
#     def toJSON(self):
#         return f"{{\"Circle\" : {str(self.calcArea())}}}"
#
# c = Circle(10)
# print(c.calcArea())
# print(c.toJSON())
#
# # output:314.0
# # {"Circle" : 314.0}

# Using composition to bulid complex objects

# class Book:
#     def __init__(self, title, price, author=None):
#         self.title = title
#         self.price = price
#
#         self.author = author
#
#         self.chapters = []
#
#     def addchapter(self, chapter):
#         self.chapters.append(chapter)
#
#
#     def getbookpagecount(self):
#         result = 0
#         for ch in self.chapters:
#             result += ch.pagecount
#         return result
#
#
# class Author:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#     def __str__(self):
#         return f"{self.fname} {self.lname}"
#
#
# class Chapter:
#     def __init__(self, name, pagecount):
#         self.name = name
#         self.pagecount = pagecount
#
#
# auth = Author("leo", "tost")
# b1 = Book("mango", 30.4, auth)
#
# b1.addchapter(Chapter("CH 1", 123))
# b1.addchapter(Chapter("CH 2", 13))
# b1.addchapter(Chapter("CH 3", 143))
#
# print(b1.author)
# print(b1.title)
# print(b1.getbookpagecount())

# Using the __str__ and __repr__ magic methods
# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.price = price
#     # use the __str__ method to return a string
#     # use the __repr__ method to return an object representation
#
#
# b1 = Book("War Zone", "Leao", 34.8)
# b2 = Book("War Zone", "Leao", 34.8)
#
# print(b1)
# print(b2)
#  output:<__main__.Book object at 0x000002A2699A7580>
# <__main__.Book object at 0x000002A2699D6EE0>

# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.price = price
#     # use the __str__ method to return a string
#     def __str__(self):
#         return f"{self.title} by {self.author}, costs {self.price}"
#     # output: War Zone by Leao, costs 34.8
#             # War Zone by Leao, costs 34.8
#
#     # use the __repr__ method to return an object representation
#     def __repr__(self):
#         return f"title={self.title},author={self.author}, price={self.price}"
#     # output:title=Zone Star,author=Uleao, price=34.8
#
# b1 = Book("War Zone", "Leao", 34.8)
# b2 = Book("Zone Star", "Uleao", 34.8)
#
# print(b1)
# print(b2)
# print(str(b1))
# print(repr(b2))

# Equality and comparison
# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.price = price
#     # use the __eq__ method checks for equality between two objects
#     def __eq__(self, value):
#         if not isinstance(value, Book):
#             raise ValueError("Can't compare book to a non-book")
#         return (self.title == value.title and
#                 self.author == value.author and
#                 self.price == value.price)
#     # the __ge__ establishes >= relationship with another obj
#     def __ge__(self, value):
#         if not isinstance(value, Book):
#             raise ValueError("Can't compare book to a non-book")
#         return self.price >= value.price
#
#
#     # the __lt__ establishes >= relationship with another obj
#     def __lt__(self, value):
#         if not isinstance(value, Book):
#             raise ValueError("Can't compare book to a non-book")
#         return self.price < value.price
#
# b1 = Book("War Zone", "Leao", 84.8)
# b2 = Book("Ze ear", "Uao", 46.8)
# b3 = Book("War Zone", "Leao", 34.8)
# b4 = Book("Zone ar", "eao", 58.8)
#
# # print(b1 == b3) output: False as for python it checks for memory location of two objects if they are diffrent it retuns flase
# # check for equality
# # print(b1 == b3)
# # print(b1 == b2)
# # print(b1 == 45)
#
# # output: ValueError: Can't compare book to a non-book
# # True
# # False
#
# # Check for greater and lesser value
# # print(b2 >= b1)
# # print(b2 < b1)
#
# # Now we can sort them too
# books = [b1, b3, b2, b4]
# books.sort()
# print([book.title for book in books])
# output: ['War Zone', 'Ze ear', 'Zone ar', 'War Zone']

# # Attribute access
# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         # title, author, price, _discount all are the attribute
#         self.title = title
#         self.author = author
#         self.price = price
#         self._discount = 0.1  #_discount is an internal Attribute
#     # The __str__ function is used to return a user-friendly string
#     # representation  of the object
#
#     def __str__(self):
#         return f"{self.title} by {self.author}, costs {self.price}"
#
#     # __getattribute__ called when an attr is retrieved. Don't directly here otherwise a recursive loop is created
#     def __getattribute__(self, name):
#         if name == "price":
#             p = super().__getattribute__("price")
#             d = super().__getattribute__("_discount")
#             return p - (p * d)
#         return super().__getattribute__(name)
#     # __setattr__ called when an attribute value is set. Don't set the
#     # directly here otherwise a recursive loop cause a crash
#
#     def __setattr__(self, name, value):
#         if name == "price":
#             if name == "price":
#                 if type(value) is not float:
#                     raise ValueError("The price attr must be a float")
#             return super().__setattr__(name, value)
#
#     # __getattr__ called when __getattribute__ lookup fails - you can be
#     # pretty much generate attribute a recursive loop cause a crash
#     def __getattr__(self, name):
#         return name + " is not here!"
#
# b1 = Book("war", "leo", 34.0)
# b2 = Book("Due war", "leo bnantrish", 78.0)
#
# # b1.price = 54.67
# # print(b1)
# # output:Due war by leo bnantrish, costs 49.203
#
# # b2.price = 40 output: ValueError: The price attr must be a float
# # print(b2)
#
# # b2.price = float(40)
# # print(b2)
#
# # print(b1.ramdomprops)
# # output: ramdomprops is not here!

# Callable objects

# class Book:
#     def __init__(self, title, author, price):
#         super().__init__()
#         # title, author, price, _discount all are the attribute
#         self.title = title
#         self.author = author
#         self.price = price
#         self._discount = 0.1
#
#     def __str__(self):
#         return f"{self.title} by {self.author}, costs {self.price}"
#
#     # the __call__ method can be used to call the object like a function
#     def __call__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#
#
# b1 = Book("war", "leo", 34.0)
# b2 = Book("Due war", "leo bnantrish", 78.0)
#
# # call the object as if it were a function
# print(b1)
# b1("Anna Karenina", "Leo Tolstoy", 45.66)
# print(b1)
# output: war by leo, costs 34.0
# Anna Karenina by Leo Tolstoy, costs 45.66

# Defining a data class

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price


# create some instances
b1 = Book("war tease", "Leur Han", 1224, 39.54)
b2 = Book("Core Entity", "Henry", 3524, 139.54)

# access fields
print(b1.title)
print(b1.author)

