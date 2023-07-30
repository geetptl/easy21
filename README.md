# Easy21

Assignment from David Silver, Lectures on Reinforcement Learning, 2015, [https://www.davidsilver.uk/teaching/](https://www.davidsilver.uk/teaching/).

----

# Setup

## The Game

Easy21 is a card game, played between the player and the dealer. Cards have values from 1 to 10, and are distinguished by red and black colours, i.e. there are 20 distinct cards. The deck is a replacement deck, which means that after looking at the card, the card goes back into the deck.

Initially, both players are given a random black coloured card.

The player draws a card from a replacement deck, with black card adding and red card subtracting their point values from the player's score. (The draw is called a _HIT_.)

If the score drops below 1 or jumps over 21, the player loses instantly.

Otherwise, at any point, player can choose to _STICK_, which means that now it's the dealer's turn.

The dealer now draws cards (the good ol' _HIT_), keeps the scores the same way, and if their score cross the same boundaries, the player wins on the spot.

At any point dealer can choose to _STICK_, which means the scores are compared. One with the higher score wins.

## Execution

When the player's turn is over, a simple strategy for the dealer is to _STICK_ if the score crosses `17`, _HIT_ otherwise.

Cards are uniformly distributed from 1 to 10, and the frequency for drawing red vs black is weighed `1:2`. This is implemented [here](easy21/game.py) in `Card.__init__` and `Card.score`.

You can play single player mode with the stated dealer by running the following command in this directory.

    `python3 repl.py`