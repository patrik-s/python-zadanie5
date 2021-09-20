
meno = input("Meno hraca: ")
print("Okey {0}\nPravidla su nasledovne. Ja si myslim cislo a ty budes hadat.\nAk chces ukoncit hru, napis 'KONIEC'.\nNa konci hry uvidis svoje skore.".format(meno))

i = 0
j = 0
g = 'stoj'
while (g.lower()) != 'koniec':
	print("\n")
	print("Myslim si cislo: ")
	while (g.lower()) != 'koniec':
		import random
		random = random.randint(1,10)
		g = input("Tvoj tip?: ")
		if (g.lower()) != "koniec":
			if g == str(random):
				print("Spravne")
				i += 1
				break
			else :
				print("Nespravne")
				j += 1
vysledok = """+----tvoje skore-----+
| spravne   |   {}    |
| nespravne |   {}   |
| celkom    |   {}   |
+====================+"""			
print(vysledok.format(i,j,i+j))

