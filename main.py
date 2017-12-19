import re

from flask import Flask
from flask import request

app = Flask(__name__)

def get_setup_position(board):
    # Remember according to the algorithm, select the furthest position
    if len([m.start() for m in re.finditer('o', board)]) != 1 and len([m.start() for m in re.finditer('x', board)]) != 1:
        # This aint setup stage
        return -1
  
    if board[4] != 'o':
        # This aint the algorithm
        return -1

    if board[3] == 'x' or board[7] == 'x':
        return 2
    if board[5] == 'x' or board[1] == 'x':
        return 6

def get_strike_position(board):
    for i in range (1,4):
        # Check the position of the o's
        positions = [m.start() for m in re.finditer('o', board)]

        if (len(positions) == 2):
            # Check if two positions are close to each other
            if ((positions[1]-positions[0])==i):
                if ((positions[0]-i) >= 0 and board[positions[0]-i] == ' '):
                    return positions[0]-i
                if ((positions[0]+i) <= 8 and board[positions[1]+i] == ' '):
                    return positions[1]+i

            # What if its in the middle
            if ((board[positions[0]+i] == ' ') and 
                (board[positions[1]-i] == ' ')):
                return positions[0]+i
    return -1

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

@app.route("/", methods=['GET'])
def board():
    board = request.args['board']
    # Outline steps #

    # check if board is valid
    if re.search("[^ox ]", board) or len(board) < 9:
        return "Bad Request", 400

    # check whose turn it is
    our_plays = len([m.start() for m in re.finditer('o', board)])
    their_plays = len([m.start() for m in re.finditer('x', board)])
    if our_plays > their_plays:
        return "Bad Request", 400

    # Using the center algorithm (only works if you start first)
    ## (https://www.quora.com/Is-there-a-way-to-never-lose-at-Tic-Tac-Toe)

    # start with the obvious :: win when possible
    ## check for two aligned o's and strike
    strike_pos = get_strike_position(board)
    if strike_pos >= 0:
        board = replace_str_index(board, strike_pos, 'o')
        return board

    # setup your win
    ## this should be your second move
    setup_pos = get_setup_position(board)
    if setup_pos >= 0:
        board = replace_str_index(board, setup_pos, 'o')
        return board

    return board
