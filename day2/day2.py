# encoding=latin-1
"""
Solution du jour 2 de advent of code https://adventofcode.com/2021
"""


def follow_instructions() -> int:
	"""
	Partie 1 : Calcule la position et la profondeur finale après avoir suivi les instructions fournies.

	:return: Le produit de la position et de la profondeur finales
	:rtype: int
	"""
	horiz = depth = 0

	with open("day2_input.txt", "r") as file:
		lines = file.readlines()

	for line in lines:
		split = line.split(" ")
		instruction, amount = split[0], int(split[1])
		if instruction == "forward":
			horiz += amount
		elif instruction == "down":
			depth += amount
		elif instruction == "up":
			depth -= amount
		else:
			print("Bad instruction :", instruction)

	return horiz * depth


def follow_new_instructions() -> int:
	"""
	Partie 2 : Calcule la position et la profondeur finale après avoir suivi les instructions fournies,
	mais avec la nouvelle interprétation

	:return: Le produit de la position et de la profondeur finales
	:rtype: int
	"""
	horiz = depth = aim = 0

	with open("day2_input.txt", "r") as file:
		lines = file.readlines()

	for line in lines:
		split = line.split(" ")
		instruction, amount = split[0], int(split[1])
		if instruction == "forward":
			horiz += amount
			depth += aim * amount
		elif instruction == "down":
			aim += amount
		elif instruction == "up":
			aim -= amount
		else:
			print("Bad instruction :", instruction)

	return horiz * depth


print(follow_new_instructions())
