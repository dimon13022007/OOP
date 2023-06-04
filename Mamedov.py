# class myBook:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def showInfo(self):
#         print('Title: {} \n'.format(self.title))
#         print(f'Author: {self.author}\n')
#         print(f'pages: {self.pages}\n')
#
#
# class myfile:
#     def __init__(self, filesize, src):
#         self.fileSize = filesize
#         self.src = src
#     def showInfo1(self):
#         print(f'file size: {self.fileSize}\n')
#         print(f'file source: {self.src}\n')
#
#
# class MyEbook(myBook, myfile):
#     def __init__(self, title, author, pages, filesize, src):
#         myBook.__init__(self, title, author, pages)
#         myfile.__init__(self, filesize, src)
#     def showInfo(self):
#         print(f'file size: {self.fileSize}\n')
#         print(f'file source: {self.src}\n')
#
#
# ebook1 = MyEbook('Python Course', 'Eric Matthes', 650, 1024, 'https://saitbook.com')
#
# ebook1.showInfo()
# print(MyEbook.mro())
# class Myclass1:
#     def sayhi(self):
#         print('Hi from class 1')
#
# class Myclass2(Myclass1):
#     pass
# def sayhi(self):
#     print('Hi from class 2')

# class Myclass3(Myclass1):
#     def sayhi(self):
#         print('Hi from class 3')
#
# class Myclass4(Myclass2, Myclass3):
#     pass
#
# myobj = Myclass4()
# myobj.sayhi()

# class Computer:
#     def calculate(self):
#         print('Calculaing...')
#
#
# class Display:
#     def display(self):
#         print('i display the image on the screen')
#
# class Smrtphone(Display, Computer):
#     pass
#
# pixel = Smrtphone()
# pixel.calculate()
# pixel.display()


# class Computer:
#     def __init__(self, model, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.model = model
#         self.memory = 128
#
#
# class Display:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.resolution = '4k'
#
# class Smartphone(Display, Computer):
#     def print_info(self):
#         print(self.resolution)
#         print(self.memory)
#
# pixel = Smartphone(model=input('Enter model: '))
# pixel.print_info()


class Computer:
    def __init__(self, size, resolution, battery_capacity, main_memory, additional_memory):
        self.size = size
        self.resolution = resolution
        self.battery_capacity = battery_capacity
        self.main_memory = main_memory
        self.additional_memory = additional_memory

    def show_info(self):
        print(f'size - {self.size}')
        print(f'resolution - {self.resolution}')
        print(f'battery capacity - {self.battery_capacity}')
        print(f'main memory - {self.main_memory}')
        print(f'additional memory - {self.additional_memory}')


class Display:
    def __init__(self, brightness, expansion, fps):
        self.brightness = brightness
        self.expansion = expansion
        self.fps = fps

    def show_info2(self):
        print(f'brightness - {self.brightness}')
        print(f'expansion - {self.expansion}')
        print(f'fps - {self.fps}')


class Ps(Computer, Display):
    def __init__(self, size, resolution, battery_capacity, main_memory, additional_memory, brightness, expansion, fps):
        Computer.__init__(self, size, resolution, battery_capacity, main_memory, additional_memory)
        Display.__init__(self, brightness, expansion, fps)

    def showInfo(self):
        print(f'size - {self.size}')
        print(f'resolution - {self.resolution}')
        print(f'battery capacity - {self.battery_capacity}')
        print(f'main memory - {self.main_memory}')
        print(f'additional memory - {self.additional_memory}')
        print(f'brightness - {self.brightness}')
        print(f'expansion - {self.expansion}')
        print(f'fps - {self.fps}')


ps = Ps(23, 23, 23, 23, 23, 23, 23, 23)
ps.showInfo()

# class Film:
#     def __init__(self, originalTitle, time, genre):
#         self.originalTitle = originalTitle
#         self.time = time
#         self.genre = genre
#
#     def showInfo(self):
#         print(f'Original title - {self.originalTitle}')
#         print(f'time - {self.time}')
#         print(f'genre - {self.genre}')
#
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def showInfo(self):
#         print(f'title - {self.title}')
#         print(f'Author - {self.author}')
#         print(f'pages - {self.pages}')
#
#
# film1 = Film('The Godfather', 126, 'horror')
# book1 = Book('AA', 'Viktor B', 315)
#
# for item in (film1,book1):
#     item.showInfo()
#
# book1 = Book('AA', 'Viktor B', 315)
# book2 = Book('AA3', 'Viktor B', 315)
# book1.__add__(book2)
#


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __eq__(self, other):
        if self.author == other.author and self.title == other.title:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.pages > other.pages:
            return True
        else:
            return False

    def __str__(self):
        return f'Title: {self.title}\n' \
               f'author: {self.author}\n' \
               f'pages: {self.pages}\n'

#
# book1 = Book('AA', 'Viktor B', 315)
# book2 = Book('AA3', 'Viktor B', 319)
#
# print(book1 == book2)
# print(book2 > book1)

# class Book:
#     def __init__(self, title, author, pages, reviews, book):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.reviews = reviews
#         self.book = book
#
#
#
#     def __eq__(self, other):
#         if self.author == other.author:
#             return True
#         else:
#             return False
#
#
#     def __gt__(self, other):
#         if self.pages > other.pages:
#             return True
#         else:
#             return False
#
#     def __ne__(self, other):
#         if self.book != other.book:
#             return True
#         else:
#             return False
#
#     def __ge__(self, other):
#         if self.reviews >= other.reviews:
#             return True
#         else:
#             return False
#
# book1 = Book(input('Enter title'))











