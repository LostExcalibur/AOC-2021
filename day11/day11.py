# encoding=latin-1
"""
Solution du jour 11 de advent of code https://adventofcode.com/2021
"""


def est_valide(x, y, Nx=10, Ny=10):
	return 0 <= x < Nx and 0 <= y < Ny


def voisins(x, y, grid):
	v = []
	Nx, Ny = len(grid[0]), len(grid)
	for i in range(-1, 2):
		for j in range(-1, 2):
			if i == j == 0:
				continue
			if est_valide(x + i, y + j, Nx, Ny):
				v.append((x + i, y + j))
	return v


def flash(grid: list[list[int]]) -> int:
	flashes, a_propager = [], []

	for i in range(10):
		for j in range(10):
			if grid[j][i] > 9:
				flashes.append((i, j))
				a_propager.append((i, j))

	while a_propager:
		i, j = a_propager.pop()
		for x, y in voisins(i, j, grid):
			grid[y][x] += 1
			if grid[y][x] > 9 and (x, y) not in flashes:
				flashes.append((x, y))
				a_propager.append((x, y))

	return len(flashes)


def step(grid: list[list[int]]) -> int:
	for i in range(10):
		for j in range(10):
			grid[j][i] += 1

	flashs = flash(grid)

	for i in range(10):
		for j in range(10):
			if grid[j][i] > 9:
				grid[j][i] = 0

	return flashs


def nombre_flashs():
	"""
	Partie 1 : Similaire au jeu de la vie, sauf qu'un flash peut entrainer un autre dans la même itération.

	:return: Le nombre total de flashs en 100 itérations
	:rtype: int
	"""

	with open("day11_input.txt", 'r') as file:
		lines = [line.strip() for line in file.readlines()]
		grid = [[int(x) for x in line] for line in lines]

	return sum(step(grid) for _ in range(100))


def attendre_synchro():
	"""
	Partie 2 : On attend que les flashs se synchronisent,
	donc on continue tant que toute la grille n'est pas à 0

	:return: Le nombre d'itérations nécessaires à la synchronisation
	:rtype: int
	"""
	with open("day11_input.txt", 'r') as file:
		lines = [line.strip() for line in file.readlines()]
		grid = [[int(x) for x in line] for line in lines]

	nb = 0
	while any(any(grid[i][j] for j in range(10)) for i in range(10)):
		nb += 1
		step(grid)

	return nb


def main():
	print(f"Solution de la partie 1 : {nombre_flashs()}")
	print(f"Solution de la partie 2 : {attendre_synchro()}")


if __name__ == '__main__':
	main()
