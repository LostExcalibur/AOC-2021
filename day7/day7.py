# encoding=latin-1
"""
Solution du jour 7 de advent of code https://adventofcode.com/2021
"""


from numpy import median


def parse_input_file(filename: str) -> list[int]:
	with open(filename, 'r') as file:
		return list(map(int, file.readline().split(',')))


def cout(x1: int, x2: int) -> int:
	n = abs(x1 - x2)
	return n * (n + 1) // 2  # Le // est pour éviter de convertir en int, car on sait que le résultat sera toujours entier


def align_horiz_positions():
	"""
	Partie  1 : Etant donné une liste de positions horizontales, trouve la position pour laquelle le coût total
	du déplacement de chacun des crabes à cette position est minimal

	:return: Le coût total des déplacement
	:rtype: int
	"""
	init = parse_input_file("day7_input.txt")

	best = int(median(init))

	return sum(map(lambda x: abs(x - best), init))


def updated_cost():
	"""
	Partie 2 : Cette fois, le coût augmente de 1 par unité de distance, donc 1 -> 2 donne 1 mais 1 -> 3 donne 3

	:return: Le coût minimal
	:rtype: int
	"""

	init = parse_input_file("day7_input.txt")
	n = max(init)

	couts: list[int] = [0] * n

	for i in range(n):
		couts[i] = sum(map(lambda x: cout(x, i), init))

	return min(couts)


print(updated_cost())
