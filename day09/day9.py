# encoding=latin-1
"""
Solution du jour 9 de advent of code https://adventofcode.com/2021
"""

from functools import reduce
from operator import mul


def est_valide(x, y, Nx, Ny):
	return 0 <= x < Nx and 0 <= y < Ny


def voisins(x, y, grid):
	v = []
	Nx, Ny = len(grid[0]), len(grid)
	if est_valide(x + 1, y, Nx, Ny):
		v.append((x + 1, y))
	if est_valide(x, y + 1, Nx, Ny):
		v.append((x, y + 1))
	if est_valide(x - 1, y, Nx, Ny):
		v.append((x - 1, y))
	if est_valide(x, y - 1, Nx, Ny):
		v.append((x, y - 1))
	return v


def est_plus_bas_que_le_tour(x, y, grid):
	for xv, yv in voisins(x, y, grid):
		if grid[y][x] >= grid[yv][xv]:
			return False
	return True


def low_points(grid):
	low = []
	Nx, Ny = len(grid[0]), len(grid)
	for x in range(Nx):
		for y in range(Ny):
			if est_plus_bas_que_le_tour(x, y, grid):
				low.append((x, y))
	return low


def risk_levels():
	"""
	Partie 1 : étant donné une grille d'entiers entre 0 et 9, trouve tous ceux qui sont plus petits que leurs voisins.
	On ne compte pas les voisins en diagonale

	:return: La somme de toutes les valeurs plus un qui sont plus petites que leurs voisins.
	:rtype: int
	"""
	with open("day9_input.txt", 'r') as file:
		grid = [line.strip() for line in file.readlines()]
		grid = [[int(x) for x in list(line)] for line in grid]

	return sum(grid[y][x] + 1 for x, y in low_points(grid))


def find_basins():
	"""
	Partie 2 : On considère maintenant dans la même grille des bassins, qui sont délimités par des 9.

	:return: Le produit de la taille des trois plus grands bassins
	:rtype: int
	"""
	with open("day9_input.txt", 'r') as file:
		grid = [line.strip() for line in file.readlines()]
		grid = [[int(x) for x in list(line)] for line in grid]

	low = low_points(grid)

	basins = []

	# Chaque point le plus bas correspond à un bassin unique
	for xlow, ylow in low:
		basin = [(xlow, ylow)]
		while True:
			nv = False
			for b in basin:
				for xv, yv in voisins(b[0], b[1], grid):
					if (xv, yv) not in basin and grid[yv][xv] != 9:
						basin.append((xv, yv))
						nv = True
			# Si on n'a pas trouvé de nouveau point dans le bassin, on arrête passe au suivant
			if not nv:
				basins.append(basin)
				break

	long = list(map(len, basins))
	long.sort()
	long.reverse()

	return reduce(mul, long[:3], 1)


def main():
	print(f"Solution de la partie 1 : {risk_levels()}")
	print(f"Solution de la partie 2 : {find_basins()}")


if __name__ == "__main__":
	main()
