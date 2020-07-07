import sys
from player import Player 

board = [['.']*3 for i in range(3)]
player_list = [Player("1", "X"), Player("2", 'O')]
possible_wins = [
                    [[0,0], [0,1], [0,2]],
                    [[1,0], [1,1], [1,2]],
                    [[2,0], [2,1], [2,2]],
                    [[0,0], [1,0], [2,0]],
                    [[0,1], [1,1], [2,1]],
                    [[0,2], [1,2], [2,2]],
                    [[0,0], [1,1], [2,2]],
                    [[0,2], [1,1], [2,0]]
                ]
def main():
    current_round = 1
    complete = 0
    print("Welcome to Tic Tac Toe!\n")
    print("Here's the current board:\n")
    display_board()
    while complete == 0 and current_round <= 9:
        print("Player " + player_list[current_round%2 - 1].get_number() + " enter a coord x,y to place your " + player_list[current_round%2 - 1].get_character() + " or enter 'q' to give up: ", end="")
        coord = input()
        print()
        if coord == 'q':
            print("You have ended the game")
            return
        else:
            x = int(coord[0])
            y = int(coord[2])
            if (x >= 1 or x <= 3) and (y >= 1 or y <= 3):
                if (check_board(x-1, y-1)):
                    board[x-1][y-1] = player_list[current_round%2 - 1].get_character()
                    winner = check_win(player_list[current_round%2 - 1].get_character())
                    if (winner == False):
                        print("Move accepted, here's the current board: ")
                    else:
                        print("Move accepted, well done you've won the game!")
                        complete = 1
                    display_board()
                    current_round += 1
                else:
                    print("Oh no, a piece is already at this place! Try again...")
            else:
                print("This coordinate doesn't exist. Try again...")
    if current_round > 9:
        print("Sorry, there are no winners")

def check_board(x, y):
    if (board[x][y] == '.'):
        return True
    else:
        return False

def check_win(character):
    for y in possible_wins:
        winner = True
        for x in y:
            if board[x[0]][x[1]] == character:
                continue
            else:
                winner = False
                break
        if winner == True:
            return winner
    return winner

def display_board():
    for x in range(3):
        for y in range(3):
            if y == 2:
                print(board[x][y])
            else:
                print(board[x][y], end = '')
    print()

if __name__ == "__main__":
    main()