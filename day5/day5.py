# encoding=latin-1
"""
Solution du jour 5 de advent of code https://adventofcode.com/2021
"""


def sign(x: int) -> int:
	return -1 if x < 0 else (1 if x > 0 else 0)


def at_least_2_overlaps():
	"""
	Partie 1 : Etant donné une liste de lignes décrites par leurs cooronées extrémales, renvoit le nombre de
	points du plan où plus de deux lignes s'intersectent.
	On ne considère que les lignes horizontales et verticales.

	:return: Le nombre de points de concourance de plus de deux lignes.
	:rtype: int
	"""

	with open("day5_input.txt", 'r') as file:
		lines = file.readlines()
		start_end = [line.split(" -> ") for line in lines]

	parsed = [[tuple(int(x) for x in pos.split(',')) for pos in line] for line in start_end ]

	grid = [[0] * 1000 for _ in range(1000)]

	for line in parsed:
		start, end = line

		x0, y0 = start
		x1, y1 = end

		if x0 == x1:
			dy = sign(y1 - y0)
			for i in range(abs(y1 - y0) + 1):
				grid[y0 + i * dy][x0] += 1

		elif y0 == y1:
			dx = sign(x1 - x0)
			for i in range(abs(x1 - x0) + 1):
				grid[y0][x0 + i * dx] += 1

	return sum(len(list(filter(lambda x: x > 1, line))) for line in grid)


def also_diagonal_overlap():
	"""
	Partie 2 : Etant donné une liste de lignes décrites par leurs cooronées extrémales, renvoit le nombre de
	points du plan où plus de deux lignes s'intersectent.
	On considère maintenant les lignes diagonales à 45° en plus.

	:return: Le nombre de points de concourance de plus de deux lignes.
	:rtype: int
	"""

	with open("day5_input.txt", 'r') as file:
		lines = file.readlines()
		start_end = [line.split(" -> ") for line in lines]

	parsed = [[tuple(int(x) for x in pos.split(',')) for pos in line] for line in start_end ]

	grid = [[0] * 1000 for _ in range(1000)]

	for line in parsed:
		start, end = line

		x0, y0 = start
		x1, y1 = end

		# horizontal
		if x0 == x1:
			if y0 > y1:
				y1, y0 = y0, y1
			for i in range(y0, y1 + 1):
				grid[i][x0] += 1

		# vertical
		elif y0 == y1:
			if x0 > x1:
				x1, x0 = x0, x1
			for i in range(x0, x1 + 1,):
				grid[y0][i] += 1

		# diagonal
		else:
			dx = sign(x1 - x0)
			dy = sign(y1 - y0)
			for i in range(abs(x1 - x0) + 1):
				grid[y0 + dy * i][x0 + dx * i] += 1

	return sum(len(list(filter(lambda x: x > 1, line))) for line in grid)


print(at_least_2_overlaps())
