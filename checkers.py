# CST205 Final Project - Checkers v5.0
# Bijan - Erik - John - Levi

# A checkers game with graphical board and audio

# Global scope 
# references to move_list in beginning process() function and 'Long rect right - middle' in draw_board()
move_list = []

def main():
  light_grid_color = makeColor(215, 215, 215)
  checkerboard = makeEmptyPicture(640,480)
  # This is the board with pieces in default position
  # w - white, wk - white king, b - black, bk - black king
  board_list = [[' ','w',' ','w',' ','w',' ','w'],
                ['w',' ','w',' ','w',' ','w',' '],
                [' ','w',' ','w',' ','w',' ','w'],
                [' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' '],
                ['b',' ','b',' ','b',' ','b',' '],
                [' ','b',' ','b',' ','b',' ','b'],
                ['b',' ','b',' ','b',' ','b',' ']]
  repaint(draw_board(board_list, checkerboard))
  # Initiate game loop
  show_message('WELCOME')
  gameover = false
  
  while not gameover:  
    # Player 1
    board_list[:] = process(requestString("Player 1, make your move."), board_list, 0)
    # Check for king
    for j in range(8):
      if board_list[0][j] == 'b':
        board_list[0][j] = 'bk'
    repaint(draw_board(board_list, checkerboard))
    # Check for Player 1 Win
    num_white = 0
    for i in range(8):
      for j in range(8):
        if 'w' in board_list[i][j] or 'wk' in board_list[i][j]:
          num_white += 1
    if num_white == 0:
      repaint(draw_board(board_list, checkerboard))
      show_message('P1WINS')
      return false
    # Player 2
    board_list[:] = process(requestString("Player 2, make your move."), board_list, 1)
    # Check for king
    for j in range(8):
      if board_list[7][j] == 'w':
        board_list[7][j] = 'wk'
    repaint(draw_board(board_list, checkerboard))
    # Check for Player 2 Win
    num_black = 0
    for i in range(8):
      for j in range(8):
        if 'b' in board_list[i][j] or 'bk' in board_list[i][j]:
          num_black += 1
    if num_black == 0:
      repaint(draw_board(board_list, checkerboard))
      show_message('P2WINS')
      return false

# Function to draw the board. Takes parameters of list board and initial blank image
# Future plans: Add parameters to display Turn #, active player, etc.
def draw_board(text_board, img_board):
  # Counters
  num_black = 0
  num_white = 0

  # Text styles
  king_style = makeStyle(serif, italic + bold, 18)
  text_style1 = makeStyle(serif, bold, 14)
  
  # Colors
  dark_grid_color = makeColor(171, 162, 191)
  light_grid_color = makeColor(215, 215, 215)
  dark_piece_color = makeColor(77, 59, 114)
 
  # Draws text coordinates and the dark squares to make the grid
  addRectFilled(img_board, 25, 16, 439, 439, light_grid_color)  
  for x in range(8):
    
    # Vertical coordinate letters
    addTextWithStyle(img_board, 50+(x*55),472,str(chr(ord('a')+x)),text_style1, black)
    # Horizontal coordinate numbers
    addTextWithStyle(img_board, 8,50+(x*55),str(8-x),text_style1, black)
    for y in range(8):
      if x % 2 == 1 and y % 2 == 0:
        addRectFilled(img_board, 25+(x*55), 16+(y*55) , 54, 54, dark_grid_color)
      elif x % 2 == 0 and y % 2 == 1:
        addRectFilled(img_board, 25+(x*55), 16+(y*55) , 54, 54, dark_grid_color)
  
  addRect(img_board, 25, 16, 439, 439, black)
  
  # Draw and keep count of pieces
  for x in range(8):
    for y in range(8):
      # Regular white piece
      if text_board[y][x] == 'w':  
        addOvalFilled(img_board, 32+(x*55), 24+(y*55), 44, 43, gray)
        addOvalFilled(img_board, 30+(x*55), 21+(y*55), 43, 43, white)
        addOval(img_board, 30+(x*55), 21+(y*55), 43, 43, black)
        addOval(img_board, 33+(x*55), 24+(y*55), 37, 37, black)
        num_white += 1
      # Kinged white piece
      elif text_board[y][x] == 'wk': 
        addOvalFilled(img_board, 32+(x*55), 24+(y*55), 44, 43, gray)
        addOvalFilled(img_board, 28+(x*55), 19+(y*55), 47, 47, yellow)
        addOvalFilled(img_board, 30+(x*55), 21+(y*55), 43, 43, white)
        addOval(img_board, 31+(x*55), 22+(y*55), 41, 41, black)
        addOval(img_board, 28+(x*55), 19+(y*55), 47, 47, black)
        addTextWithStyle(img_board, 45+(x*55), 49+(y*55), "K", king_style, black)
        num_white += 1
      # Regular dark piece
      elif text_board[y][x] == 'b': 
        addOvalFilled(img_board, 32+(x*55), 24+(y*55), 44, 43, gray)
        addOvalFilled(img_board, 30+(x*55), 21+(y*55), 43, 43, dark_piece_color)
        addOval(img_board, 30+(x*55), 21+(y*55), 43, 43, white)
        addOval(img_board, 33+(x*55), 24+(y*55), 37, 37, white)
        num_black += 1
      # Kinged dark piece
      elif text_board[y][x] == 'bk': 
        addOvalFilled(img_board, 32+(x*55), 24+(y*55), 44, 43, gray)
        addOvalFilled(img_board, 28+(x*55), 19+(y*55), 47, 47, yellow)
        addOvalFilled(img_board, 31+(x*55), 22+(y*55), 41, 41, dark_piece_color)
        addOval(img_board, 28+(x*55), 19+(y*55), 47, 47, black)
        addTextWithStyle(img_board, 45+(x*55), 49+(y*55), "K", king_style, white)
        num_black += 1
        
  # Small rect right - top
  addRectFilled(img_board, 474, 16, 158, 70, dark_grid_color)
  addRect(img_board, 474, 16, 158, 70, black)
  addTextWithStyle(img_board, 497, 36,"Player 2: " + str(num_white) + " pieces", text_style1, gray)
  addTextWithStyle(img_board, 496, 35,"Player 2: " + str(num_white) + " pieces", text_style1, white)
  
  # Long rect right - middle
  addRectFilled(img_board, 474, 97, 158, 276, dark_grid_color)
  addRect(img_board, 474, 97, 158, 276, black)
  addTextWithStyle(img_board, 511, 113,"Last 10 Moves", text_style1, gray)
  addTextWithStyle(img_board, 510, 112,"Last 10 Moves", text_style1, black)
  addLine(img_board, 474, 115, 632, 115, black)
  for move in range(len(move_list)): # using global var 'move_list'
    move_str = str(move_list[move])
    if move_str[:2] == "P1":
      addTextWithStyle(img_board, 518, 139+(18*move),str(move_list[move]), text_style1, gray) # using global var 'move_list'
      addTextWithStyle(img_board, 517, 138+(18*move),str(move_list[move]), text_style1, black) # using global var 'move_list'
    elif move_str[:2] == "P2":
      addTextWithStyle(img_board, 518, 139+(18*move),str(move_list[move]), text_style1, gray) # using global var 'move_list'
      addTextWithStyle(img_board, 517, 138+(18*move),str(move_list[move]), text_style1, white) # using global var 'move_list'

  
  # Small rect right - bottom
  addRectFilled(img_board, 474, 384, 158, 70, dark_grid_color)
  addRect(img_board, 474, 384, 158, 70, black)
  addTextWithStyle(img_board, 497, 406,"Player 1: " + str(num_black) + " pieces", text_style1, gray)
  addTextWithStyle(img_board, 496, 405,"Player 1: " + str(num_black) + " pieces", text_style1, black)
  
  return img_board


def show_message(prompt):
  prompt = prompt.lower()
  if prompt == 'welcome':
    showInformation("Welcome to Checkers!\nIn this game, you and an opponent will take turns moving your pieces diagonally through text commands (e.g. 'C3 to D4').\nYour pieces can only move forward in a diagonal direction. However, pieces will be granted backwards movement capabilities if they reach the opposite end of the board and become a King.\nThe objective is to capture all of your enemy's pieces by jumping over them.\nGood luck!")
  if prompt == 'invalid move':
    showInformation("Not a valid movement.")
  if prompt == 'error':
    showInformation("Error. Unable to process that command.")
  if prompt == 'p1wins':
    showInformation("Congratulations, Player 1. You win!")
  if prompt == 'p2wins':
    showInformation("Congratulations, Player 2. You win!")

#Checks if two spaces are diagonal and 'dist' spaces away
def isAdjacent(startRow, startCol, destRow, destCol, dist):
  if abs(destRow - startRow) == dist and abs(destCol - startCol) == dist:
    return true   
  return false

#Checks if the space is occupied by the opposing player's piece  
def isSpaceAnOpponentsPiece(row, col, player, board):
  if player == 0:
    if board[row][col] == 'w' or board[row][col] == 'wk':
      board[row][col] = ' '
      return true
  if player == 1:
    if board[row][col] == 'b' or board[row][col] == 'bk':
      board[row][col] = ' '
      return true
  return false

#Checks if a space before has a piece to capture
def isPreviousDiagonalAPieceForCapture(startRow, startCol, destRow, destCol, player, board):
  if (destRow - startRow) % 2 != 0 or (destCol - startCol) % 2 != 0:
    return false
    
  rowDist = (destRow - startRow) / 2
  colDist = (destCol - startCol) / 2
  middleRow = startRow + rowDist
  middleCol = startCol + colDist
  return isSpaceAnOpponentsPiece(middleRow, middleCol, player, board)


def isMoveValid(startRow, startCol, destRow, destCol, board, player):
  #check if the board space has a piece and the destination is empty
  if board[startRow][startCol] == ' ' or board[destRow][destCol] != ' ':
    return false
  #check if the starting piece belongs to player
  if player == 0:
    if board[startRow][startCol] == 'w' or board[startRow][startCol] == 'wk':
      return false
  if player == 1:
    if board[startRow][startCol] == 'b' or board[startRow][startCol] == 'bk':
      return false
  #check that the move is forward unless the piece is a King
  if board[startRow][startCol][-1:] != 'k':
    #player == 0 for black
    if player == 0 and destRow > startRow:
      return false
    #player == 1 for white
    if player == 1 and destRow < startRow:
      return false
  #check that the spaces are adjacent Diagonals
  if isAdjacent(startRow, startCol, destRow, destCol, 1) == false:
    #if not an adjacent, check if they are two diagonals away and space between is a piece for a capture
    if isAdjacent(startRow, startCol, destRow, destCol, 2) and isPreviousDiagonalAPieceForCapture(startRow, startCol, destRow, destCol, player, board):
      return true
    else:
      return false
  else:
    return true
    
# Define grid dictionary for letter + num = x,y coordinates to ease the calculation of user-input in process()
def grid():
  map_grid = {}
  letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
  num = ['1', '2', '3', '4', '5', '6', '7', '8']
  total_loc = 70
  for i in letter:
    loc = total_loc
    for j in num:
      coord = i + j
      map_grid[coord] = str(loc)
      # Make single digits have leading zeros
      # Helps smooth string-slicing interaction later on
      if len(map_grid[coord]) == 1:
        map_grid[coord] = map_grid[coord].zfill(2)
      loc -= 10
    total_loc += 1
  return map_grid
  
# Process player movement commands (e.g. 'C3 to D4')
# Adjusts board for proper movement display
def process(command, text_board, player):
  map_grid = grid()
  # Temp var for moving pieces
  piece = 'none'
  command_copy = command.lower()
  command = command.lower().split()
  # Test if valid input (must be in format "a1 to b2")
  if len(command) == 3 and len(command[0]) == 2 and len(command[2]) == 2 and command[0][:1].isalpha() and command[0][1:].isdigit() and command[2][:1].isalpha() and command[2][1:].isdigit():
    if command[1] == "to" and command[0][:1] <= 'h' and int(command[0][1:]) <= 8 and command[2][:1] <= 'h' and int(command[2][1:]) <= 8:
      # Test if valid movement for pieces 
      if command[0] in map_grid and command[2] in map_grid:
        while not isMoveValid(int(map_grid[command[0]][:1]), int(map_grid[command[0]][1:]), int(map_grid[command[2]][:1]), int(map_grid[command[2]][1:]), text_board, player):
          show_message('INVALID MOVE')
          return process(requestString("Player %d, make your move." % (player + 1)), text_board, player)
      # Remove player piece
      if command[0] in map_grid:
        x = int(map_grid[command[0]][:1])
        y = int(map_grid[command[0]][1:])
        piece = text_board[x][y]
        text_board[x][y] = ' '
        # Add move to global variable 'move_list'
        add_to_move_list(command_copy, player) 
      # Place player piece
      if command[2] in map_grid:
        x = int(map_grid[command[2]][:1])
        y = int(map_grid[command[2]][1:])
        text_board[x][y] = piece  
      else:
        show_message('ERROR')
        return process(requestString("Player %d, make your move." % (player + 1)), text_board, player)
    else:
      show_message('ERROR')
      return process(requestString("Player %d, make your move." % (player + 1)), text_board, player)
  else:
    show_message('ERROR')
    return process(requestString("Player %d, make your move." % (player + 1)), text_board, player)
  # Play audio of user's command  
  speech(command)
  
  return text_board
 
# Function to add valid commands to 'move_list'
def add_to_move_list(command,player):
  command = command.lower()
  if player == 0:
    move_list.insert(0,"P1: " + str(command)) # using global var 'move_list'
  elif player == 1:
    move_list.insert(0,"P2: " + str(command)) # using global var 'move_list'
  if len(move_list) == 11:
    move_list.pop()

# Function to play text-to-speech audio for player commands
def speech(command):
  # Folder must contain wav files for 'a', 'b', 'c', 'd', 'e', 'f', 'g', '1', '2', '3', '4', '5', '6', '7', '8', and 'to'
  folder = os.path.dirname(os.path.realpath(__file__)) + "\\sounds\\"
  start1 = command[0][:1]
  start2 = command[0][1:]
  to = command[1]
  dest1 = command[2][:1]
  dest2 = command[2][1:]
  wav = ".wav"

  speech1 = makeSound(folder + start1 + wav)
  speech2 = makeSound(folder + start2 + wav)
  speech3 = makeSound(folder + to + wav)
  speech4 = makeSound(folder + dest1 + wav)
  speech5 = makeSound(folder + dest2 + wav)
  
  play(collage(speech1, speech2, speech3, speech4, speech5))
  
# Combine audio files into one for playback
def collage(s1, s2, s3, s4, s5):
  totalLength = getLength(s1) + getLength(s2) + getLength(s3) + getLength(s4) + getLength(s5)
  final = makeEmptySound(totalLength, int(getSamplingRate(s1)))
  i = 0
  for n in range(0, getLength(s1)):
    value = getSampleValueAt(s1, n)
    setSampleValueAt(final, i, value)
    i += 1
  for n in range(0, getLength(s2)):
    value = getSampleValueAt(s2, n)
    setSampleValueAt(final, i, value)
    i += 1
  for n in range(0, getLength(s3)):
    value = getSampleValueAt(s3, n)
    setSampleValueAt(final, i, value)
    i += 1
  for n in range(0, getLength(s4)):
    value = getSampleValueAt(s4, n)
    setSampleValueAt(final, i, value)
    i += 1
  for n in range(0, getLength(s5)):
    value = getSampleValueAt(s5, n)
    setSampleValueAt(final, i, value)
    i += 1
  return final
  
