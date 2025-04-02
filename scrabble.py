
abc = 'azertyuiopqsdfghjklmwxcvbn?'
abc = list(abc)
print(abc)

### EXERCICE 2 
def motMax(tirage, motsPossibles):
	L = []
	occurencesTirage = {lettre:0 for lettre in tirage}
	for mot in motsPossibles:
		Possible = True
		occurences = {lettre:0 for lettre in tirage}
		for lettre in mot: 
			if lettre not in tirage:
				Possible = False
			else:
				occurences[lettre]+=1
		for lettre in occurences.keys():
			if occurences[lettre]>occurencesTirage[lettre]:
				Possible = False

		if Possible == True:
			L.append(mot)
	if L==[]:
		print("Il n'y a aucun mot possible !")
	else:
		m=0
		motM = L[0]
		for i in range(0, len(L)):
			if m<len(L[i]):
				m=len(L[i])
				motM=L[i]
		return motM



### EXERCICE 3
def maxPointsMot(tirage, motsPossibles, pointsLettres):
	L = []
	occurencesTirage = {lettre:0 for lettre in abc}

	for lettre in tirage:
		occurencesTirage[lettre]+=1
	for mot in motsPossibles:
		occurences = {lettre:0 for lettre in abc}
		Possible = True
		for lettre in mot: 
			
			if lettre in tirage or '?' in tirage:
				occurences[lettre]+=1
				
			else:
				Possible = False
		nombreJoker = occurencesTirage['?']
		for lettre in occurences.keys():
			if occurences[lettre]>(occurencesTirage[lettre] + nombreJoker):
				Possible = False
			else:
				if occurences[lettre] - occurencesTirage[lettre] >= 0:
					nombreJoker -= occurences[lettre] - occurencesTirage[lettre]
		if Possible == True:
			L.append(mot)
	if L==[]:
		print("Il n'y a aucun mot possible !")
	else:
		motM=maxScore(pointsLettres, L)
		return motM


def score(pointsLettres, mot):
	pointsMot = 0
	for lettre in mot:
		pointsMot += pointsLettres[lettre]
	return pointsMot


def maxScore(pointsLettres, listeMots):
	points=0
	motM = listeMots[0]
	for i in range(0, len(listeMots)):
		pointsMot = score(pointsLettres, listeMots[i])
		if points<pointsMot:
			points=pointsMot
			motM=listeMots[i]
	return (motM, points)


### EXERCICE 4

def maxPointsMotJoker(tirage, motsPossibles, pointsLettres):
	L = []
	for mot in motsPossibles:
		Possible = True
		for lettre in mot: 
			
			if lettre not in tirage:
				Possible = False
		if Possible == True:
			L.append(mot)
	if L==[]:
		print("Il n'y a aucun mot possible !")
	else:
		motM=maxScore(pointsLettres, L)
		return motM

pointsLettres={'?':0,'a':1,'e':1,'i':1,'l':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1, 'd':2,'g':2,'m':2, 'b':3,'c':3,'p':3, 'f':4,'h':4,'v':4, 'j':8, 'q':8, 'k':10,'w':10,'x':10,'y':10,'z':10}


def dictionnaire():
	with open("motsSansAccent.txt") as file:
		dic = file.read()
		listeMots = dic.split("\n")
		for i in range(0,len(listeMots)):
			mot = listeMots[i]
			m=''
			for l in mot:
				if l in abc:
					m+=l
			listeMots[i]=m
	return listeMots

motsPossibles = dictionnaire()
tirage = ['e', 'v', 'g', 'a', 'a', 'e', 'v', 'r', 't', 't', 'b', 'i', 'y', 's', 's', 'c', 'z', '?']



print(maxPointsMot(tirage, motsPossibles, pointsLettres))











