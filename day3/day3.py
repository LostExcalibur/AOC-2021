# encoding=latin-1
"""
Solution du jour 3 de advent of code https://adventofcode.com/2021
"""


def occurences_bits(nombres: list[str]) -> tuple[list[int], list[int]]:
	freq_0 = [0] * len(nombres[0])
	freq_1 = [0] * len(nombres[0])
	for ligne in nombres:
		for pos, bit in enumerate(ligne):
			# On augmente la case correspondante
			(freq_1 if bit == '1' else freq_0)[pos] += 1
	return freq_0, freq_1


def calculate_power_consumption():
	"""
	Partie 1 : Calcule les nombres gamma et epsilon :
	   - gamma est constitué des bits les plus fréquents en chaque position,
	   - epsilon des moins fréquents

	:return: La consommation, soit gamma * epsilon
	:rtype: int
	"""

	with open("day3_input.txt", "r") as file:
		lignes = [ligne.strip() for ligne in file.readlines()]

	freq_0, freq_1 = occurences_bits(lignes)

	gamma = epsilon = ''
	for i in range(len(freq_1)):
		if freq_1[i] > freq_0[i]:
			gamma += '1'
			epsilon += '0'
		else:
			gamma += '0'
			epsilon += '1'

	gamma = int(gamma, 2)
	# Je suis cooool, en vrai c'est équivalent à int(epsilon, 2)
	# et en en plus ça marche que pour ce nombre de bits
	epsilon = ~gamma + 4096

	return gamma * epsilon


def calculate_life_support_rating():
	"""
	Partie 2 : Calcule le taux d'oxygene et de CO2

	:return: Le taux d'oxygene * le taux de CO2
	:rtype: int
	"""

	with open("day3_input.txt", "r") as file:
		lignes = [ligne.strip() for ligne in file.readlines()]

	oxygene = lignes.copy()
	co2 = lignes.copy()
	bit = 0
	while len(oxygene) > 1:
		freq_0, freq_1 = occurences_bits(oxygene)
		bon = '1' if freq_1[bit] >= freq_0[bit] else '0'
		oxygene = [number for number in oxygene if number[bit] == bon]
		bit += 1

	bit = 0
	while len(co2) > 1:
		freq_0, freq_1 = occurences_bits(co2)
		bon = '0' if freq_1[bit] >= freq_0[bit] else '1'
		co2 = [number for number in co2 if number[bit] == bon]
		bit += 1

	assert len(oxygene) == len(co2) == 1

	return int(oxygene[0], 2) * int(co2[0], 2)


def main():
	print(f"Solution de la partie 1 : {calculate_power_consumption()}")
	print(f"Solution de la partie 2 : {calculate_life_support_rating()}")


if __name__ == "__main__":
	main()
