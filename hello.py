import time

variable = time.altzone
power = 10  ** 2

string = "my name is abdul rahman"

first_name = "abdul"
second_name = "Rahman"

full_name = first_name + " " + second_name
len(full_name)

age = 16

can_vote = age>=18
can_vote

age = 19
has_license = True
is_drunk = False

can_vote = age>=16 and has_license and not is_drunk
can_vote

name = "Baba"
string = f"my name is {name}"
print(name.lower())



temp = 26
if temp > 30:
    print("its too hot gang")
elif temp > 25:
    print("gang its too hot!")
else:
    print("gang sybau")


has_license = True
age = 17

if has_license:
    if age >= 18:
        print("gang welcome")
    else:
        print("gang first be 18 gang then buy ticket")
else:
    print("get the fuck out you are 18 but no ticket")


for i in range(1,20,2):
    print(i)


my_list = ["hi", 25, True,]

my_list[0] = "dave"
my_list.insert(1, "kaka")
my_list


person = { "name": "alice",
          "place": "hyderabad" }

person["name"] = "dave"
person["license"] = True

if "license" in person:
    print("found gang!")

person.update({"name":"randi"})
print(person)

fruits = set(["banana", "apple", "banana",])
set(fruits)


def check_weather():
    temp = 26
    if temp >= 26:
        print("damn nigga its hot ")
    else:
        print("sybau cold")

check_weather()


def greet(name,age):
    print(f"hi {name} your age is {age}")

greet(name="nigga", age=25)



def calculate_total(price, discount, tax_rate):
    tax = price * tax_rate
    total= price + tax - discount
    print(f"hey pussy your total is {total}")

calculate_total(10, 0.1, 0.2)


def value(a,b):
    print(a+b)

value(5,6)



def value_return(a=7,b=7):
    return a + b

print(value_return())


def calculate_area(height, width):
    return height * width

room_area = calculate_area(10, 12)
print(f"The area is {room_area}")



def double(number):
    return number * 2

first_number = double(10) + double(2)
first_number


def double(number):
    number * 2
    return number
total = double(10) + double(2)
total



def simple_function():
    numbers = [1,2,3,4,5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number

f, l = simple_function()
print(f,l)


from math import sqrt, pi

ournewnumber = sqrt(16)
print(ournewnumber)
print(pi)




import os
current_dir = os.getcwd()
print(current_dir)


import pandas as pd

import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

temperature = data["current"]["temperature_2m"]
print(f"hi the paris temp currently is {temperature}")


import requests
def get_weather(latitude,longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data = response.json()
    return data["current"]["temperature_2m"]
   

paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")


x = 10
y = 20
print(x + y)


def mynigga():
    print("woof")

mynigga()


x = 10

y = 10

print(f"{x} hello number")