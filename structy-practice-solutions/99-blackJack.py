'''
BLACKJACK HIGHEST

Basic Blackjack rules:
1. Cards with the numbers 2 through 10 have their face value.
2. Jacks, queens, and kings are valued at 10 points.
3. Aces can be 1 or 11 points.

Have the function BlackjackHighest(strArr) take the strArr parameter being passed 
which will be an array of numbers and letters representing blackjack cards. 
Numbers in the array will be written out. 
So for example strArr may be ["two","three","ace","king"]. 

The full list of possibilities for 
strArr is: two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace. 

Your program should output below, above, or blackjack signifying if you have blackjack (numbers add up to 21) or not and the highest card in your hand in relation to whether or not you have blackjack. 
If the array contains an ace but your hand will go above 21, you must count the ace as a 1. 
You must always try and stay below the 21 mark. 
So using the array mentioned above, the output should be below king. 
The ace is counted as a 1 in this example because if it wasn't you would be above the 21 mark.

Another example would be if strArr was ["four","ten","king"], the output here should be above king. 
If you have a tie between a ten and a face card in your hand, return the face card as the "highest card". 
If you have multiple face cards, the order of importance is jack, queen, king.

Examples
Input: ["four","ace","ten"]
Output: below ten
Input: ["ace","queen"]
Output: blackjack ace

'''

def BlackjackHighest(strArr):
  cards_list = ['ace','two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
  cards_values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  hand_values = []
  highest_card_rank = 0
  ace_in_deck = False

  for card in strArr:
    index_of_card = cards_list.index(card)
    if card == 'ace':
      ace_in_deck = True
    if index_of_card > highest_card_rank:
      highest_card_rank = index_of_card
    hand_values.append(cards_values[cards_list.index(card)])

  total_hand = sum(hand_values)
  if ace_in_deck==True and total_hand == 21:
    return 'blackjack'+' '+'ace'
  elif ace_in_deck==False and total_hand == 21:
    return 'blackjack'+' '+cards_list[highest_card_rank]
  elif ace_in_deck==True and total_hand > 21:
    total_hand-=10 #adjusting ace value to 1
    if total_hand < 21:
      return 'below'+' '+cards_list[highest_card_rank]
    else:
      return 'above'+' '+cards_list[highest_card_rank]
  elif ace_in_deck==True and total_hand < 21:
    return 'below'+' '+'ace'
  elif ace_in_deck==False and total_hand > 21:
    return 'above'+' '+cards_list[highest_card_rank]
  elif ace_in_deck==False and total_hand < 21:
    return 'below'+' '+cards_list[highest_card_rank]
  else:
    return 'Missed'
    
# keep this function call here 
print(BlackjackHighest(["ten","seven","three"]))
#Input: ["ten","seven","three"]
#Ans. Below ten
