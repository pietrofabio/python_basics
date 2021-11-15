#def multi_print():
#        print("Hallo Welt!")
#        print("Hallo Welt!")

#multi_print()

#############################################

#def multi_print2(name, count):
#    for i in range(0, count):
#        print(name)

#multi_print2('kak', 5)

#def weitere_funktion():
#    multi_print2("kik",4)
#    multi_print2("kak", 2)

#weitere_funktion()

#############################################

#def maximum(a, b):
#    if a < b:
#        return str(b) + " b"
#    else:
#        return str(a) + " a"

#result = maximum(6, 5)
#print(result)

#############################################

#liste = [1, 2, 3]

#liste.append(4)

#print(liste)

#print("Hallo, Welt".split(", "))

#############################################

#file = open("lesen.txt", "r")

#for line in file:
#    print(line.strip())

#############################################

#file = open("schreiben.txt", "w")

#students = ["Max", "Monika", "Erik", "Franziska"]

#students.append("Kakafej")

#for student in students:
#    file.write(student + "\n")

#file.write("asdasd")

# #line: int
# #for line in file:
# #    print(line.strip())
#
# file.close()

#############################################

#WITH --> Datei wird geschlossen bevor/nach ein Fehler aufgetreten ist

# with open("lesen.txt", "r"):
#     for line in file:
#        print(line)

#############################################

# with open("datei.csv") as file:
#     for line in file:
#         data = line.strip().split(";")
#
#         #print(data)
#         print("In " + data[0] + " leben " + data[1] + " Personen, der Flughafen heißt " + data[2] + ".")

#############################################

# with open("datei.csv") as file:
#     for line in file:
#         data = line.strip().split(";")
#         if int(data[1]) < 2000000:
#         #if data[2] == "BER" or data[2] == "BUD":
#             print("In " + data[0] + " leben " + data[1] + " Personen, der Flughafen heißt " + data[2] + ".")

#############################################

# #%matplotlib inline
# import matplotlib.pyplot as plt
#
# xs = [1, 2, 3]
# ys = [4, 7 ,4]
#
# plt.plot(xs, ys)
# plt.show()

#############################################

# import matplotlib.pyplot as plt
#
# xs = []
# ys = []
#
# name = "Max"
# gender ="M"
# state = "CA"
#
# counter = 0
#
# with open("names.csv", "r") as file:
#     for line in file:
#         #counter = counter + 1
#         line_splitted = line.strip().split(",")
#         if line_splitted[1] == name and line_splitted[3] == gender and line_splitted[4] == state and int(line_splitted[2]) >= 1950 and int(line_splitted[2]) <= 2000:
#             counter = counter + int(line_splitted[5])
#             xs.append(line_splitted[2])
#             ys.append(line_splitted[5])
#             #print(line_splitted)
#             #break
#         #if counter == 12:
#         #    break
# #print(xs)
# #print(ys)
#
# print(counter)
# plt.plot(xs, ys)
# plt.show()

#############################################

# cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]
#
#
# def list_sum(l):
#     # hier kommt dein Code hin
#     summe = 0
#     # i = 0
#     for i in range(0, len(cart_prices)):
#         summe = summe + cart_prices[i]
#     print(summe)
#
#
# list_sum(cart_prices)

#############################################

# def prices_list(name, price):
#     # hier kommt dein Code hin, das "pass" kannst du durch deinen Code ersetzen
#     liste = []
#     preis = 0.79
#     for i in range(0, 10):
#         liste.append(str(i + 1) + " x Wunderkeks: " + str((i + 1) * preis))
#     return liste
#
# print(prices_list("Wunderkeks", 0.79))

#############################################

# shelf = ["Zaubersäge", "leer", "Wunderkekse", "Trickarten", "leer"]
#
# def add_shelf(article):
#     # hier kommt dein Code hin.
#     # Du darfst von innerhalb der Funktion direkt auf die Variable "shelf"
#     # zugreifen, diese muss nicht als Parameter übergeben werden, da sie
#     # schon außerhalb der Funktion existiert.
#     for i in range(0, len(shelf)):
#         if shelf[i] == "leer":
#             #shelf[i] = "Rubik's Cube"
#             shelf[i] = article
#             break
#     #print("Hier kommt dein Code hin")
#
# add_shelf("Rubik's Cube")
# print(shelf)

#############################################

# # Dictionaries
#
# d ={"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}
#
# d["Budapest"] = "BUD"
#
# print(d)
#
# del d["Budapest"]
#
# print(d)
#
# print(d["Helsinki"])
#
# print(d.get("Budapest"))
#
# if "Budapest" in d:
#     print("Budapest ist im Dictionary enthalten.")
# else:
#     print("Budapest ist nicht im Dictionary enthalten.")
#
# #############################################
#
#
# list = [x * x for x in range(10)]
#
# print(list[2:-2])

#############################################

#Tupel

# t = (1, 2, 3)
#
# print(t)

#############################################

# person = ["Max Müller", 55]
#
# def do_something(p):
#     p.append("Max Mustermann")
#
# do_something(person)
# print(person)

#############################################

#1

# student = ("Max Müller", 22, "Informatik")
#
# name, age, subject = student
#
# print(name)
# print(age)
# print(subject)

#2

# def get_student():
#     return ("Max Müller", 22, "Informatik")
#
# name, age, subject = get_student()
#
# print(name)
# print(age)
# print(subject)

#3

# students = [
#     ("Max Müller", 22),
#     ("Monika Mustermann", 23)
# ]
#
# for student in students:
#     name, age = student
#     print(name)
#     print(age)

#############################################

#d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}

#1

# for key in d:
#     value = d[key]
#     print(key)
#     print(value)

#2

# for key, value in d.items():
#     print(key + ": " + value)

#############################################

# d = {}
#
# with open("names.csv", "r") as file:
#     for line in file:
#         list = line.strip().split(",")
#         if list[0] == "Id":
#             continue
#         #serial, name, year, sex, state, count = tlist
#         #d = {"Serial": list[0], "Name": list[1], "Year": list[2], "Sex": list[3], "State": list[4], "Count": list[5]}
#         #d = {list[1]: list[5]}
#         name = list[1]
#         count = int(list[5])
#         #max(d, key=d.get)
#
#         if name in d:
#             d[name] = d[name] + count
#         else:
#             d[name] = count
#
# maxvalue = 0
# name = ""
#
# for key, value in d.items():
#     if int(value) > maxvalue:
#         name = key
#         maxvalue = int(value)
#     #else:
#     #    maxvalue = maxvalue
#
# print(name, maxvalue)
#         # for element in list:
#         #     if element in d:
#         #         d[element] = d[element] + 1
#         #     else:
#         #         d[element] = 1
        # for key, value in d.items():
        #     if maxvalue < value:
        #         maxvalue = value
        # print(maxvalue)
        #print(maxvalue[1])
        # for key in d:
        #     value = d[key]
        #     print(key)
        #     print(value)

#############################################

# Listen und Dictionaries verschachteln

#1

# liste = [
#     ["Berlin", "München", "Köln"],
#     ["Budapest", "Pécs", "Sopron"]
# ]
#
# print(liste[0][1])

#München

#2

# students = {
#     "Informatik": ["Max", "Monika"],
#     "BWL": ["Erik", "Franziska"]
# }
#
# print(students["Informatik"][1])
# #Monika
# print(students["BWL"][0:])
# #Erik, Franziska

#############################################

# Objektorientierung

# students = ["Max", "Monika"]
# students.append("Erik")
# print(students)

# class Student():
#     def name(self):
#         print(self.firstname + " " + self.lastname)
#
# erik = Student()
# erik.firstname = "Erik"
# erik.lastname = "Mustermann"
# erik.name()
#
# print(erik.firstname)
# print(erik.lastname)
#
# monika = Student()
# monika.firstname = "Monika"
# monika.lastname = "Müller"
# monika.name()
#
# print(monika.firstname)
# print(monika.lastname)
#
# class Company():
#     def name(self):
#         print(self.legal_name + " " + self.legal_type)
#
# c = Company()
# c.legal_name = "Max Müller"
# c.legal_type = "GmbH"
# c.name()
#
# def name_5x(v):
#     v.name()
#     v.name()
#     v.name()
#     v.name()
#     v.name()
#
# name_5x(monika)
# name_5x(c)

#############################################

# class Student():
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.term = 1
#
#     def increase_term(self):
#         self.term = self.term + 1
#
#     def name(self):
#         print(self.firstname + " " + self.lastname + " (Semester: " + str(self.term) + ")")
#
# erik = Student("Erik", "Mustermann")
# erik.increase_term()
# erik.name()
#
# monika = Student("Monika", "Müller")
# monika.name()

# from datetime import date
#
# print(date.today().weekday())

#if date.today().weekday() == 0:
    #run_report()

#############################################

# # Kapseln
#
# class Phonebook():
#     def __init__(self):
#         self.entries = {}
#
#     def add(self, name, phone_number):
#         self.entries[name] = phone_number
#
#     def get(self, name):
#         if name in self.entries:
#             return self.entries[name]
#         else:
#             return None
#
#     def __str__(self):
#         #return "--STR--"
#         return "Phonebook(" + str(self.entries) + ")"
#     def __repr__(self):
#         return self.__str__()
#     def __len__(self):
#         return len(self.entries)
#
# book = Phonebook()
# book.add("CicaCica", "+491794353644")
# book.add("Én", "+4917634519122")
#
# print(book.entries)
# #{'CicaCica': '+491794353644', 'Én': '+4917634519122'}
# print(book.get("Én"))
# #+4917634519122
# print(book)
# ##--STR--
# #Phonebook({'CicaCica': '+491794353644', 'Én': '+4917634519122'})
# print(len(book))
# #2

#############################################

# Class Creation

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#         self.diameter = 2 * radius
#         self.circumference = Circle.get_circumference(self)
#         self.area = Circle.get_area(self)
#
#     def get_circumference(self):
#         return 2 * 3.14159 * self.radius
#
#     def get_area(self):
#         return 3.14159 * self.radius ** 2
#
# mycircle = Circle(10)
#
# print(mycircle.radius, mycircle.diameter, mycircle.circumference, mycircle.area)

#############################################

# class Student():
#     def __init__(self, firstname, surname):
#         self.firstname = firstname
#         self.surname = surname
#
#     def name(self):
#         return self.firstname + " " + self.surname
#
# class WorkingStudent(Student):
#     def __init__(self, firstname, surname, company):
#         super().__init__(firstname, surname)
#         self.company = company
#
#     def name(self):
#         return self.firstname + " " + self.surname
#
#     def name(self):
#         #return "WorkingStudent: " + self.firstname + " " + self.surname + " " + self.company
#         return super().name() + " (" + self.company + ")"
#
# students = [
#     WorkingStudent("Max", "Müller", "ABC GmbH"),
#     Student("Monika", "Mustermann"),
#     Student("Erik", "Müller"),
#     WorkingStudent("Franziska", "Mustermann", "XY AG")
# ]
#
# #student = WorkingStudent("Max", "Müller", "ABC GmbH")
# for student in students:
#     print(student.name())
#
# # Max Müller (ABC GmbH)
# # Monika Mustermann
# # Erik Müller
# # Franziska Mustermann (XY AG)

#############################################

# class FileReader():
#     def __init__(self, filename):
#         self.filename = filename
#
#     def lines(self):
#         lines = []
#         with open(self.filename, "r") as file:
#             for l in file:
#                 lines.append(l.strip())
#         return lines
#
# class CSVReader(FileReader):
#     def __init__(self, filename):
#         super().__init__(filename)
#
#     def lines(self):
#         lines = super().lines()
#         #lines_splitted = []
#         return [line.split(",") for line in lines]      # List Comprehension für die auskommentierte Zeilen
#         #for line in lines:
#         #    lines_splitted.append(line.split(","))
#         #return lines_splitted
#
# #f = FileReader("datei.csv")
# f = CSVReader("datei.csv")
# print(f.lines())

#############################################

import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

url = 'https://dwa-hq-ql001.hospinet.net/internal_forms_authentication/'
payload = {'username': 'hospinet\peter.fabian', 'pwd': 'Axamew43'}
session = requests.Session()
session.get(url)
session.post(url, data=payload)
response = session.post(url, data=payload)
print(response.cookies)
url_afterlogin ='https://qlik.hospinet.net/hub/my/work'

#url_login = 'https://dashboard.getoaky.com/login'
#url_afterlogin = 'https://dashboard.getoaky.com/select-hotel'
#requests.get(url_login, auth=HTTPBasicAuth('hospinet\peter.fabian@h-hotels.com', 'Axamew43'))
#requests.get(url_login, auth=HTTPBasicAuth('maik.krell@h-hotels.com', 'oaky123'))

page = requests.get(url_afterlogin)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

# url_login = 'https://dashboard.getoaky.com/login'
# url_afterlogin = 'https://dashboard.getoaky.com/select-hotel'
# payload = {'c-login__input': 'maik.krell@h-hotels.com', 'password': 'oaky123'}
#
# with requests.Session() as session:
#     post = session.post(url_login, data=payload)
#     r = session.get(url_afterlogin)
#     print(r)
#
# page = requests.get(url_afterlogin)
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# text = str(soup.find_all('label', attrs='class="c-login__label" for="email">Email'))
# print(text)

# requests.post(url, data=payload)
#
# page = requests.get(url)
#
#
# print(soup)
# #results = soup.find(id="table-body")
# daten_elements = soup.find_all("o-table__body__row__item")#, class_="o-table__body__row__item")
# print(daten_elements)
#
# for daten_element in daten_elements:
#     print(daten_element, end='\n'*2)

#<td class="o-table__body__row__item" title="6th Sep, 20">6th Sep, 20</td>

# import requests
# from bs4 import BeautifulSoup
#
# URL = 'https://dashboard.getoaky.com/'
#
# page = requests.get(URL)
#
# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(id='all')
# print(results.prettify())

#<li class="o-table__tab o-button--tab--right" id="all" role="presentation">
#                    <a href="#" role="tab">All</a>
#                </li>

# import requests
# import bs4
#
# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# page = requests.get(URL)
#
# soup = bs4.BeautifulSoup(page.content, 'html.parser')
# results = soup.find(id='ResultsContainer')
# job_elems = results.find_all('section', class_='card-content')