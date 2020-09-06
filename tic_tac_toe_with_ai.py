
def human_move():
    while True:
            try:
                move = int(input("Make your move human(1-9): "))
                if isValid(move) and is_position_free(move):
                    insert_move(move,"x")
                    break
                else:
                    print("Please insert different number")
            except:
                print("Make a valid move")

def insert_move(move,player):
    if move == 0:
        print("Game is a tie")
    board[move]=player
    print("{} in position {}".format(player,move))
    print_board(board)

def print_board(board):
    print(" "+board[1]+" | "+board[2]+ " | "+board[3]) 
    print("__________")
    print(" "+board[4]+" | "+board[5]+ " | "+board[6])
    print("__________")
    print(" "+board[7]+" | "+board[8]+ " | "+board[9])


def is_position_free(move):
    if board[move] == " ":
        print(board[move])
        return True

def victory_check(board,player):
    if (board[1]==player and board[2]==player and board[3]==player) or (board[4]==player and board[5]==player and board[6]==player) or (board[7]==player and board[8]==player and board[9]==player) or  (board[1]==player and board[4]==player and board[7]==player) or (board[2]==player and board[5]==player and board[8]==player) or (board[3]==player and board[6]==player and board[9]==player) or(board[1]==player and board[5]==player and board[9]==player) or (board[3]==player and board[5]==player and board[7]==player):
        return True

    return False

    
def computer_move():
    move = 0
    avail_pos=[ind for ind,val in enumerate(board) if val == " " and ind !=0]
    print(avail_pos)
    for i in ['o','x']:
        for j in avail_pos :
            board_copy= board[:]
            board_copy[j]=i
            if victory_check(board_copy,i):
                move = j
                return insert_move(move,'o')
    if 5 in avail_pos:
        move = 5
        return insert_move(move,'o')   
    corners_list=[]   
    for corners in avail_pos:
        if corners in [1,3,7,9]:
            corners_list.append(corners)
    if len(corners_list)>0:
        move = randomMove(corners_list)
        return insert_move(move,'o')
    edge_list=[]
    for edges in avail_pos:
        if edges in [2,4,6,8]:
            edge_list.append(edges)
    if len(edge_list)>0:
        move = randomMove(edge_list)
        return insert_move(move,'o')

    

def isBoardFull(board):
    if board.count(" ")==1:
        return True 

def randomMove(li):
    import random
    x= random.choice(li)
    return x


def isValid(move):

    if move > 0 and move < 10 :
        return True
    else:
        return print("Make a valid move human")

def main():
    global board
    board = [" " for i in range(10)]
    print("Welcome to the game of TIC-TAC-TOE Against a manual coded AI \n") 
    print_board(board)
    while not(isBoardFull(board)):
        if not victory_check(board,"o"):          
            human_move()
        else:
            print("Computer Wins")
            break
        if not victory_check(board,"x"):
            computer_move()
        else:
             print("Human Wins")
             break

    if isBoardFull(board):
        print("Game is a Tie")
            
                
       
main()