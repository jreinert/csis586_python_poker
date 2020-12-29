#Author: Jeremy Reinert
#Date: 1/31/2020
#Version: 1.0


#hw2-reinert.py
"""Deals two hands of five cards from a 52 card deck and determines winning poker hand"""
#Import Modules
import random

#Functions
#Init, deal, and print functions
def initialize_deck(suit, face, deck):
    """Initializes card deck from suit and face lists passed as parameters"""
    for f in face:
        for s in suit:
            deck += (f, s),

def print_deck(deck):
    """Prints cards from card deck"""
    number_columns = 4
    count = 0
    
    for face, suit in deck:
        print(f'{face} of {suit}', end=' ')
        count += 1
        
        if count == number_columns:
            print()
            count = 0

def print_hand(hand):
    """Prints formatted hand to console"""
    print('[', end = '')
    for i in hand:
        if hand.index(i) < len(hand) - 1:
            print(f'{i[0]} of {i[1]}, ', end = '')
        else:
            print(f'{i[0]} of {i[1]}', end = '')
    print(']')
    print(' ')    
    
def deal_cards(deck, hand_one, hand_two):
    """Uses random module shuffle function to shuffle cards a random number of times and deals two hands of five cards"""   
    random.shuffle(deck)
    hand_one += deck[0:5]
    del deck[0:5]
    hand_two += deck[0:5]

#Hand evaluation functions
def one_pair(hand, face):
    """Searches for a pair in hand passed and returns True if one is found"""
    face_values_in_hand = []
    for i in hand:
        face_values_in_hand.append(i[0])
        
    for value in face:
        if face_values_in_hand.count(value) == 2:
            return True
        
    return False        
    
def two_pairs(hand, face):
    """Counts and returns True if two pairs are found in the hand passed"""
    face_values_in_hand = []
    two_pair = 0
    for i in hand:
        face_values_in_hand.append(i[0])
        
    for value in face:
        if face_values_in_hand.count(value) == 2:
            two_pair += 1
    
    if two_pair > 1:
        return True
    
    return False

def three_of_a_kind(hand, face):
    """Counts and returns True if there is a three of a kind in the hand"""
    face_values_in_hand = []
    for i in hand:
        face_values_in_hand.append(i[0])
        
    for value in face:
        if face_values_in_hand.count(value) == 3:
            return True
    
    return False

def four_of_a_kind(hand, face):
    """Counts and returns True if there is a four of a kind in the hand"""
    face_values_in_hand = []
    for i in hand:
        face_values_in_hand.append(i[0])
        
    for value in face:
        if face_values_in_hand.count(value) == 4:
            return True
    
    return False
 
def flush(hand, suit):
    """Counts cards suits and returns True if there are five of a kind in the hand"""
    suits_in_hand = []
    for i in hand:
        suits_in_hand.append(i[1])
        
    for s in suit:
        if suits_in_hand.count(s) == 5:
            return True    
    
    return False

def full_house(hand, face):
    """Calls one_pair and three_of_a_kind functions and returns True if both return True"""
    if one_pair(hand, face) == True and three_of_a_kind(hand, face) == True:
        return True
    
    return False

def straight(hand, face):
    """Evaluates hand for 5 sequential face values and returns True if found"""
    #Init empty lists for function use
    face_values_in_hand = []
    sequences = []
    
    #Append face values to sequences list
    for i in face:
        sequences.append(i)
    sequences.append('Ace')
    
    #Append vace values in hand to face_values_in_hand list
    for i in hand:
        face_values_in_hand.append(i[0])
 
    #Sort face_values_in_hand, init empty hand_face string var, and add element in face_values_in_hand list to hand_face string
    face_values_in_hand = sorted(face_values_in_hand)
    hand_face = ''
    for i in face_values_in_hand:
        hand_face += i    
    
    while len(sequences) > 4:
        #Sort sequences, init empty seq_face string var, set seq_split equal to elements sequence[0:5], and add elements in seq_split to seq_face string
        seq_face = ''
        seq_split = sequences[0:5]
        seq_split = sorted(seq_split)
        for i in seq_split:
            seq_face += i
        
        #Compare seq_face with hand_face and return True if equal -- else, delete element at sequences[0] and loop again
        if seq_face == hand_face:
            return True
        else:
            del sequences[0]
        
    return False

def straight_flush(hand, face, suit):
    """Calls straight and flush functions and returns True if both return True"""
    if straight(hand, face) == True and flush(hand, suit) == True:
        return True
    
    return False

def high_card(hand):
    """Evaluates hand for its highest card and returns it to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    high_card_val = 0
    high_card = ''
    
    for i in hand:
        for j in face:
            if i[0] == j[0] and high_card_val < j[1]:
                high_card_val = j[1]
                high_card = f'{i[0]} of {i[1]}'
    
    return high_card

def high_card_2(hand):
    """Evaluates hand for its highest card and returns it to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    high_card_val = 0
    high_card = ''
    
    for i in hand:
        for j in face:
            if i[0] == j[0] and high_card_val < j[1]:
                high_card_val = j[1]
                high_card = i[0]
    
    return high_card

def high_card_val(hand):
    """Evaluates hand for its highest card and returns its value to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    high_card_val = 0
    
    for i in hand:
        for j in face:
            if i[0] == j[0] and high_card_val < j[1]:
                high_card_val = j[1]
    
    return high_card_val

def high_card_val_2(hand):
    """Evaluates hand for its highest card and returns its value to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    high_card_val = 0
    
    for i in hand:
        for j in face:
            if i == j[0] and high_card_val < j[1]:
                high_card_val = j[1]
    
    return high_card_val

def high_card_straight(hand):
    """Evaluates hand for its highest card value and returns it to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    high_card_val = 0
    face_values_in_hand = []
    
    for i in hand:
        face_values_in_hand.append(i[0])
        
    if 'Ace' in face_values_in_hand and 'Four' in face_values_in_hand:
        high_card_val = 4
        return high_card_val
    
    for i in hand:
        for j in face:
            if i[0] == j[0] and high_card_val < j[1]:
                high_card_val = j[1]
    return high_card_val

def high_card_full_house(hand):
    """Evalutes hand for its highest card value and returns it to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    high_card_val = 0
    face_values_in_hand = []
    
    for i in hand:
        face_values_in_hand.append(i[0])
    
    for i in face_values_in_hand:
        if face_values_in_hand.count(i) == 3:
            for j in face:
                if i == j[0] and high_card_val < j[1]:
                    high_card_val = j[1]
    
    return high_card_val

def high_card_pairs(hand):
    """Evaluates hand for its highest card value and returns it to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    hand_val = 0
    face_values_in_hand = []
    
    for i in hand:
        face_values_in_hand.append(i[0])
    
    for i in face_values_in_hand:
        for j in face:
            if i == j[0]:
                hand_val += j[1]
    
    return hand_val

def evaluate_hand(hand, face, suit):
    
    #Init hand_rank var and set to empty string
    hand_rank = ' '
      
    #Evaluate hand for hand value and set hand_rank to value if True returned
    if high_card(hand) != '':
        hand_rank = high_card(hand)
    
    if one_pair(hand, face) == True:
        hand_rank = 'One Pair'
    
    if two_pairs(hand, face) == True:
        hand_rank = 'Two Pairs'
    
    if three_of_a_kind(hand, face) == True:
        hand_rank = 'Three of a Kind'
        
    if straight(hand, face) == True:
        hand_rank = 'Straight'
        
    if flush(hand, suit) == True:
        hand_rank = 'Flush'
        
    if full_house(hand, face) == True:
        hand_rank = 'Full House'
        
    if four_of_a_kind(hand, face) == True:
        hand_rank = 'Four of a Kind'
        
    if straight_flush(hand, face, suit) == True:
        hand_rank = 'Straight Flush'
    
    #Return hand_rank to function call    
    return hand_rank

# Tie breaker functions
def tie_break_straight(hand_one, hand_two):
    """Determines which hand has the higher highest card to break the tie"""
    if high_card_straight(hand_one) > high_card_straight(hand_two):
        print('Hand One wins!!!')
    elif high_card_straight(hand_two) > high_card_straight(hand_one):
        print('Hand Two wins!!!')
    else:
        print('Tie. No winners!!!')

def tie_break_four_of_a_kind(hand_one, hand_two):
    """Determines which hand has the higher face value in their respective four of a kind"""
    high_card_val_hand_one = 0
    high_card_face_hand_one = ''
    high_card_val_hand_two = 0
    high_card_face_hand_two = ''
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    face_values_in_hand_one = []
    face_values_in_hand_two = []
    
    for i in hand_one:
        face_values_in_hand_one.append(i[0])
    
    for i in hand_two:
        face_values_in_hand_two.append(i[0])
    
    for i in face_values_in_hand_one:
        if face_values_in_hand_one.count(i) == 4:
            high_card_face_hand_one = i
            
    for i in face_values_in_hand_two:
        if face_values_in_hand_two.count(i) == 4:
            high_card_face_hand_two = i
            
    for i in face:
        if i[0] == high_card_face_hand_one:
            high_card_val_hand_one = i[1]
        
        if i[0] == high_card_face_hand_two:
            high_card_val_hand_two = i[1]
    
    if high_card_val_hand_one > high_card_val_hand_two:
        print('Hand One wins!!!')
    elif high_card_val_hand_two > high_card_val_hand_one:
        print('Hand Two wins!!!')

def tie_break_three_of_a_kind(hand_one, hand_two):
    """Determines which hand has the higher face value in their respective four of a kind"""
    high_card_val_hand_one = 0
    high_card_face_hand_one = ''
    high_card_val_hand_two = 0
    high_card_face_hand_two = ''
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    face_values_in_hand_one = []
    face_values_in_hand_two = []
    
    for i in hand_one:
        face_values_in_hand_one.append(i[0])
    
    for i in hand_two:
        face_values_in_hand_two.append(i[0])
    
    for i in face_values_in_hand_one:
        if face_values_in_hand_one.count(i) == 3:
            high_card_face_hand_one = i
            
    for i in face_values_in_hand_two:
        if face_values_in_hand_two.count(i) == 3:
            high_card_face_hand_two = i
            
    for i in face:
        if i[0] == high_card_face_hand_one:
            high_card_val_hand_one = i[1]
        
        if i[0] == high_card_face_hand_two:
            high_card_val_hand_two = i[1]
    
    if high_card_val_hand_one > high_card_val_hand_two:
        print('Hand One wins!!!')
    elif high_card_val_hand_two > high_card_val_hand_one:
        print('Hand Two wins!!!')

def tie_break_flush(hand_one, hand_two):
    """Determines which hand has the higher highest card to break the tie"""
    hand_one_high_card = high_card_val(hand_one)
    hand_two_high_card = high_card_val(hand_two)
    
    if hand_one_high_card > hand_two_high_card:
        print("Hand One wins!!!")
    elif hand_two_high_card > hand_two_high_card:
        print("Hand Two wins!!!")
 
def tie_break_full_house(hand_one, hand_two):
    """Determines which hand has the higher face value in its set of triplets"""
    hand_one_high_card = high_card_full_house(hand_one)
    hand_two_high_card = high_card_full_house(hand_two)
    
    if hand_one_high_card > hand_two_high_card:
        print("Hand One wins!!!")
    elif hand_two_high_card > hand_two_high_card:
        print("Hand Two wins!!!")

def tie_break_pairs(hand_one, hand_two):
    """Evaluates hands for highest hand and determines winner"""
    hand_one_val = high_card_pairs(hand_one)
    hand_two_val = high_card_pairs(hand_two)
    
    if hand_one_val > hand_two_val:
        print('Hand One wins!!!')
    elif hand_two_val > hand_one_val:
        print('Hand Two wins!!!')

def tie_break_pair(hand_one, hand_two):
    """Removes pair from hand, finds high kicker and returns winner"""
    hand_one_copy = []
    hand_two_copy = []
    hand_one_pair_face = ''
    hand_two_pair_face = ''
    hand_one_high_card_val = 0
    hand_two_high_card_val = 0
    face_values_in_hand_one = []
    face_values_in_hand_two = []
    
    #copy face values into new lists
    for i in hand_one:
        face_values_in_hand_one.append(i[0])
    
    for i in hand_two:
        face_values_in_hand_two.append(i[0])
        
    #find face values of pair
    for i in face_values_in_hand_one:
        if face_values_in_hand_one.count(i) == 2:
            hand_one_pair_face = i
            
    for i in face_values_in_hand_two:
        if face_values_in_hand_two.count(i) == 2:
            hand_two_pair_face = i
    
    #copy only pairs into list
    for i in face_values_in_hand_one:
        if i == hand_one_pair_face:
            hand_one_copy.append(i)
            
    for i in face_values_in_hand_two:
        if i == hand_two_pair_face:
            hand_two_copy.append(i)
            
    #pass hand copy to high_card_val_2 and determine winner
    hand_one_high_card_val = high_card_val_2(hand_one_copy)
    hand_two_high_card_val = high_card_val_2(hand_two_copy)
    
    if hand_one_high_card_val > hand_two_high_card_val:
        print('Hand One wins!!!')
    elif hand_two_high_card_val > hand_one_high_card_val:
        print('Hand Two wins!!!')
    else:
        #delete elements in hand copy lists
        del hand_one_copy[:]
        del hand_two_copy[:]
        
        #append all items but pairs into lists
        for i in face_values_in_hand_one:
            if i == hand_one_pair_face:
                continue
            else:
                hand_one_copy.append(i)
                
        for i in face_values_in_hand_two:
            if i == hand_two_pair_face:
                continue
            else:
                hand_two_copy.append(i)
        
        #pass hand copy to high_card_val_2 and determine winner
        hand_one_high_card_val = high_card_val_2(hand_one_copy)
        hand_two_high_card_val = high_card_val_2(hand_two_copy)

        if hand_one_high_card_val > hand_two_high_card_val:
            print('Hand One wins!!!')
        elif hand_two_high_card_val > hand_one_high_card_val:
            print('Hand Two wins!!!')

def tie_break_high_card(hand_one, hand_two):
    """Evaluates each hand to find second highest card in each and determine winner"""
    high_card_hand_one = high_card_2(hand_one)
    high_card_hand_two = high_card_2(hand_two)
    hand_one_copy = []
    hand_two_copy = []
    
    print(high_card_hand_one)
    print(high_card_hand_two)
    
    for i in hand_one:
        if i[0] == high_card_hand_one:
            continue
        else:
            hand_one_copy.append(i)
    
    for i in hand_two:
        if i[0] == high_card_hand_two:
            continue
        else:
            hand_two_copy.append(i)
    
    high_card_hand_one_val = high_card_val(hand_one_copy)
    high_card_hand_two_val = high_card_val(hand_two_copy)
    
    if high_card_hand_one_val > high_card_hand_two_val:
        print('Hand One wins!!!')
    elif high_card_hand_two_val > high_card_hand_one_val:
        print('Hand Two wins!!!')
    else:
        print('Tie. Logic only goes to first kicker card')
    
        
def compare_hands(hand_one, hand_two, face, suit):
    """Calls evaluate_hand function and determines winning hand"""
    #Vars and list for evaluating and comparing hand values
    hand_one_rank_val = 0
    hand_two_rank_val = 0
    hand_ranks =[('One Pair', 1), ('Two Pairs', 2), ('Three of a Kind', 3), ('Straight', 4), ('Flush', 5), ('Full House', 6), ('Four of a Kind', 7), ('Straight Flush', 8)]
    
    #hand_one evaluation
    hand_one_rank = evaluate_hand(hand_one, face, suit)
    print(f'Hand One: {evaluate_hand(hand_one, face, suit)}')
    print_hand(hand_one)
    
    #hand_two evaluation
    hand_two_rank = evaluate_hand(hand_two, face, suit)
    print(f'Hand Two: {evaluate_hand(hand_two, face, suit)}')
    print_hand(hand_two)
    
    #Obtain hand values
    for i in hand_ranks:
        if i[0] == hand_one_rank:
            hand_one_rank_val = i[1]
        if i[0] == hand_two_rank:
            hand_two_rank_val = i[1]

    #Determine who wins 
    if hand_one_rank_val == 0 and hand_two_rank_val == 0:
        if high_card_val(hand_one) > high_card_val(hand_two):
            print('Hand One wins!!!')
        elif high_card_val(hand_two) > high_card_val(hand_one):
            print('Hand Two wins!!!')
        elif high_card_val(hand_one) == high_card_val(hand_two):
            tie_break_high_card(hand_one, hand_two)
    elif hand_one_rank_val > hand_two_rank_val:
        print('Hand One wins!!!')
    elif (hand_two_rank_val > hand_one_rank_val):
        print('Hand Two wins!!!')
    elif hand_one_rank_val == 4 and hand_two_rank_val == 4:
        tie_break_straight(hand_one, hand_two)
    elif hand_one_rank_val == 8 and hand_two_rank_val == 8:
        tie_break_straight(hand_one, hand_two)
    elif hand_one_rank_val == 7 and hand_two_rank_val == 7:
        tie_break_four_of_a_kind(hand_one, hand_two)
    elif hand_one_rank_val == 3 and hand_two_rank_val == 3:
        tie_break_three_of_a_kind(hand_one, hand_two)
    elif hand_one_rank_val == 5 and hand_two_rank_val == 5:
        tie_break_flush(hand_one, hand_two)
    elif hand_one_rank_val == 6 and hand_two_rank_val == 6:
        tie_break_full_house(hand_one, hand_two)
    elif hand_one_rank_val == 2 and hand_two_rank_val == 2:
        tie_break_pairs(hand_one, hand_two)
    elif hand_one_rank_val == 1 and hand_one_rank_val == 1:
        tie_break_pair(hand_one, hand_two)
                
        
#Init lists containing suits and card faces
suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
face = ['Ace', 'Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

number_of_plays = input('How many times do you want to play?')
is_num = False

while is_num == False:
    if number_of_plays.isdigit():
        number_of_plays = int(number_of_plays)
        is_num = True
    else:
        number_of_plays = input('You did not enter a valid number. Please enter the number of times you want to play.')

num_played = 1
while num_played <= number_of_plays:
    print()
    print(f'This is play number {num_played}:')
    #Init empty deck and hand lists
    deck = []
    hand_one = []
    hand_two = []
    
    #Call initialize_deck function to create deck of cards
    initialize_deck(suit, face, deck)
    
    #Call deal_cards function to deal shuffle deck and two hands of 5 cards
    deal_cards(deck, hand_one, hand_two)
    
    #Call compare_hands function to determine winning card -- other functions called from within this function
    compare_hands(hand_one, hand_two, face, suit)
    
    num_played += 1
        
        




