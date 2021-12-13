# encoding=latin-1
"""
Solution du jour 10 de advent of code https://adventofcode.com/2021
"""


from functools import reduce
from numpy import median


def est_corrompue(line: str) -> tuple[bool, str]:
	stack: list[str] = []
	for char in line:
		if char == '(':
			stack.append(')')
		elif char == '{':
			stack.append('}')
		elif char == '[':
			stack.append(']')
		elif char == '<':
			stack.append('>')
		else:
			expected = stack.pop()
			if char != expected:
				return True, char
	return False, ''


def find_illegal_chars():
	"""
	Partie 1 : Se rapporte à vérifier si l'expression est bien parenthèsée. On utilise une structure de tas.

	:return: Le score total de syntaxe
	:rtype: int
	"""

	with open("day10_input.txt", 'r') as file:
		lines = [line.strip() for line in file.readlines()]

	scores = { ')': 3,
			   ']': 57,
			   '}': 1197,
			   '>': 25137 }
	total = 0

	for line in lines:
		corr, c = est_corrompue(line)
		if corr:
			total += scores[c]

	return total


def complete_lines():
	"""
	Partie 2 : Cette fois on cherche à compléter les lignes incomplètes, en rajoutant les caractères fermants
	manquants. On associe alors un score à chacun, et on prend le score médian.

	:return: Le score médian de toutes les lignes
	:rtype: int
	"""

	with open("day10_input.txt", 'r') as file:
		lines = [line.strip() for line in file.readlines()]
		lines = filter(lambda l: not est_corrompue(l)[0], lines)

	scores = []

	scores_map = { ')': 1,
				   ']': 2,
				   '}': 3,
				   '>': 4, }

	for line in lines:
		stack: list[str] = []
		for char in line:
			# Flemme de tout taper, mais chacun des nombres correspond respectivement à
			# '[', '{' et '<'
			if ord(char) in [91, 123, 60]:
				stack.append(chr(ord(char) + 2))
			# '(' est pas marrant parce que ')' est juste après dans la table ascii et non 2 plus loin
			elif char == '(':
				stack.append(')')
			else:
				stack.pop()

		scores.append( reduce(lambda x, y: x * 5 + y, map(lambda x: scores_map[x], stack.__reversed__()), 0) )

	return int(median(scores))


def main():
	print(f"Solution de la partie 1 : {find_illegal_chars()}")
	print(f"Solution de la partie 2 : {complete_lines()}")


if __name__ == '__main__':
	main()
