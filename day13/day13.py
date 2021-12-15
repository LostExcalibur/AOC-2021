# encoding=latin-1
"""
Solution du jour 13 de advent of code https://adventofcode.com/2021
"""
import pprint


def parse_input(filename: str) -> tuple[list[tuple[int, int]], list[tuple[str, int]]]:
	points, instructions = [], []
	with open(filename, 'r') as file:
		for line in file.readlines():
			if not line.strip():
				continue
			if line.strip().startswith("fold along "):
				instr = line.split('=')
				direc, line = instr[0][-1], int(instr[1])
				instructions.append((direc, line))
				continue

			split = line.strip().split(',')
			point = (int(split[0]), int(split[1]))
			points.append(tuple(point))

	return points, instructions


def build_grid(points):
	maxx = max(t[0] for t in points) + 1
	maxy = max(t[1] for t in points) + 1

	grid = []
	for i in range(maxy):
		grid.append([0] * maxx)

	for x, y in points:
		grid[y][x] = 1

	return grid


def fold(grid, coord, val):
	new = [line.copy()[:val + 1] for line in grid] \
		if coord == 'x' else \
		[line.copy() for line in grid[:val + 1]]

	if coord == 'x':
		for x in range(val, len(grid[0])):
			for y in range(len(grid)):
				new[y][2 * val - x] |= grid[y][x]

	if coord == 'y':
		for x in range(len(grid[0])):
			for y in range(val, len(grid)):
				new[2 * val - y][x] |= grid[y][x]

	return new


def first_fold(points: list[tuple[int, int]], instructions: list[tuple[str, int]]):
	"""
	Partie 1 : On reçoit une liste de points, et on effectue le premier pli

	:param points: Les points et leurs coordonnées
	:param instructions: Les plis à effectuer
	:return: Le nombre de points restants après le premier pli
	:rtype: int
	"""

	grid = build_grid(points)
	grid = fold(grid, *instructions[0])

	return sum(sum(x for x in line) for line in grid)


def completely_fold(points: list[tuple[int, int]], instructions: list[tuple[str, int]]):
	"""
	Partie 1 : On reçoit une liste de points, et on effectue le premier pli

	:param points: Les points et leurs coordonnées
	:param instructions: Les plis à effectuer
	:return: Le nombre de points restants après le premier pli
	:rtype: int
	"""

	grid = build_grid(points)

	for instruction in instructions:
		grid = fold(grid, *instruction)

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			grid[i][j] = "\u2B1B" if grid[i][j] else '\u2B1C'

	with open("output.txt", 'w', encoding="utf-8") as out:
		out.writelines("".join(line) + '\n' for line in grid)


def main():
	points, instructions = parse_input("day13_input.txt")
	print(f"Solution de la partie 1 : {first_fold(points, instructions)}")
	completely_fold(points, instructions)
	print(f"Solution de la partie 1 : Voir output.txt")


if __name__ == '__main__':
	main()
