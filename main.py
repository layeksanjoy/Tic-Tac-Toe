inf = 9999
print("Enter the the values as")
print("[' 1 ',' 2 ',' 3 ']\n[' 4 ',' 5 ',' 6 ']\n[' 7 ',' 8 ',' 9 ']\n")

board = [['   ','   ','   '],
        ['   ','   ','   '],
        ['   ','   ','   '],]


def draw():
  for i in range(0,3):
    print("------------------\n")
    for j in range(0,3):
      print(board[i][j], end = "|")
    print('\n')
  print("------------------\n")
  print("\n\n")

def checkWin():
# diagonals
  if(board[0][0] == ' O ' and board[1][1] == ' O ' and board[2][2] == ' O '):
    return 10
  if(board[0][0] == ' X ' and board[1][1] == ' X ' and board[2][2] == ' X '):
    return -1

  if(board[0][2] == ' O ' and board[1][1] == ' O ' and board[2][0] == ' O '):
    return 10
  if(board[0][2] == ' X ' and board[1][1] == ' X ' and board[2][0] == ' X '):
    return -1

# 1st col
  if(board[0][0] == ' O ' and board[1][0] == ' O ' and board[2][0] == ' O '):
    return 10
  if(board[0][0] == ' X ' and board[1][0] == ' X ' and board[2][0] == ' X '):
    return -1

# 2nd col
  if(board[0][1] == ' O ' and board[1][1] == ' O ' and board[2][1] == ' O '):
    return 10
  if(board[0][1] == ' X ' and board[1][1] == ' X ' and board[2][1] == ' X '):
    return -1

# 3rd  col
  if(board[0][2] == ' O ' and board[1][2] == ' O ' and board[2][2] == ' O '):
    return 10
  if(board[0][2] == ' X ' and board[1][2] == ' X ' and board[2][2] == ' X '):
    return -1

# 1st row
  if(board[0][0] == ' O ' and board[0][1] == ' O ' and board[0][2] == ' O '):
    return 10
  if(board[0][0] == ' X ' and board[0][1] == ' X ' and board[0][2] == ' X '):
    return -1

# 2nd row
  if(board[1][0] == ' O ' and board[1][1] == ' O ' and board[1][2] == ' O '):
    return 10
  if(board[1][0] == ' X ' and board[1][1] == ' X ' and board[1][2] == ' X '):
    return -1

# 3rd  row
  if(board[2][0] == ' O ' and board[2][1] == ' O ' and board[2][2] == ' O '):
    return 10
  if(board[2][0] == ' X ' and board[2][1] == ' X ' and board[2][2] == ' X '):
    return -1

  tie = True
  for i in range(0,3):
    for j in range(0,3):
      if(board[i][j] == '   '):
        tie = False
        break
  if(tie):
    return 0

  return 2


# 10 O won : -1 X Won :0 if Tie : 2 Match is not Complete 

def minimax(board,isMax):
  temp = checkWin()
  if(temp != 2):
    # draw()
    # print("End",temp)
    return temp

  if(not isMax):
      bestScore = inf

      for i in range(0,3):
        for j in range(0,3):
          if(board[i][j] == '   '):
            board[i][j] = ' X '
            # draw()
            score = minimax(board,True) 
            # print(score)
            board[i][j] = '   '
            if(score < bestScore):
              bestScore = score
      return bestScore

  else:
      bestScore = -inf
      for i in range(0,3):
        for j in range(0,3):
          if(board[i][j] == '   '):
            board[i][j] = ' O '
            # draw()
            score = minimax(board,False)
            # print(score)
            board[i][j] = '   '

            if(score > bestScore):
              bestScore = score
      return bestScore


def bestMove(board):
  bestScore = -inf
  move = []
  for i in range(0,3):
    for j in range(0,3):
      # is the spot available
      if(board[i][j] == '   '):
        board[i][j] = ' O '
        score = minimax(board ,False)
        board[i][j] = '   '
        if(score > bestScore):
          bestScore = score
          move = [i,j]
  
  board[move[0]][move[1]] = ' O '


# draw()
# bestMove(board)
# value = minimax(board,True)
# print("Value",value)
# draw()



i = 0
while (i < 9):
  j = 0
  if( i == 0):
    j = 1
  elif(i == 1):
    j = 2
  else:
    div = i%2
    if(div == 0):
      j = 1
    else:
      j = 2


  print("Input Player 1")    
  val = int(input())


  posi = 0
  posj = 0

  t_posj = val%3
  # print(t_posj)
  if(t_posj == 0):
    posj = 2
  else:
    posj = t_posj - 1
  # print(posj)
  
  t_posi = val//3
  posi = t_posi
  # print(t_posi)
  if(t_posi > 0):
    if(t_posj == 0):
      posi = t_posi - 1
  
  # print(posi)
  

  if( j == 1):
    # print(j,posi,posj)
    if(board[posi][posj] == '   '): 
      board[posi][posj] = ' X '
      i += 1
      result = checkWin();
      if(result == -1):
        draw()
        print("Player 1 Won")
        break
    else:
      print("Area is already Filled")
      print("Please Enter Again ")
      continue



  result = checkWin()
  if(result == 0):
    draw()
    print("It was a draw..")
    break


  bestMove(board)
  i+= 1

  draw()
  if(result == 10):
    draw()
    print("The AI Won")
    break
