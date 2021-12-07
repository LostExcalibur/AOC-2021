# encoding=latin-1
"""
Solution du jour 1 de advent of code https://adventofcode.com/2021
"""


def number_times_increased():
	"""
	Partie 1 : renvoit le nombres de fois que la mesure de pronfondeur a augmenté par rapport à la dernière mesure

	:return: le nombre de mesures plus grandes que la précédente
	:rtype: int
	"""
	with open("day1_input.txt", "r") as file:
		lignes = file.readlines()
	nombres = [int(x) for x in lignes if x.strip()]

	plus_grands = [nombres[i] for i in range(1, len(nombres)) if nombres[i - 1] < nombres[i]]

	return len(plus_grands)


def number_sum_increased():
	"""
	Partie 2 : renvoit le nombres de fois que la somme des trois dernières mesures a augmenté
	par rapport à la somme précédente

	:return: le nombre de sommes plus grandes que la précédente
	:rtype: int
	"""
	with open("day1_input.txt", "r") as file:
		lignes = file.readlines()
	nombres = [int(x) for x in lignes if x.strip()]

	sommes = [sum(nombres[i: i + 3]) for i in range(len(nombres) - 2)]

	plus_grandes = [sommes[i] for i in range(1, len(sommes)) if sommes[i - 1] < sommes[i]]

	return len(plus_grandes)


# print(number_times_increased())
print(number_sum_increased())
