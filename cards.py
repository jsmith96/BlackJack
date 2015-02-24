""" cards.py

author: Jonny Heberer, John H. Smith, A. Y. Cho
github: http://github.com/jrheberer/BlackJack
date: Feb 24 2015
"""

import random


class Card(object):
    """Create Card object with rank and suit"""
    def __init__(self, r=0, s=''):
        self.__rank = r
        self.__suit = s
        self.__hidden = False
        
        if type(r) == str:
            if r in 'Aa':
                self.__rank = 1
            elif r in 'Jj':
                self.__rank = 11
            elif r in 'Qq':
                self.__rank = 12
            elif r in 'Kk':
                self.__rank = 13
        elif type(r) == int:
            if 1 <= r <= 13:
                self.__rank = r

        if type(s) == str and s != '':
            if s in 'Cc':
                self.__suit = 'C'
            elif s in 'Dd':
                self.__suit = 'D'
            elif s in 'Hh':
                self.__suit = 'H'
            elif s in 'Ss':
                self.__suit = 'S'
                
    def get_rank(self):
        """Get Card's rank"""
        return self.__rank
        
    def get_suit(self):
        """Get Card's suit"""
        return self.__suit
        
    def get_hidden(self):
        """Get Card's hidden value (false = face up, true = face down"""
        return self.__hidden
        
#    def get_value(self):
#        """Show card's Black Jack value"""
#        if self.__rank >= 10:
#            return 10
#        else:
#            return self.__rank
        
    def set_face_down(self):
        """Place the card face down on the table, so it is hidden"""
        self.__hidden = True
        
    def set_face_up(self):
        """Place the card race up on the table, so it is not hidden"""
        self.__hidden = False
                    
    def __str__(self):
        """Print the Card as rank and suit. format is 10H.
           ?? means the card does not have coherent valus for rank and suit"""
        if self.__hidden == True:
            return 'XX'
        else:
            card_rank_str  = '?? A 2 3 4 5 6 7 8 9 10 J Q K'
            card_rank_list = card_rank_str.split()
            return (card_rank_list[self.__rank] + self.__suit)
            
    def __repr__(self):
        """Print Card"""
        return self.__str__()


class Deck(object):
    """Create Deck object"""
    def __init__(self, cardlist=[]):
        self.__cards = cardlist
        self.__drawn = []

    def show_cards(self):
        """Show the cards in the deck"""
        return self.__cards

    def show_drawn_cards(self):
        """Show the cards drawn from the deck"""
        return self.__drawn

    def shuffle(self, n=1):
        """Shuffle the deck n times"""
        for _ in range(n):
            random.shuffle(self.__cards)

    def draw(self, n=1):
        """Draw n cards from the deck"""
        drawn_card_list = []
        for _ in range(n):
            drawn_card = self.__cards.pop(0)
            drawn_card_list.append(drawn_card)
            self.__drawn.append(drawn_card)
        return drawn_card_list

    def size(self):
        """Find the number of cards in the deck"""
        return len(self.__cards)

    def reshuffle(self):
        """Shuffle the discard pile and add to the bottom of the deck"""
        random.shuffle(self.__drawn)
        self.__cards += self.__drawn
        self.__drawn = []

def create_cards():
    all_ranks = range(1, 14)
    all_suits = ['H', 'D', 'C', 'S']
    full_deck = [Card(rank, suit) for suit in all_suits for rank in all_ranks]
    return Deck(full_deck)

class BlackjackPlayer(object):
    """Create a Blackjack Player"""
    def __init__(self, h = []):
        self.__hand = h
        self.__stay = False
        self.__bust = False

    def hit(self, deck):
        """The player takes a hit (is dealt a card)"""
        self.__hand += deck.draw()

    def stay(self):
        """The player chooses to stay (receives no more cards this round)"""
        self.__stay = True

    def busted(self):
        """blah"""
        self.__bust = True

    def get_hand(self):
        """Get the cards from the player's hand"""
        return self.__hand

    def get_stay(self):
        """Find if the player choose to stay"""
        return self.__stay

    def reset(self):
        """Clears hand to start a new round"""
        self.__hand = []
        self.__stay = False

class Blackjack(object):
    """Starts a game of Blackjack"""
    def __init__(self,players=1, deck = create_cards()):
        self.__players = [BlackjackPlayer() for _ in range(players)]
        self.__deck = deck.shuffle()

    def set_bust(self, player):
        """Determines if the player is bust"""
        hand = player.get_hand()
        ranks = [card.get_rank for card in hand]
        values = [rank if rank < 11 else 10 for rank in ranks]
        score = sum(values)
        if score > 21:
            player.busted()
   
