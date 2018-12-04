class Hiku():
	""" This class lets you write a hiku and save it on text file"""
	def __init__(self,name,date):
		"""initelizing"""
		self.name = name #the name of the hiku
		self.date = date
		self.hiku = []
	def write_hiku(self):
		"""reciving each indevidual line of the hiku from the user"""
		count = 0
		while(count<3):
			line = input("Line {0}:".format(count+1))
			line = line.split()
			syllables = 0
			for i in line:
				syllables += self.syllable_count(i)
			if((count == 0 or count == 2) and syllables !=5):#chcking if the first and lasst lines have 5 syllables 
				print("You must have 5 syllables.\nYouu only have {0} syllables".format(syllables))
				continue
			elif(count == 1 and syllables != 7):#checking if the secod line has 7 syllabels
				print("You must have 7 syllables.\nYouu only have {0} syllables".format(syllables))
				continue
			" ".join(line)
			self.hiku.append(" ".join(line))
			count +=1

	def syllable_count(self,word):
		"""counting the number of syllabels in indevidual words"""
		word = word.lower()
		count = 0
		vowels = "aeiouy"
		if word[0] in vowels:
			count += 1
		for index in range(1, len(word)):
			if word[index] in vowels and word[index - 1] not in vowels:
				count += 1
		if word.endswith("e"):
			count -= 1
		if count == 0:
			count += 1
		return count
	def save_list(self,fileName,listName):
		"""saving an inputed list in to a text file along with the name and date"""
		F = open(fileName+".txt","w+")
		F.write(self.date+"\n")
		F.write(fileName+"\n")
		for i in listName:
			print(i)
			F.write(i+"\n")
		F.close()
hiku = Hiku(input("What is the name of your hiku\n"),input("What is the date?\n"))
hiku.write_hiku()
hiku.save_list(hiku.name,hiku.hiku)


#made by Fizzy Bubalech
