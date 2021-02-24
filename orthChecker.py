import os
from editdistance import eval as diff

#How many changes are allowed to add word to result
TOLERANCE = 2

def addToDICT(word):
	word = word.lower()
	if not DICT.get(ord(word[0])) is None:
		existing = DICT.get(ord(word[0]))
		if word in existing: return
		existing.append(word)
		existing.sort()
		DICT[ord(word[0])] = existing
	else:
		DICT[ord(word[0])] = [word,]

def setupDICT():
	try:
		global DICT
		global filePath, dict
		projectPath = os.path.dirname(os.path.abspath(__file__))
		filePath = os.path.join(projectPath, 'words.txt')
		file = open(filePath, 'r')
		lines = file.read().splitlines()
		DICT = {}
		for line in lines:
			newWord = line.lower()
			addToDICT(newWord)
			# print(DICT)
		file.close()
	except FileNotFoundError:
		print("Words file not found!")
		return 0

def getSim(word):
	result = []
	word = word.lower()
	for line in DICT.get(ord(word[0])):
		distance = diff(word, line)
		ratio1 = 1-(distance/len(line))
		ratio2 = 1-(TOLERANCE/len(line))
		if ratio1 >= ratio2:
			result.append((line, ratio1))

	result.sort(key=lambda word: word[1], reverse=True)
	return result

def updateFile():
	arr = []
	for val in DICT.values():
		arr += val

	print(arr)
	with open(filePath, 'w') as file:
		file.write('\n'.join(arr))

def addAndUpdate(word):
	addToDICT(word)
	updateFile()
	print("Mot ajouté au DICT")

setupDICT()
while True:
	global ph
	ph = input("Donner votre phrase: ")
	c1 = ph[0].isalpha() and ph[0] == ph[0].upper()
	c2 = ph[-1].isalpha()
	c3 = ph.find("  ") == -1

	if (c1 and c2 and c3):
		print("Phrase validée!")
		ph = ph.split(' ')
		break
	else:
		print("Phrase non validée")

for index, word in enumerate(ph):
	print(f'Mot: "{word}"')
	results = getSim(word)
	# print(results)
	if len(results) == 0:
		print("Mot n'existe pas dans le DICT, taper \"add\" pour l'ajouter au DICT, ou presser entrer pour ignorer.")
		answer = input("input: ")
		if answer == "add":
			addAndUpdate(word)
		else:
			print("Mot ignoré")
		continue

	elif results[0][1] == 1:
		print("Mot correct!")
		continue

	print("0) Ajouter au DICT")
	for i, res in enumerate(results):
		print(f"{i+1}) \"{res[0]}\" / \"{word}\" : {int(res[1]*100)}%")
	else:
		while True:
			choice = int(input("Taper l'indice de l'opstion desirée: "))
			if 0 <= choice < len(results):
				break
		if choice == 0:
			addAndUpdate(word)
			continue
		choice -= 1
		ph[index] = results[choice][0].capitalize() if word[0].isupper() else results[choice][0].lower()
	

print("La phrase est:", ' '.join(ph))