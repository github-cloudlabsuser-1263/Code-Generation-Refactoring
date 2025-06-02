# Intentionally flawed Python program
"""
This script simulates drawing five random cards from a standard 52-card deck.

Modules:
   itertools: Used to generate the full deck of cards as combinations of ranks and suits.
   random: Used to shuffle the deck for randomness.

Process:
   - Creates a deck of cards as tuples of (rank, suit).
   - Shuffles the deck randomly.
   - Draws and prints five cards from the top of the shuffled deck.
"""

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
