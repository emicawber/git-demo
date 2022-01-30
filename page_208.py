import json

filename = 'favourite_number'

def read_num():
	try:
		with open(filename,'r') as f:
			num = int(json.load(f))
	except FileNotFoundError:
		return None
	else:
		return num

def ask_num():
	try:
		num = int(input("Please enter your favourite number: "))
	except ValueError:
		print("Incorrect value for number")
		return None
	else:
		return num


num = read_num()

if (num):
	print(f"Your favorite number is: {num}")
else:
	flag = True

	while flag:
		num = ask_num()
		if (num):
			with open(filename, 'w') as f:
				json.dump(num, f)
			flag = False
		else:
			print("Invalid number")

