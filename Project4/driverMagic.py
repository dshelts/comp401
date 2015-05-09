import magicCollection
import instructions
def main():

	collection = magicCollection.collection()
	collection.readFile("cardCollection.txt")
	while True:
		instructions.menu()
		print "0: to quit"
		ui = str(raw_input("Enter your choice: "))
		
		if ui == "0":
			break
		
		elif ui == "1":
			#manually enter cards			
			collection.enterCards()
			collection.writeFile("cardCollection.txt")
			print ("cardCollection.txt has been updated.")
	
		elif ui == "2":
			#enter by file
			filename = str(raw_input("\nEnter file you would like to read from: "))
			collection.readFile(filename)

		elif ui == "3":
			#print collection
			print(collection)

		elif ui == "4":
			#create a deck list
			deck = str(raw_input("\nInput deck name: "))+".txt"
			newDeck = magicCollection.collection()
			newDeck.enterCards()
			collection.writeFile(deck)
			print ("Your deck is in text file: "+deck)
		
		elif ui == "5":
			#search by string and substring
			cardName = str(raw_input("\nInput a card name or part of name: "))
			foundCard = collection.findCard(cardName)
			if foundCard != None:
				print (foundCard)

			else:
				possible = collection.findCards(cardName)
				if len(possible) == 0:
					print("Card or possible cards not in collection.")
				else:
					print(cardName+" Not found did you mean?\n[")
					for card in possible:
						print(card)
					print("]")
					

		else:
			break
	
	print("__DONE__")


if __name__ == '__main__':
	main()