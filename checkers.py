# final project - checkers v4
# bijan - erik - john - levi

# KNOWN ISSUES/BUGS:
# crashes sometimes while playing and moving pieces, usually at 'while not' loop in valid movement testing

#v4.1 changelog - bijan:
#fixed issue in isMoveValid not checking for capturing enemy pieces properly

# v4 changelog - erik:
# added last add_to_move_list() function to keep track of valid moves
# added move_list to display last 10 moves
# will add colors corresponding to which player's piece was moved

# v3 changelog - levi:
# vastly simplified the process() function to have more optimal/readable design
# added "else: return false" to isMoveValid() function because it was returning false positives
# added Bijan's functions and incorporated them into my process() function
# program can now distinguish between valid and invalid movements
# *however*, I have not incorporated all of Bijan's functions to determine one piece jumping over another

# v2 changelog - levi:
# created show_message() function for message display
# created process() function that processes user input to move game pieces
# currently, game pieces can move anywhere they want
# need: is_move_valid() function

# v1 changelog - erik:
# created draw_board function which takes a 2D list and draws the board
# checkers() currently being used just to test speed and design
# added coordinate letters and numbers to side
# added piece counts - can seperate regular and king pieces if desired
# ============================================PROGRAM BELOW===============================================

# Global scope - trying to limit this
# references to move_list in beginning process() function and 'Long rect right - middle' in draw_board()
move_list = []

def checkers():
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
  
  show_message('Welcome')
  gameover = False
  while not gameover:  
    board_list[:] = process(requestString("Player 1, make your move."), board_list, false, 0)
    repaint(draw_board(board_list, checkerboard))
    board_list[:] = process(requestString("Player 2, make your move."), board_list, false, 1)
    repaint(draw_board(board_list, checkerboard))


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
  addRectFilled(img_board, 474, 16, 158, 70, light_grid_color)
  addRect(img_board, 474, 16, 158, 70, black)
  addTextWithStyle(img_board, 480, 35,"Player 2: " + str(num_white) + " pieces", text_style1, black)
  
  # Long rect right - middle
  addRectFilled(img_board, 474, 97, 158, 276, light_grid_color)
  addRect(img_board, 474, 97, 158, 276, black)
  addTextWithStyle(img_board, 510, 112,"Last 10 Moves", text_style1, black)
  addLine(img_board, 474, 115, 632, 115, black)
  for move in range(len(move_list)): # using global var 'move_list'
    addTextWithStyle(img_board, 525, 138+(18*move),str(move_list[move]), text_style1, black) # using global var 'move_list'
  
  #small rect right - bottom
  addRectFilled(img_board, 474, 384, 158, 70, light_grid_color)
  addRect(img_board, 474, 384, 158, 70, black)
  addTextWithStyle(img_board, 480, 405,"Player 1: " + str(num_black) + " pieces", text_style1, black)
  
  return img_board

def show_message(prompt):
  prompt = prompt.lower()
  if prompt == 'welcome':
    showInformation("Welcome to Checkers!\nIn this game, you and an opponent will take turns moving your pieces diagonally through text commands (e.g. 'C3 to D4').\nYour pieces can only move forward in a diagonal direction. However, pieces will be granted backwards movement capabilities if they reach the opposite end of the board.\nThe objective is to capture all of your enemy's pieces by jumping over them.\nRemember that you can string together multiple jumps!\nGood luck!")
  if prompt == 'invalid move':
    showInformation("You cannot move that piece here.")
  if prompt == 'error':
    showInformation("Error. Unable to process that command.")

#Checks if a two spaces are diagonal and 'dist' spaces away
def isAdjacent(startRow, startCol, destRow, destCol, dist):
  return abs(destRow - startRow) == dist and abs(destCol - startCol) == dist

#Checks if the space is occupied by the opposing player's piece  
def isSpaceAnOpponentsPiece(row, col, player, board):
  if player == 0:
    return board[row][col] == 'w' or board[row][col] == 'wk'
  
  if player == 1:
    return board[row][col] == 'b' or board[row][col] == 'bk'
    
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

def isMoveValid(startRow, startCol, destRow, destCol, isKing, board, player):
  #check if the board space has a piece and the destination is empty
  if board[startRow][startCol] == ' ' or board[destRow][destCol] != ' ':
    return false
  #check that the move is forward
  #player == 0 for black
  if player == 0 and destRow > startRow and isKing == false:
    return false
  #player == 1 for white
  if player == 1 and destRow < startRow and isKing == false:
    return false
  
  #check that the spaces are adjacent Diagonals
  if isAdjacent(startRow, startCol, destRow, destCol, 1) != true:
    #if not an adjacent, check if they are two diagonals away and space between is a piece for a capture
    if isAdjacent(startRow, startCol, destRow, destCol, 2) != true and isPreviousDiagonalAPieceForCapture(startRow, startCol, destRow, destCol, player, board):
      return false
    else:
      return true
  
  return true

# Process player movement commands (e.g. 'C3 to D4')
# Adjusts board for proper movement display
def process(command, text_board, isKing, player):
  # Define grid dictionary for letter + num = x,y coordinates 
  # to ease the calculation of user-input
  map_grid = {}
  letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
  num = ['1', '2', '3', '4', '5', '6', '7', '8']
  total_loc = 70
  for i in letter:
    loc = total_loc
    for j in num:
      coord = i + j
      map_grid[coord] = str(loc)
      loc -= 10
    total_loc += 1
     
  # Analyze user input
  piece = 'none'
  command_copy = command.lower()
  command = command.lower().split()
  # Test if valid input
  if len(command) == 3 and len(command[0]) == 2 and len(command[2]) == 2:
    if command[1] == "to" and command[0][:1] <= 'h' and int(command[0][1:]) <= 8 and command[2][:1] <= 'h' and int(command[2][1:]) <= 8:
      # Test if valid movement
      if command[0] in map_grid and command[2] in map_grid:
        while not isMoveValid(int(map_grid[command[0]][:1]), int(map_grid[command[0]][1:]), int(map_grid[command[2]][:1]), int(map_grid[command[2]][1:]), isKing, text_board, player):
          show_message('INVALID MOVE')
          return process(requestString("Player %d, make your move." % (player + 1)), text_board, false, player)
      # Remove player piece
      if command[0] in map_grid:
        x = int(map_grid[command[0]][:1])
        y = int(map_grid[command[0]][1:])
        piece = text_board[x][y]
        text_board[x][y] = ' '
        add_to_move_list(command_copy) # Add move to gloval variable 'move_list'
      # Place player piece
      if command[2] in map_grid:
        x = int(map_grid[command[2]][:1])
        y = int(map_grid[command[2]][1:])
        text_board[x][y] = piece
        
      else:
        show_message('ERROR')
    else:
      show_message('ERROR')
  else:
    show_message('ERROR')
  return text_board
 
# Function to add valid commands to 'move_list'
def add_to_move_list(command):
  command = command.lower()
  move_list.insert(0,command) # using global var 'move_list'
  if len(move_list) == 11:
    move_list.pop()