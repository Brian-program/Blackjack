import random
from itertools import product


suits = ["spades","clubs","diamonds","hearts"]
values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

#card lists
deck = list(product(suits, values))
dealer_hand = []
player_hand = []

#dictionary of values of face cards
face_card_key = {"A":11, "J":10, "Q":10, "K":10}

#end the game
end_round = False
end_game = False

#blackjack boolean
player_blackjack = False
dealer_blackjack = False


#getters
def get_player_hand():
	return player_hand

def get_dealer_hand():
	return dealer_hand

def get_player_hand_sum():
	player_hand_sum = 0

	for i in player_hand:
		if i[1] in face_card_key:
			value = face_card_key[i[1]]
			player_hand_sum += int(value)
		else:
			value = i[1]
			player_hand_sum += int(value)

	if player_hand_sum > 21:
		for i in player_hand:
			if i[1] == "A":
				player_hand_sum -= 10

	return player_hand_sum

def get_dealer_hand_sum():
	dealer_hand_sum = 0

	for i in dealer_hand:
		if i[1] in face_card_key:
			value = face_card_key[i[1]]
			dealer_hand_sum += int(value)
		else:
			value = i[1]
			dealer_hand_sum += int(value)

	if dealer_hand_sum > 21:
		for i in dealer_hand:
			if i[1] == "A":
				dealer_hand_sum -= 10

	return dealer_hand_sum


#Fisher–Yates shuffle Algorithm
def shuffle():
	global deck
	for i in range(len(deck)-1,1,-1):
		#j is a random index of the array
		j = random.randint(0, i)
		#change the two positions
		deck[i], deck[j] = deck[j], deck[i]

#puts all the cards back into deck and shuffles
def reshuffle():
	global deck, player_hand, dealer_hand
	deck = list(product(suits, values))
	dealer_hand = []
	player_hand = []
	shuffle()


#deal cards
def deal():
	global deck, player_hand, dealer_hand, player_blackjack, dealer_blackjack
	card = deck.pop()
	player_hand.append(card)

	card = deck.pop()
	dealer_hand.append(card)
	
	card = deck.pop()
	player_hand.append(card)
	
	card = deck.pop()
	dealer_hand.append(card)

	if player_hand[0][1] == "A":
		if player_hand[1][1] == "10" or  player_hand[1][1] == "J" or  player_hand[1][1] == "Q" or player_hand[1][1] == "K":
			player_blackjack = True
	elif player_hand[1][1] == "A":
			if player_hand[0][1] == "10" or  player_hand[0][1] == "J" or  player_hand[0][1] == "Q" or player_hand[0][1] == "K":
				player_blackjack = True

	if dealer_hand[0][1] == "A":
		if dealer_hand[1][1] == "10" or  dealer_hand[1][1] == "J" or  dealer_hand[1][1] == "Q" or dealer_hand[1][1] == "K":
			player_blackjack = True
	elif dealer_hand[1][1] == "A":
			if dealer_hand[0][1] == "10" or  dealer_hand[0][1] == "J" or  dealer_hand[0][1] == "Q" or dealer_hand[0][1] == "K":
				dealer_blackjack = True


#player hits
def player_hit():
	global player_hand
	card = deck.pop()
	player_hand.append(card)
	if get_player_hand_sum() > 21: 
		print("Your hand: " + str(get_player_hand()))
		lose()
		end()

#dealer hits until their hand is greater than 16
def dealer_hits():
	global dealer_hand
	if get_dealer_hand_sum() < 16:
		card = deck.pop()
		dealer_hand.append(card)
		dealer_hits()

#player stands and dealer takes his turn and prints results
def stand():
	dealer_hits()


#results of that round
def results():
	if get_dealer_hand_sum() > 21:
		win()
	elif get_player_hand_sum() > get_dealer_hand_sum():
		win()
	elif get_player_hand_sum() == get_dealer_hand_sum():
		if player_blackjack == True and dealer_blackjack == True:
			tie()
		elif player_blackjack == True:
			win()
		elif dealer_blackjack == True:
			lose()
		else:
			tie()
	elif get_player_hand_sum() < get_dealer_hand_sum():
		lose()
	else:
		print("There has been an error :o")
	print("Dealer's hand" + str(get_dealer_hand()))


#ends round loop and/or game loop depending on player's choice
def end():
	global end_round, end_game
	choice = input("\nPress: \n1| Play Again \n2| End Game\n")
	if "1" in choice:
		end_round = True
		new_round()
	else:
		end_round = True
		end_game = True

#starts the round loop after reshuffling
def new_round():
	global end_round, player_blackjack, dealer_blackjack
	reshuffle()
	deal()
	end_round = False
	player_blackjack = False
	dealer_blackjack = False



#prints the result
def lose():
	print("\nYou LOSE")

def win():
	print("\nYou WIN")

def tie():
	print("\nTIE")

#runs through a round
def run():
	 print("Your hand: " + str(get_player_hand()))
	 choice = input("Press: \n1| hit \n2| stand\n")
	 if "1" in choice:
	 	player_hit()
	 else:
	 	stand()
	 	results()
	 	end()

#main function/loop
def main():
	reshuffle()
	deal()
	print("WELCOME TO THE BLACKJACK TEXT GAME")
	while not end_game:
		if not end_round:
			run()



if __name__ == '__main__':
	main()