print(' _______________________________________________________________ ')
print("|  _____  _  ____     _____  ____  ____     _____  ____  _____  |")
print("| /__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/  |")   
print("|   / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \    |")  
print("|   | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_   |") 
print("|   \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\  |")
print('|_______________________________________________________________|\n')
print(20*' ',"   reference:    ")
print(20*' ','     |    |      ') 
print(20*' ','  1  | 2  | 3    ')
print(20*' ',"-----+----+----- ")
print(20*' ',"     |    |      ")
print(20*' ',"  4  | 5  | 6    ")
print(20*' ',"-----+----+----- ")
print(20*' ',"     |    |      ")
print(20*' ',"  7  | 8  | 9    \n")
print('RULES:')
print("Only 2 players can play this game\nPlayer-1:x\nPlayer-2:y\nEnter the numbers in the box to place [x or o] in that place\n!!!HAVE FUN!!! ")

def display_board():
    print()
    print('                               reference:')
    print('     |    |     ',10*' ','     |    |   ',)
    print('  '+board[1]+'  | '+board[2]+'  | '+board[3]+'   ',10*' ','  1  | 2  | 3  ')
    print('-----+----+-----',10*' ',"-----+----+-----")
    print('     |    |     ',10*' ',"     |    |     ")
    print('  '+board[4]+'  | '+board[5]+'  | '+board[6]+'   ',10*' ',"  4  | 5  | 6   ")
    print('-----+----+-----',10*' ',"-----+----+-----")
    print('     |    |     ',10*' ',"     |    |      ")
    print('  '+board[7]+'  | '+board[8]+'  | '+board[9]+'   ',10*' ',"  7  | 8  | 9    \n\n")
        
def x_input():
    while True:
        x = input("[X] Enter your choice:")
        if x.isdigit() and int(x) <10 and int(x) >0:
            x = int(x)
            if board[x] == " ":
                return x
            else:
                print('[X] place already taken.')
        else:
            print('[x] Enter valid option (1 - 9).')    
def o_input():
    while True:
        o = input("[O] Enter your choice:")
        if o.isdigit() and int(o) <10 and int(o) >0:
            o = int(o)
            if board[o] == " ":
                return o            
            else:
                print('[O] place already taken.')
        else:
            print('[O] Enter valid option (1 - 9).')              
def win_check():
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == 'x':
            print('[X] wins the match!')
            if not new_game():
                return False
        elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == 'o':
                print('[O] wins the match!')
                if not new_game():
                    return False
    if ' ' not in board:
        print('MATCH DRAW!!')
        if not new_game():
            return False
    return True

def new_game():
    while True:
        nxt = input('Do you want to play again?(y/n):')
        if nxt in['y','Y']:
            again = True
            break
        elif nxt in ['n','N']:
            print('Have a great day')
            again = False
            break
        else:
            print('Enter correct input')
    if again:
        play = True
        print('__________NEW GAME__________')
        main_game()
    else:
        return False

def main_game():
    global board,winning_place
    # variables declaration
    play = True
    board=['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    display_board()
    # main loop
    while play:
        x = x_input()
        board[x] = 'x'
        display_board()
        play = win_check()
        if play:
            o = o_input()
            board[o] = 'o'
            display_board()
            play = win_check()          

# Initialization           
if __name__ == '__main__':        
    main_game()            
        
