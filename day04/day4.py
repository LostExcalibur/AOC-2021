# encoding=latin-1
"""
Solution du jour 4 de advent of code https://adventofcode.com/2021
"""

import numpy as np


def parse_input(filename: str) -> tuple[list[int], list[np.ndarray]]:
	with open(filename, 'r') as file:
		nombres = [int(nb) for nb in file.readline().split(',')]

		plateaux, current = [], []
		i = 0
		new = True

		while line := file.readline():
			if line[0] == '\n':
				continue
			if new:
				current = np.zeros((5, 5), dtype=int)
				i = 0
				new = False
			current[i, :] = [int(nb) for nb in line.split(' ') if nb.strip()]
			i += 1

			if i == 5:
				plateaux.append(current)
				new = True
	return nombres, plateaux


def final_score_win():
	"""
	Partie 1 : Calcule le score final du plateau gagnant en multipliant la somme de tous ses nombres
	non appelés par le dernier nombre appelé

	:return: Le score final du plateau gagnant
	:rtype: int
	"""
	nombres, plateaux = parse_input("day4_input.txt")

	called = []
	winner = None
	won = False

	while not won:
		called.append(nombres.pop(0))

		for plateau in plateaux:
			for i in range(5):
				# merci numpy
				if all(map(lambda x: x in called, plateau[:, i])) or all(map(lambda x: x in called, plateau[i, :])):
					winner = plateau
					won = True
					break
			if won:
				break

	return sum(sum(filter(lambda x: x not in called, winner[i])) for i in range(5)) * called[-1]


def final_score_lose():
	"""
	Partie 2 : Calcule le score final du dernier plateau à gagner en multipliant la somme de tous ses nombres
	non appelés par le dernier nombre appelé

	:return: Le score final du plateau perdant
	:rtype: int
	"""

	nombres, plateaux = parse_input("day4_input.txt")

	called = []
	gagne = [False] * len(plateaux)

	# On appelle des nombres jusqu'à ce qu'il ne reste plus qu'un plateau en jeu
	while len([x for x in gagne if x]) < len(plateaux) - 1:
		called.append(nombres.pop(0))

		for idx, plateau in enumerate(plateaux):
			if gagne[idx]:
				continue
			for i in range(5):
				# merci numpy
				if all(map(lambda x: x in called, plateau[:, i])) or all(map(lambda x: x in called, plateau[i, :])):
					gagne[idx] = True

	# On a trouvé celui qui gagne en dernier
	perdant = plateaux[gagne.index(False)]

	# On continue jusqu'à ce qu'il gagne
	termine = False
	while not termine:
		called.append(nombres.pop(0))
		for i in range(5):
			# merci numpy
			if all(map(lambda x: x in called, perdant[:, i])) or all(map(lambda x: x in called, perdant[i, :])):
				termine = True

	return sum(sum(filter(lambda x: x not in called, perdant[i])) for i in range(5)) * called[-1]


def main():
	print(f"Solution de la partie 1 : {final_score_win()}")
	print(f"Solution de la partie 2 : {final_score_lose()}")


if __name__ == "__main__":
	main()
