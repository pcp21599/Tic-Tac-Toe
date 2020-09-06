
def take_input(player_name,e_val):
    player_val = int(input('Make a move {}: '.format(player_name)))
    if (int(player_val) < 10 ) and (int(player_val) > 0) and (player_val not in e_val):
        return player_val
    else:
        return take_input(player_name,e_val)
def board_print(board_layout):
    for i in board_layout:
        print(i,end="\n")


def pos_board(inp,p_val):
    if inp == 1:
        board[0][0]=p_val
    elif inp ==2:
        board[0][1]=p_val
    elif inp ==3:
        board[0][2]=p_val
    elif inp ==4:
        board[1][0]=p_val
    elif inp ==5:
        board[1][1]=p_val
    elif inp ==6:
        board[1][2]=p_val
    elif inp ==7:
        board[2][0]=p_val
    elif inp ==8:
        board[2][1]=p_val
    elif inp ==9:
        board[2][2]=p_val
    return board

def check_victory(board,count):
    v=""
    daig2=[board[0][2],board[1][1],board[2][0]]
    # Checking Vertical Victory
    for i in range(3):
        vert=[]
        daig1=[]
        for j in range(3):
            vert.append(board[j][i])
            daig1.append(board[j][j])
            if board[j].count(1)==3: 
                v='p1'
            elif board[j].count(2)==3:
                v='p2'
            elif vert.count(1)==3:
                v='p1'
            elif vert.count(2)==3: 
                v='p2'
            elif daig1.count(1)==3:
                v='p1'
            elif daig1.count(1)==3:
                v='p2'
            elif daig2.count(1)==3:
                v='p1'
            elif daig2.count(2)==3:
                v='p2'
            elif v=="" and count == 9:
                v='Draw'
    return v 
count = 0 
board=[[0,0,0],
       [0,0,0],
       [0,0,0]]

while count < 10:
    e_val=[]
    p1 = take_input('p1',e_val)
    e_val.append(p1)
    board=pos_board(p1,1)
    board_print(board)
    p2 = take_input('p2',e_val)
    e_val.append(p2)
    board=pos_board(p2,2)
    board_print(board)
    count+=1
    result=check_victory(board,count)
    if result == "":
        continue
    if result == 'p1' or 'p2':
        print('The winner is {}'.format(result))
        break
    elif result == 'Draw':
        print('Its a draw')
        break

      

      



