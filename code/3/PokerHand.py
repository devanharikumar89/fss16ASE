"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
from __future__ import division, print_function
from Card import *



class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def card_hist(self):
        """Builds a histogram of the ranks that appear in the hand with card as key.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card] = self.ranks.get(card.rank, 0) + 1


    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.
        """
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                return True
            else:
                return False

    def has_two_pair(self):
        """Returns True if the hand has two pairs, False otherwise.
        """
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                count+=1
        return count>=2        

    def has_three_of_a_kind(self):
        """Returns True if the hand has three of a kind, False otherwise.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False
        

    def has_straight(self):
        """Returns True if the hand has a straight, False otherwise.
        """
        self.rank_hist()
        card_ranks = self.ranks.keys()
        card_ranks.sort()
        if card_ranks[0]==1:
            card_ranks.append(14)

        prev = card_ranks[0]
        count = 1
        for i in range(1, len(card_ranks)):
            curr = card_ranks[i]
            if curr-prev == 1:
                count+=1
                if count >= 5:
                    return True
            else:
                count=1
            prev=curr
        return False
    
    def has_full_house(self):
        """Returns True if the hand has a full house, False otherwise.
        """
        self.rank_hist()
        
        gteq3 = 0
        eq2 = 0
        for val in self.ranks.values():
            if val >= 3:
                gteq3 += 1
            elif val >= 2:
                eq2+=1
        return gteq3>1 or (gteq3==1 and eq2>=1)

    def has_four_of_a_kind(self):
        """Returns True if the hand has four of a kind, False otherwise.
        """
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val == 4:
                return True
        return False    

    def has_straight_flush(self):
        """Returns True if the hand has a straight flush, False otherwise.
        """
        self.card_hist()
        ranked_cards = self.ranks.keys()
        ranked_cards.sort()

        add_14 = False
        suit_to_add = None
        for card in ranked_cards:
            if card.rank==1:
                suit_to_add = card.suit
                add_14= True

        if add_14:
            ranked_cards.append(Card(suit = suit_to_add, rank = 14))

        ranked_cards.sort()

        prev = ranked_cards[0]
        count = 1
        for i in range(1, len(ranked_cards)):
            curr = ranked_cards[i]
            if curr.suit == prev.suit and curr.rank-prev.rank == 1:
                count+=1
                if count >= 5:
                    return True
            else:
                count=1
            prev=curr
        return False 

    def classify(self):
        """Classifies the pokerhand depending on the highest value of the hand"""
        method_map = {7:self.has_pair, 6:self.has_two_pair, 5:self.has_three_of_a_kind, 4:self.has_straight, 3:self.has_flush, 2:self.has_full_house, 1: self.has_four_of_a_kind, 0:self.has_straight_flush}
        label_map = {0:'STRAIGHT_FLUSH', 1:'FOUR_OF_A_KIND', 2:'FULL_HOUSE', 3:'FLUSH', 4:'STRAIGHT', 5:'THREE_OF_A_KIND', 6:'TWO_PAIR', 7:'PAIR'}
        indices = sorted(method_map.keys())
        for _key in indices:
            if method_map[_key]():
                self.label = label_map[_key]
                print (self.label)
                return
        self.label = 'NONE'

simulation_map = {}
def deal(simulations):
    for _ in xrange(simulations):
        deck = Deck()
        deck.shuffle()
        hand = PokerHand()
        deck.move_cards(hand, 5)
        hand.classify()
        simulation_map[hand.label]=simulation_map.get(hand.label, 0)+1
    #print simulation_map
    for key in simulation_map:
        print (key, " : ", (100*simulation_map[key])/(simulations), "%")

if __name__ == '__main__':
    deal(5000000)



