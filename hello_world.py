name = "Etienne"
print(f"Hello {name}, would you like to learn Python today?")
print(name.upper())
print(name.lower())
print(name.title())

name = " Etienne "
print(name.rstrip())
print(name.lstrip())
print(name.strip())


stones = ["Keith Richards", "Mick Jagger", "Charlie Watts", "Ronnie Wood"]
print(f"Rolling Stones are: {stones[0]}, {stones[1]}, {stones[2]}, {stones[3]}")

print(stones[-1])

stones.append("Etienne Lacroix")
print(stones)
del stones[-1]
print(stones)
stones.insert(0,"Etienne Lacroix")
print(stones)
popped_stone = stones.pop(0)
print(popped_stone)
print(stones)
stones.remove("Charlie Watts")
stones.sort(reverse=True)
print(stones)
print(sorted(stones))

# Exercise page 46
locations = ["Hawaii", "California", "France"]
print(locations)
print(sorted(locations))
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)

stones.sort();

for stoner in stones:
	print(f"Rolling Stones member: {stoner}")
	print("Still in loop")
	if stoner.lower() == "keith richards":
		print("My favourite!")
	elif stoner.lower() == "mick jagger":
		print("He's ok")
	elif stoner.lower() == "ronnie wood":
		print("He's been there a while but not an original")
print("Best Band In The World!\n")


numbers = []
for num in range(1,6):
	numbers.append(num)
print(numbers, max(numbers), min(numbers), sum(numbers))

# List Comprehension
a = [val**2 for val in range(1,11)]
print(a)

# Count from 1 - 20
for i in range(1,21):
	print(i)

million = [val for val in range(1,1_000_001)]
#print(million, sum(million))
print(f"Slice of a million is: {million[0:10]}")

# Odd numbers
for a in range(1,21,2):
	print(a)

# Looping through a slice
for stoner in stones[0:2]:
	print(stoner)

#Copying a list
favourite_band = stones # This just makes favourite_band point t stones... doesn't create a new list
print(f"Favourite Band: {favourite_band}")
stones.append("Mick Taylor")
print(f"With appended to original: {favourite_band}")	# Changed STONES list but out FAVOURITE_BAND, which was modified too
print(f"Stones original: {stones}\n")
del stones[-1]
favourite_band = stones[:]
print(f"Favourite Band: {favourite_band}")
stones.append("Mick Taylor")
print(f"With appended to original: {favourite_band}")
print(f"Original: {stones}")

# Tuple of immutable values (i.e. can't be changed)
tup = (1,10)
print(tup[0])
#tup[0] = 15  Generates an error since can't change value of tuple
# Can't change individual values but can assign a new value to a variable that represents a tuple
tup = (2,20)
print(tup[0])

for a in tup:
	print(a)

if 'Keith Richards' in stones:
	print("My favourite is in the list")

# Exercise page 84
alien_colors = ["green","red","yellow"]
for alien_color in alien_colors:
	if alien_color == "green":
		print("Earned 5 points")
	if alien_color != "green":
		print("Earned 10 points")


# Dictionaries
alien_0 = {'x_pos':13,
	'y_pos':32,
	}
print(alien_0['x_pos'])
print(alien_0.get('y_pos',0))

for a, b in sorted(alien_0.items()):
	print(f"Key: {a}")
	print(f"Value: {b}\n")

# Create a list of aliens
aliens = []

for alien_num in range(30):
	new_alien = {'color':'green', 'points':5, 'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)

print(f"Total number of aliens created: {len(aliens)}\n")

# Append dictionaries to list
stones = []
stones.append({'Name': 'Keith Richards', 'Instrument': 'Guitar'})
stones.append({'Name': 'Mick Jagger', 'Instrument': 'Singer'})

for stoner in stones:
	for key, value in stoner.items():
		print(f"{key}: {value}")
	print("\n")

msg = input("What's your name? ")
print(f"Hi {msg}")

try:
	age = int(input("Enter your age: "))
except ValueError:
	print("Incorrect value for age")
else:
	print(age)

pizzas = {}
flag = True

while flag:
	msg = input("Would you like a Pizza (Y/N)? ").upper()

	if msg == 'N':
		flag = False
	else:
		flag = True

		pizzas['SIZE'] = input("Size (L/M/S): ").upper()
		print(f"{pizzas['SIZE']} selected")

		topping = input("Would you like any toppings (Y/N)? ").upper()

		if topping == 'Y':
			toppings_flag = ""
			cnt = 1
			pizzas['TOPPINGS'] = []

		while toppings_flag != "N":
			topping = input(f"Please enter your {cnt} topping: ").upper()
			pizzas['TOPPINGS'].append(topping)

			toppings_flag = input("Would you like any other toppings (Y/N)? ").upper()

			cnt += 1

		print("Here is your order: ")
		for key, value in pizzas.items():
			print(f"{key} {value}")

# Page 137
def make_shirt(size, text):
	print(f"Size will be: {size} and text will be '{text}'")

make_shirt(18, "Stones!")

# Page 142
def make_album(artist_name, album_title, num_songs=None):
	if num_songs:
		album = {'ARTIST_NAME': artist_name, 'TITLE': album_title, 'NUM_SONGS': num_songs}
	else:
		album = {'ARTIST_NAME': artist_name, 'TITLE': album_title}
	return album

album = make_album('Rolling Stones','Sticky Fingers')
print(album)

print(f"{make_album('Rolling Stones','Sticky Fingers',9)}")

# Page 146
def send_messages(msgs_to_send, sent_msgs):
	while msgs_to_send:
		msg = msgs_to_send.pop();
		sent_msgs.append(msg)
		print(msg)

msgs_to_send = ["HEY", "YO"]					# lists
sent_msgs = []

send_messages(msgs_to_send, sent_msgs)
print(f"Messages left to send: {msgs_to_send}")
print(f"Messages sent: {sent_msgs}")

msgs_to_send = ["HEY", "YO"]
sent_msgs = []

send_messages(msgs_to_send[:], sent_msgs)
print(f"Messages left to send: {msgs_to_send}")
print(f"Messages sent: {sent_msgs}")

# Page 150
def sandwhich_builder(*items):						# items becomes a tuple (list of items that shouldn't be changed) - Looks just like a list but uses () instead of []
	for item in items:								# the * makes it optional
		sandwhich.append(item)						# if wanted to just send a list, just put items withouth the "*" and in the call, send a list between []

sandwhich = []
sandwhich_builder('Tomato','bacon')
print(f"Your 1st sandwhich is made of: {sandwhich}")
sandwhich = []
sandwhich_builder('Tomato','bacon', 'letuce')
print(f"Your 2nd sandwhich is made of: {sandwhich}")

def car_info(manufacturer, model_name, **args):		# Args becomes a dictionary (key-value pair)
	args['manufacturer'] = manufacturer
	args['model_name'] = model_name
	return args;

car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)

print("Page 162")

class Restaurant:
	"""Page 162"""

	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"{self.restaurant_name}, {self.cuisine_type}")

	def open_restaurant(self):
		print("Restaurant is opened")

	def set_number_served(self, num):
		if num >= self.number_served:
			self.number_served = num
		else:
			print(f"Invalid number served value: {num}")

	def increment_served(self):
		self.number_served += 1


new_restaurant = Restaurant("Mcdonald","French")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
new_restaurant.set_number_served(10)
print(new_restaurant.number_served)
new_restaurant.increment_served()
print(new_restaurant.number_served)

print("Page 173")
class IceCreamStand(Restaurant):
	"""Page 173"""

	def __init__(self,restaurant_name, cuisine_type, flavors):		# flavors is a list and is not optional (must have at least 1 flavor if you're a ice cream stand
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def get_flavors(self):
		for flavor in self.flavors:
			print(flavor)

new_ice_cream_stand = IceCreamStand("Dairy Queen", "Ice Cream", ['Vanilla', 'Chocolate'])
new_ice_cream_stand.get_flavors()


print("Reading from whole file")
with open('pi_digits.txt') as file_object:
	contents = file_object.read().rstrip()
print(contents)

print("Reading from file - 1 line at at time")
with open('pi_digits.txt') as file_object:
	print(file_object)	
	for line in file_object:
		print(line.rstrip())

# Writing to file
with open('test.txt', 'w') as f:	# Could also do "a" to append
	f.write("Hello")


# Page 202
WORD_TO_FIND = 'DICK'
try:
	with open("moby_dick.txt") as f:
		i = 0
		word_cnt = 0
		for line in f:
			if line.upper().count(WORD_TO_FIND):
				print(f"Number of times word '{WORD_TO_FIND}' is found in line #{i}: {line.upper().count(WORD_TO_FIND)}")
				word_cnt += 1
			i += 1
		print(f"Total number of lines: {i} - Total number of time found work {WORD_TO_FIND}: {word_cnt}")
except FileNotFoundError:
	pass
else:
	print(contents.count('dick'))

# Write and read json files
import json

numbers_out = [1, 2, 3, 4, 5, 6 ,7]
with open('numbers.json', 'w') as f:
	json.dump(numbers_out, f)

with open('numbers.json', 'r') as f:
	numbers_in = json.load(f)
print(f"Numbers read from json file: {numbers_in}")