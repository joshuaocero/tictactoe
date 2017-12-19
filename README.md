# tictactoe

This is an API implementation of the game TicTacToo.

Current implementation follows the Center strategy described by Arjun Subramaniam on Quora (https://www.quora.com/Is-there-a-way-to-never-lose-at-Tic-Tac-Toe)

The API is not fully functional but the following bits and pieces are working right now:

* API can apply finishing move to end the game
* API can play second move if oponent marked an edge as described on quora

## Assumptions(that must be in place) according to the center strategy

* API started first with 'o' in the center
* Opponent marked an edge and not a corner
