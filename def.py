#Chapter-8
#Functions
def greeting():
	#this is called Docstring that will enclosed by 3 quotes, when it generates documentation for function
	"""greeting a msg"""
	print("Hello")
greeting()

#Pass information to the function
def greeting(name):
	print("hello " + name.title() + "!!!")

greeting("mahi")
greeting("tamil")

#Arguments and Parameters => the variable username called "parameters" and the value of information mahi is "argument"

#Ass-1
def display_msg():
	print("Hello everyone we are going to see this function chapter")

display_msg()

#Ass-2
def fav_book(title):
	print("my fav book is " + title.upper() + ". Such a nice book")

fav_book("ponniyan selvan")

#Passing Arguments
#Positional Arguments => Arguments should be in the same order in which parameter were written
#Keyword Arguments => Arguments should be with variable(parameter) name
def details(name, age):
	print("My name is " + str(name) + " and my age is " + str(age))

details("mahi", 23)
#Multi function calls
details("tamil", 27)
#Order matters in postional alrguments

#Keyword arguments => you can change order but, be sure when you giving arguments that should match with variable name 
def details(name, age):
	print("My name is " + str(name) + " and my age is " + str(age))

details(age = 23, name = "mahi")

#Default Values => should be as last parameter after all parameter that does not have defalut values
def details(age, name = "mahi"):
	print("My name is " + str(name) + " and my age is " + str(age))

details(age = 23)
details(23)

#Equivalent function calls => positional arguments, keyword arguments and default values often all used together
#Avoiding Arguments Errors

#Ass-1
def make_shirt(size, msg):
	print("the shirt size is " + str(size) + " and msg will print as " + str(msg))

make_shirt(63, "be brave")
make_shirt(size = 63, msg = '"be brave"')

#Ass-2
def make_shirt(msg, size = "large" ):
	print("the shirt size is " + str(size) + " and msg will print as " + str(msg))

make_shirt("be brave")
make_shirt("be brave", size = "medium")

#Ass-3
def info(city, country = "india"):
	print(str(country) + " : " + str(city))

info("aagra")
info("Hyd")
info("sanfrancisko" , country = "USA")

#Return values => it can process some date then it will return
def get_name(first_name, last_name):
	full_name = first_name + " " + last_name
	return full_name.title()

name = get_name("maheswari", "kumar")
print(name)

#Make arguments optional
def get_name(first_name, last_name, middle_name):
	full_name = first_name + " " + middle_name + " " + last_name
	return full_name.title()

name = get_name("maheswari", "kumar", "tamil")
print(name)
#if i want middle name argument as optional just make default value
def get_name(first_name, last_name, middle_name=""):
	if middle_name:
		full_name = first_name + " " + middle_name + " " + last_name
	else:
		full_name = first_name + " " + last_name
	
	return full_name.title()

name = get_name("maheswari", "kumar", "tamil")
print(name)
name = get_name("maheswari", "kumar")
print(name)

#returning dict
def get_name(first_name, last_name):
	full_name = {"first" : first_name, "last" : last_name}
	return full_name

name = get_name("maheswari", "kumar")
print(name)
#here also you can make optional 
def get_name(first_name, last_name, age=""):
	full_name = {"first" : first_name, "last" : last_name}
	if age:
		full_name["age"] = age
	return full_name
	
name = get_name("maheswari", "kumar")
print(name)
name = get_name("maheswari", "kumar", age=23)
print(name)

#using function with while loop
def get_name(first_name, last_name):
	full_name = first_name + " " + last_name
	return full_name.title()

while True:
	print("enter ypur name plz: ")
	f_name = input("name: ")
	if f_name == "q":
		break
	l_name = input("name: ")
	if l_name == "q":
		break
	format_name = get_name(f_name, l_name)
	print("Hello " + format_name)

#Ass-1
def area(city, state): 
	return city + " " + state

details1 = area("salem", "tamilnadu")
print(details1)

#Ass-2
def album(name, artist, track=""):
	lst = {"name" : name, "artist" : artist}
	if track:
		lst["track"] = track
	return lst

lst1 = album("song", "Spb")
print(lst1)
lst1 = album("song", "Spb", 45)
print(lst1)

#Ass-3
def album(name, artist):
	lst = {"name" : name, "artist" : artist}
	return lst

while True:
	print("enter: ")
	n = input("name: ")
	if n == "q":
		break
	a = input("album: ")
	if a == "q":
		break

	format1 = album(n , a)
	print(format1)

#passing list in function
def students(names):
	for name in names:
		print("hi " + str(name))

students_details = ["mahi", "tamil"]
students(students_details)

#modifying list in the funtion
#without def()
un_print = ["top", "jean", "shirt"]
complete = []

while un_print:
	current = un_print.pop()
	complete.append(current)
	print("types: " + str(current))

for completed in complete:
	print(completed)

#with def()
def printed_dress(un_print, complete):
	while un_print:
		current = un_print.pop()
		complete.append(current)
		print("types: " + str(current))

def show_complete(complete):
	for completed in complete:
		print(completed)

un_print = ["top", "jean", "shirt"]
complete = []
printed_dress(un_print, complete)
show_complete(complete)

#preventing a modifying list
def printed_dress(un_print, complete):
	while un_print:
		current = un_print.pop()
		complete.append(current)
		print("types: " + str(current))

def show_complete(complete):
	for completed in complete:
		print(completed)

un_print = ["top", "jean", "shirt"]
complete = []
printed_dress(un_print[:], complete)
show_complete(complete)
#the original list intact = it will not affect
print(un_print) 

#Ass-1
def magicians_names(names):
	for name in names:
		print(name)

magicians = ["mahi", "tamil", "nandi"]
magicians_names(magicians)

#Ass-2
def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	for magician in magicians:
		print("Great " + magician)

magicians = ["mahi", "nandi"]
show_magicians(magicians)
make_great(magicians)

#Ass-3
def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	for magician in magicians:
		print("Great " + magician)

magicians = ["mahi", "nandi"]
show_magicians(magicians[:])
make_great(magicians)
new = []
new = magicians[:]
print(new)
show_magicians(magicians[:])

#Passing an arbitary number of arguments => arbitary will create empty tuple howmany arguments if storing as value it will store there
def ordering(*cake):
	print("my fave cakes: ")
	for cakes in cake:
		print(cakes)

ordering("vennila")
ordering("chco", "mango")	

#mixing positional & arbitary arguments
#Passing an arbitary number of arguments
def ordering(kg, *cake):
	print("my order cake is : " + "with " + str(kg) + " kg")
	for cakes in cake:
		print(cakes)

ordering(1, "vennila")
ordering(2, "chco", "mango")	

#using keyword and arbitary arguments
def build_user(first, last, **user_info):# it will create empty dict
	profile = {}
	profile["first name"] = first
	profile["last name"] = last
	for keys, values in user_info.items():
		profile[keys] = values

	return profile

user_profile = build_user("mahi", "kumar", location = "salem", state = "tamilnadu")
print(user_profile)

#Ass-1
def ordered(*sandwitch):
	print("these sandwitchs are ordered: ")
	for sandwitchs in sandwitch:
		print(sandwitchs)

ordered("veg", "panner")
ordered("grill", "mushroom")
ordered("chicked", "normal")

#Ass-2
def mine(first, last, **details):
	my_dict = {}
	my_dict["first_name"] = first
	my_dict["last_name"] = last
	for key, value in details.items():
		my_dict[key] = value

	return my_dict

my_info = mine("maheswari", "kumar", location="salem", country="india", age=23)
print(my_info)

#Ass-3
def car_info(manufacture, model, **car_details):
	dic = {}
	dic["manufacture"] = manufacture
	dic["model"] = model
	for key, value in car_details.items():
		dic[key] = value

	return dic

info = car_info('subaru', 'outback', color='blue', tow_package=True)
print(info)

#Styling your code
#Ass-1
def order_items(*sandwitch):
	"""printing the ordered sandwitchs"""
	print("These sandwitchs are ordered: ")
	#Looping through the sandwitch items
	for sandwitchs in sandwitch:
		print(sandwitchs)

order_items("veg", "panner")
order_items("grill", "mushroom")
order_items("chicked", "normal")