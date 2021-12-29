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

age = int(input("enter your age: "))
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