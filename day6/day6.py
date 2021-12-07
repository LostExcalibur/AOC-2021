# encoding=latin-1
"""
Solution du jour 6 de advent of code https://adventofcode.com/2021
"""


def simulate(n: int) -> int:
	with open("day6_input.txt", 'r') as file:
		poissons = [int(x) for x in file.readline().split(',')]

	for _ in range(n):
		if _ % 5 == 0:
			print(_)
		a_ajouter = []
		for i in range(len(poissons)):
			if poissons[i] == 0:
				poissons[i] = 6
				a_ajouter.append(8)
				continue
			poissons[i] -= 1
		poissons += a_ajouter

	return len(poissons)


def nb_poissons_lanterne():
	"""
	Partie 1 : Chaque poisson est modélisé par le nombre de jours qu'il lui reste avant de créer un nouveau
	poisson ; son compteur est alors réinitialisé à 6. Un poisson qui apparait voir son compteur initialisé
	à la valeur 8, pour simuler sa maturation.

	:return: Le nombre de poissons après 80 jours
	:rtype: int
	"""

	return simulate(80)


def nb_poissons_plus_lgt():
	"""
	Partie 2 : le même problème, mais plus longtemps

	:return: Le nombre de poissons après 256 jours
	:rtype: int
	"""

	# Devient très lent un peut après 100 générations
	# return simulate(256)

	with open("day6_input.txt", 'r') as file:
		poissons = [int(x) for x in file.readline().split(',')]

	num_per_day = [poissons.count(i) for i in range(9)]

	for i in range(256):
		new = num_per_day[0]
		for n in range(8):
			num_per_day[n] = num_per_day[n + 1]
			if n == 6:
				num_per_day[n] += new
		num_per_day[8] = new

	return sum(num_per_day)


print(nb_poissons_plus_lgt())
