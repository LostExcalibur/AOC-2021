# encoding=latin-1
"""
Solution du jour 8 de advent of code https://adventofcode.com/2021
"""


def parse_input(filename: str) -> list[tuple[list[str], list[str]]]:
	with open(filename, 'r') as file:
		lines = [line.strip().split(" | ") for line in file.readlines()]

	return [(line[0].split(" "), line[1].split(" ")) for line in lines]


def easy_digits():
	"""
	Partie 1 : On se concentre d'abord sur les chiffres faciles, c'est à dire 1, 4, 7 et 8 car ils ont
	chacun un nombre unique de segments.

	:return: Le nombre de fois que ces chiffres sont apparus
	:rtype: int
	"""

	lines = parse_input("day8_input.txt")
	compte = 0

	for line in lines:
		_, output = line
		for nombre in output:
			compte += 1 if len(nombre) in { 2, 3, 4, 7 } else 0

	return compte


def deduce_all_output():
	"""
	Partie 2 : Cette fois on veut décoder tous les nombres

	:return: La somme de tous les outputs décodés
	:rtype: int
	"""

	correspondances_uniques = { 2: 1,
								3: 7,
								4: 4,
								7: 8 }

	lines = parse_input("day8_input.txt")

	total = 0

	for line in lines:
		uniques, output = line
		line_mapping = { }

		# On identifie d'abord les longueurs uniques
		for nombre in uniques:
			n = len(nombre)
			if n in correspondances_uniques.keys():
				line_mapping[correspondances_uniques[n]] = set(nombre)
				continue

		# On construit le set du petit "L" à gauche du 4, en gros la différence entre 4 et 1
		diff = line_mapping[4] - line_mapping[1]

		for nombre in uniques:
			n = len(nombre)
			# On l'a déjà identifié
			if n in correspondances_uniques.keys():
				continue

			s = set(nombre)
			# C'est un 2, 3 ou 5
			if n == 5:
				# Il a la ligne du 1 dedans, c'est un 3
				if line_mapping[1].issubset(s):
					line_mapping[3] = s
					continue
				# Il a le petit bout du 4 dedans donc c'est un 5
				elif diff.issubset(s):
					line_mapping[5] = s
					continue
				# C'est forcément un 2
				else:
					line_mapping[2] = s
					continue

			# C'est un 0, un 6 ou un 9
			if n == 6:
				# Le symbole contient celui du 4, c'est un 9
				if line_mapping[4].issubset(s):
					line_mapping[9] = s
					continue
				# Il contient le bout de 4, c'est un 6
				elif diff.issubset(s):
					line_mapping[6] = s
					continue
				# C'est forcément un 0
				else:
					line_mapping[0] = s
					continue

		# On a créé les correspondances pour cette ligne, on peut décoder la sortie

		for i, nb in enumerate(output):
			s = set(nb)
			for k, v in line_mapping.items():
				if v == s:
					total += k * 10 ** (3 - i)

	return total


print(deduce_all_output())
