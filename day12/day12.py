# encoding=latin-1
"""
Solution du jour 12 de advent of code https://adventofcode.com/2021
"""


def parse_input(filename: str) -> dict:
	graphe = { }

	with open(filename, 'r') as file:
		for line in file.readlines():
			start, end = line.strip().split('-')

			if start not in graphe.keys():
				graphe[start] = []
			graphe[start].append(end)

			if end not in graphe.keys():
				graphe[end] = []
			graphe[end].append(start)

	return graphe


def parcours(graphe: dict, start: str, visites: list[str], partie2: bool):
	resultat = []
	if start == "end":
		resultat.append(visites)
		return resultat

	voisins = filter(lambda x: (x.isupper() or (x not in visites or partie2)) and x != "start", graphe[start])
	for v in voisins:
		p = partie2
		if p and v.islower() and v in visites:
			p = False
		resultat.extend(parcours(graphe, v, visites + [v], p))

	return resultat


def nombre_chemins():
	"""
	Partie 1 : on parcourt le graphe, en ne visitant les petites grottes qu'au plus une fois mais les grosses
	autant de fois qu'on veut.

	:return: Le nombre de chemis différents
	:rtype: int
	"""

	graphe = parse_input("day12_input.txt")

	return len(parcours(graphe, "start", ["start"], False))


def nouveaux_chemins():
	"""
	Partie 2 : Pareil que partie 1, mais se donne une grotte en minuscule à visiter dux fois

	:return: Le nombre de chemins
	:rtype: int
	"""

	graphe = parse_input("day12_input.txt")

	return len(parcours(graphe, "start", ["start"], True))


def main():
	print(f"Solution de la partie 1 : {nombre_chemins()}")
	print(f"Solution de la partie 2 : {nouveaux_chemins()}")


if __name__ == '__main__':
	main()
