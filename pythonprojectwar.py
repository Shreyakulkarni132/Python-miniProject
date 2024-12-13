#GAME OF WAR

import random
# Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):  # Multiple cards
            self.all_cards.extend(new_cards)
        else:  # Single card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} cards."


# Game Setup
print("Welcome to the Card Game!")
player_one_name = input("Enter Player One's name: ")
player_two_name = input("Enter Player Two's name: ")

player_one = Player(player_one_name)
player_two = Player(player_two_name)

new_deck = Deck()
new_deck.shuffle()

# Distribute cards
for _ in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

# Game Loop
while game_on:
    round_num += 1
    print(f"\n--- Round {round_num} ---")
    print(player_one)
    print(player_two)

    # Check if a player has run out of cards
    if len(player_one.all_cards) == 0:
        print(f"{player_one.name} is out of cards! {player_two.name} wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print(f"{player_two.name} is out of cards! {player_one.name} wins!")
        game_on = False
        break

    # Start a new round
    player_one_cards = [player_one.remove_one()]
    player_two_cards = [player_two.remove_one()]

    print(f"{player_one.name} plays: {player_one_cards[-1]}")
    print(f"{player_two.name} plays: {player_two_cards[-1]}")

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            print(f"{player_one.name} wins the round!")
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            print(f"{player_two.name} wins the round!")
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print("It's a WAR!")
            if len(player_one.all_cards) < 5:
                print(f"{player_one.name} cannot declare war! {player_two.name} wins!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print(f"{player_two.name} cannot declare war! {player_one.name} wins!")
                game_on = False
                break
            else:
                print("Drawing 5 cards for war...")
                for _ in range(5):
                    if len(player_one.all_cards) > 0:
                        player_one_cards.append(player_one.remove_one())
                    if len(player_two.all_cards) > 0:
                        player_two_cards.append(player_two.remove_one())

    # Ask if players want to continue
    if game_on:
        continue_game = input("Do you want to play the next round? (yes/no): ").lower()
        if continue_game != 'yes':
            print("Thank you for playing, hope you enjoyed \nXOXO ")
            game_on = False
