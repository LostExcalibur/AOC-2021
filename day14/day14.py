# encoding=latin-1
"""
Solution du jour 14 de advent of code https://adventofcode.com/2021
"""


def parse_data(filename: str) -> tuple[str, dict]:
	corresp = {}

	with open(filename, 'r') as file:
		lines = file.readlines()

		start = lines[0].strip()

		for line in lines[2:]:
			a, b = line.strip().split(' -> ')
			corresp[a] = b

	return start, corresp


def step(current, corresp):
	new = current[0]

	for i in range(len(current)):
		if current[i:i + 2] in corresp:
			new += corresp[current[i:i + 2]] + current[i + 1]

	return new


def grow_polymer(start, corresp):
	current = start
	for i in range(10):
		current = step(current, corresp)

	freqs = {}
	for unique in set(current):
		freqs[unique] = current.count(unique)

	return max(freqs.values()) - min(freqs.values())


def grow_further(start: str, corresp: dict):
	current = {}
	for pattern in set(corresp.keys()):
		current[pattern] = start.count(pattern)

	for key, value in current.items():
		if value:
			print(f"{key}: {value}")

	for i in range(10):
		for pattern, equiv in corresp.items():
			current[pattern] -= 1
			current[pattern[0] + equiv] += 1
			current[equiv + pattern[1]] += 1

	end = ''
	for k, v in current.items():
		end += k * v

	freqs = { }
	for unique in set(end):
		freqs[unique] = end.count(unique)

	return max(freqs.values()) - min(freqs.values())


def main():
	data = parse_data("day14_input.txt")
	print(f"Solution de la partie 1 : {grow_polymer(*data)}")
	print(f"Solution de la partie 2 : {grow_further(*data)}")


if __name__ == '__main__':
	main()
