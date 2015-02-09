# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 19:50:02 2015

@author: Jonny
"""

class Card(object):
    """Create Card object with rank and suit"""
    def __init__(self,r=0,s=''):
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
                
        if type(s) ==str and s!='':
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
        
    def get_value(self):
        """Show card's Black Jack value"""
        if self.__rank >= 10:
            return 10
        else:
            return self.__rank
        
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
            card_rank_str = '?? A 2 3 4 5 6 7 8 9 10 J Q K'
            card_rank_list = card_rank_str.split()
            return (card_rank_list[self.__rank] + self.__suit)
            
    def __repr__(self):
        """Print Card"""
        return self.__str__()