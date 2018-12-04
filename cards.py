import random
import time
class Cards():
	def __init__(self):
		self.deck = []
	def populate_deck(self):
		suits = ["Diamonds","Hearts","Clubs","Spades"]
		for i in suits:
			for j in range(1,14):
				value = j
				if(j == 11):
					value = "Jack"
				if(j == 12):
					value = "Queen"
				if(j == 13):
					value = "King"
				if(j == 1):
					value = "Ace"
				self.deck.append(str(value)+" of "+ i)
	def print_deck(self,list):
		if(self.deck != []):
			for i in self.deck:
				print(str(self.deck.index(i)+1)+": "+i)

		else:
			print("the deck is empty")
	def shuffle(self):
		random.shuffle(self.deck)
class War(Cards):
	def set_up(self):
		self.player1 = self.deck[:len(self.deck)//2]
		self.player2 = self.deck[len(self.deck)//2:]
	def check_cards(self,top_p1,top_p2):
		pass
	def turn(self):
		if(len(self.player1)>0 and len(self.player2)>0):
			top_p1 = self.player1[-1]
			top_p2 = self.player2[-1]
			print(top_p1+" - "+ top_p2)
			top_p1 = top_p1.split()
			top_p1  = top_p2.split()
			if(top_p1[0] == "Jack"): 
				value1 = 11#top_p1[0] = 11
			if(top_p2[0] == "Jack"): 
				value2 = 11 #top_p2[0] = 11
			if(top_p1[0] == "Queen"): 
				value1 = 12#top_p1[0] = 12
			if(top_p2[0] == "Queen"):
				value2 = 12#top_p2[0] = 12
			if(top_p1[0] == "King"):
				value1 = 13#top_p1[0] = 13
			if(top_p2[0] == "King"):
				value2 = 13#top_p2[0] = 13
			if(top_p1[0] == "Ace"):
				value1 = 1#top_p1[0] = 1
			if(top_p2[0] == "Ace"):
				value2 = 1#top_p2[0] = 1
			else: 
				value2 = top_p2[0]
				value1 = top_p1[0]
			#self.check_cards(top_p1,top_p2)
			if(value1>value2):
				self.player1.append(self.player2[-1])
				self.player2.pop()
				print("Player One one this turn")
			if(value1 < value2):
				self.player2.append(self.player1[-1])
				self.player1.pop()
				print("Player Two one this turn")
			else:
				self.player1.pop()
				self.player2.pop()
				print("No one won this turn")
			return True
		else:
			print("The game is over")
			return False



Deck = Cards()
Deck.populate_deck()
Deck.shuffle()
Deck.print_deck(Deck.deck)
game = War()
game.populate_deck()
game.shuffle()
game.set_up()
while(True):
	ass = game.turn()
	if(ass == False):
		break

