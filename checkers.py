# final project - checkers v2
# bijan - erik - john - levi

# v2 changelog - levi:
# created show_message() function for message display
# created process() function that processes user input to move game pieces
# currently, game pieces can move anywhere they want
# need: is_move_valid() function


def checkers():
  light_grid_color = makeColor(215, 215, 215)
  checkerboard = makeEmptyPicture(640,480)
  #this is the board with pieces in default position
  #w - white, wk - white king, b - black, bk - black king
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
    board_list[:] = process(requestString("Player 1, make your move."), board_list)
    repaint(draw_board(board_list, checkerboard))
    board_list[:] = process(requestString("Player 2, make your move."), board_list)
    repaint(draw_board(board_list, checkerboard))
  
  showInformation("this pause is to see speed of draw_board function")
  
  board_list = [[' ','w',' ','w',' ',' ',' ','w'],
                ['w',' ','bk',' ','w',' ','w',' '],
                [' ','w',' ',' ',' ',' ',' ','w'],
                [' ',' ','wk',' ',' ',' ',' ',' '],
                [' ','b',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ','b',' ','b',' '],
                [' ','b',' ','b',' ','wk',' ','b'],
                [' ',' ',' ',' ','b',' ','b',' ']]
  
  repaint(draw_board(board_list, checkerboard))


# Function to draw the board. Takes parameters of list board and initial blank image
# Future plans: Add parameters to display Turn #, active player, etc.
def draw_board(text_board, img_board):
  #counters
  num_black = 0
  num_white = 0

  #text styles
  king_style = makeStyle(serif, italic + bold, 18)
  text_style1 = makeStyle(serif, bold, 14)
  
  #colors
  dark_grid_color = makeColor(171, 162, 191)
  light_grid_color = makeColor(215, 215, 215)
  dark_piece_color = makeColor(77, 59, 114)
 
  #draws text coordinates and the dark squares to make the grid
  addRectFilled(img_board, 25, 16, 439, 439, light_grid_color)  
  for x in range(8):
    
    #vertical coordinate letters
    addTextWithStyle(img_board, 50+(x*55),472,str(chr(ord('a')+x)),text_style1, black)
    #horizontal coordinate numbers
    addTextWithStyle(img_board, 8,50+(x*55),str(8-x),text_style1, black)
    for y in range(8):
      if x % 2 == 1 and y % 2 == 0:
        addRectFilled(img_board, 25+(x*55), 16+(y*55) , 54, 54, dark_grid_color)
      elif x % 2 == 0 and y % 2 == 1:
        addRectFilled(img_board, 25+(x*55), 16+(y*55) , 54, 54, dark_grid_color)
  
  addRect(img_board, 25, 16, 439, 439, black)
  
  #draw and keep count of pieces
  for x in range(8):
    for y in range(8):
      #regular white piece
      if text_board[y][x] == 'w':  
        addOvalFilled(img_board, 32+(x*55), 24+(y*55), 44, 43, gray)
        addOvalFilled(img_board, 30+(x*55), 21+(y*55), 43, 43, white)
        addOval(img_board, 30+(x*55), 21+(y*55), 43, 43, black)
        addOval(img_board, 33+(x*55), 24+(y*55), 37, 37, black)
        num_white += 1
      #kinged white piece
      elif text_board[y][x] == 'wk': 
        addOvalFilled(img_board, 32+(x*55), 24+(y*55), 44, 43, gray)
        addOvalFilled(img_board, 28+(x*55), 19+(y*55), 47, 47, yellow)
        addOvalFilled(img_board, 30+(x*55), 21+(y*55), 43, 43, white)
        addOval(img_board, 31+(x*55), 22+(y*55), 41, 41, black)
        addOval(img_board, 28+(x*55), 19+(y*55), 47, 47, black)
        addTextWithStyle(img_board, 45+(x*55), 49+(y*55), "K", king_style, black)
        num_white += 1
      #regular dark piece
      elif text_board[y][x] == 'b': 
        addOvalFilled(img_board, 32+(x*55), 24+(y*55), 44, 43, gray)
        addOvalFilled(img_board, 30+(x*55), 21+(y*55), 43, 43, dark_piece_color)
        addOval(img_board, 30+(x*55), 21+(y*55), 43, 43, white)
        addOval(img_board, 33+(x*55), 24+(y*55), 37, 37, white)
        num_black += 1
      #kinged dark piece
      elif text_board[y][x] == 'bk': 
        addOvalFilled(img_board, 32+(x*55), 24+(y*55), 44, 43, gray)
        addOvalFilled(img_board, 28+(x*55), 19+(y*55), 47, 47, yellow)
        addOvalFilled(img_board, 31+(x*55), 22+(y*55), 41, 41, dark_piece_color)
        addOval(img_board, 28+(x*55), 19+(y*55), 47, 47, black)
        addTextWithStyle(img_board, 45+(x*55), 49+(y*55), "K", king_style, white)
        num_black += 1
        
  #small rect right - top
  addRectFilled(img_board, 474, 16, 158, 70, light_grid_color)
  addRect(img_board, 474, 16, 158, 70, black)
  addTextWithStyle(img_board, 480, 35,"Player 2: " + str(num_white) + " pieces", text_style1, black)
  
  #long rect right - middle
  addRectFilled(img_board, 474, 97, 158, 276, light_grid_color)
  addRect(img_board, 474, 97, 158, 276, black)
  
  #small rect right - bottom
  addRectFilled(img_board, 474, 384, 158, 70, light_grid_color)
  addRect(img_board, 474, 384, 158, 70, black)
  addTextWithStyle(img_board, 480, 405,"Player 1: " + str(num_black) + " pieces", text_style1, black)
  
  return img_board

def show_message(prompt):
  prompt = prompt.lower()
  if prompt == 'welcome':
    showInformation("Welcome to Checkers!\nIn this game, you and an opponent will take turns moving your pieces diagonally through text commands (e.g. 'C3 to D4').\nYour pieces can only move forward in a diagonal direction. However, pieces will be granted backwards movement capabilities if they reach the opposite end of the board.\nThe objective is to capture all of your enemy's pieces by jumping over them.\nRemember that you can string together multiple jumps!\nGood luck!")
  if prompt == 'error':
    showInformation("Error. Unable to process that command.")

# Process player movement commands (e.g. 'C3 to D4')
# Adjusts board for proper movement display
def process(command, text_board):
  piece = 'none'
  command = command.lower().split()
  if len(command) == 3 and len(command[0]) == 2 and len(command[2]) == 2:
    if command[1] == "to" and command[0][:1].isalpha() and command[0][1:].isdigit() and command[2][:1].isalpha() and command[2][1:].isdigit():
      # Remove player piece
      if command[0][:1] == 'a':
        if command[0][1:] == '1':
          piece = text_board[7][0]
          text_board[7][0] = ' '
        if command[0][1:] == '2':
          piece = text_board[6][0]
          text_board[6][0] = ' '
        if command[0][1:] == '3':
          piece = text_board[5][0]
          text_board[5][0] = ' '
        if command[0][1:] == '4':
          piece = text_board[4][0]
          text_board[4][0] = ' '
        if command[0][1:] == '5':
          piece = text_board[3][0]
          text_board[3][0] = ' '
        if command[0][1:] == '6':
          piece = text_board[2][0]
          text_board[2][0] = ' '
        if command[0][1:] == '7':
          piece = text_board[1][0]
          text_board[1][0] = ' '
        if command[0][1:] == '8':
          piece = text_board[0][0]
          text_board[0][0] = ' '
      if command[0][:1] == 'b':
        if command[0][1:] == '1':
          piece = text_board[7][1]
          text_board[7][1] = ' '
        if command[0][1:] == '2':
          piece = text_board[6][1]
          text_board[6][1] = ' '
        if command[0][1:] == '3':
          piece = text_board[5][1]
          text_board[5][1] = ' '
        if command[0][1:] == '4':
          piece = text_board[4][1]
          text_board[4][1] = ' '
        if command[0][1:] == '5':
          piece = text_board[3][1]
          text_board[3][1] = ' '
        if command[0][1:] == '6':
          piece = text_board[2][1]
          text_board[2][1] = ' '
        if command[0][1:] == '7':
          piece = text_board[1][1]
          text_board[1][1] = ' '
        if command[0][1:] == '8':
          piece = text_board[0][1]
          text_board[0][1] = ' '
      if command[0][:1] == 'c':
        if command[0][1:] == '1':
          piece = text_board[7][2]
          text_board[7][2] = ' '
        if command[0][1:] == '2':
          piece = text_board[6][2]
          text_board[6][2] = ' '
        if command[0][1:] == '3':
          piece = text_board[5][2]
          text_board[5][2] = ' '
        if command[0][1:] == '4':
          piece = text_board[4][2]
          text_board[4][2] = ' '
        if command[0][1:] == '5':
          piece = text_board[3][2]
          text_board[3][2] = ' '
        if command[0][1:] == '6':
          piece = text_board[2][2]
          text_board[2][2] = ' '
        if command[0][1:] == '7':
          piece = text_board[1][2]
          text_board[1][2] = ' '
        if command[0][1:] == '8':
          piece = text_board[0][2]
          text_board[0][2] = ' '
      if command[0][:1] == 'd':
        if command[0][1:] == '1':
          piece = text_board[7][3]
          text_board[7][3] = ' '
        if command[0][1:] == '2':
          piece = text_board[6][3]
          text_board[6][3] = ' '
        if command[0][1:] == '3':
          piece = text_board[5][3]
          text_board[5][3] = ' '
        if command[0][1:] == '4':
          piece = text_board[4][3]
          text_board[4][3] = ' '
        if command[0][1:] == '5':
          piece = text_board[3][3]
          text_board[3][3] = ' '
        if command[0][1:] == '6':
          piece = text_board[2][3]
          text_board[2][3] = ' '
        if command[0][1:] == '7':
          piece = text_board[1][3]
          text_board[1][3] = ' '
        if command[0][1:] == '8':
          piece = text_board[0][3]
          text_board[0][3] = ' '
      if command[0][:1] == 'e':
        if command[0][1:] == '1':
          piece = text_board[7][4]
          text_board[7][4] = ' '
        if command[0][1:] == '2':
          piece = text_board[6][4]
          text_board[6][4] = ' '
        if command[0][1:] == '3':
          piece = text_board[5][4]
          text_board[5][4] = ' '
        if command[0][1:] == '4':
          piece = text_board[4][4]
          text_board[4][4] = ' '
        if command[0][1:] == '5':
          piece = text_board[3][4]
          text_board[3][4] = ' '
        if command[0][1:] == '6':
          piece = text_board[2][4]
          text_board[2][4] = ' '
        if command[0][1:] == '7':
          piece = text_board[1][4]
          text_board[1][4] = ' '
        if command[0][1:] == '8':
          piece = text_board[0][4]
          text_board[0][4] = ' '
      if command[0][:1] == 'f':
        if command[0][1:] == '1':
          piece = text_board[7][5]
          text_board[7][5] = ' '
        if command[0][1:] == '2':
          piece = text_board[6][5]
          text_board[6][5] = ' '
        if command[0][1:] == '3':
          piece = text_board[5][5]
          text_board[5][5] = ' '
        if command[0][1:] == '4':
          piece = text_board[4][5]
          text_board[4][5] = ' '
        if command[0][1:] == '5':
          piece = text_board[3][5]
          text_board[3][5] = ' '
        if command[0][1:] == '6':
          piece = text_board[2][5]
          text_board[2][5] = ' '
        if command[0][1:] == '7':
          piece = text_board[1][5]
          text_board[1][5] = ' '
        if command[0][1:] == '8':
          piece = text_board[0][5]
          text_board[0][5] = ' '
      if command[0][:1] == 'g':
        if command[0][1:] == '1':
          piece = text_board[7][6]
          text_board[7][6] = ' '
        if command[0][1:] == '2':
          piece = text_board[6][6]
          text_board[6][6] = ' '
        if command[0][1:] == '3':
          piece = text_board[5][6]
          text_board[5][6] = ' '
        if command[0][1:] == '4':
          piece = text_board[4][6]
          text_board[4][6] = ' '
        if command[0][1:] == '5':
          piece = text_board[3][6]
          text_board[3][6] = ' '
        if command[0][1:] == '6':
          piece = text_board[2][6]
          text_board[2][6] = ' '
        if command[0][1:] == '7':
          piece = text_board[1][6]
          text_board[1][6] = ' '
        if command[0][1:] == '8':
          piece = text_board[0][6]
          text_board[0][6] = ' '
      if command[0][:1] == 'h':
        if command[0][1:] == '1':
          piece = text_board[7][7]
          text_board[7][7] = ' '
        if command[0][1:] == '2':
          piece = text_board[6][7]
          text_board[6][7] = ' '
        if command[0][1:] == '3':
          piece = text_board[5][7]
          text_board[5][7] = ' '
        if command[0][1:] == '4':
          piece = text_board[4][7]
          text_board[4][7] = ' '
        if command[0][1:] == '5':
          piece = text_board[3][7]
          text_board[3][7] = ' '
        if command[0][1:] == '6':
          piece = text_board[2][7]
          text_board[2][7] = ' '
        if command[0][1:] == '7':
          piece = text_board[1][7]
          text_board[1][7] = ' '
        if command[0][1:] == '8':
          piece = text_board[0][7]
          text_board[0][7] = ' '
      
      # Place player piece
      if command[2][:1] == 'a':
        if command[2][1:] == '1':
          text_board[7][0] = piece
        if command[2][1:] == '2':
          text_board[6][0] = piece
        if command[2][1:] == '3':
          text_board[5][0] = piece
        if command[2][1:] == '4':
          text_board[4][0] = piece
        if command[2][1:] == '5':
          text_board[3][0] = piece
        if command[2][1:] == '6':
          text_board[2][0] = piece
        if command[2][1:] == '7':
          text_board[1][0] = piece
        if command[2][1:] == '8':
          text_board[0][0] = piece
      if command[2][:1] == 'b':
        if command[2][1:] == '1':
          text_board[7][1] = piece
        if command[2][1:] == '2':
          text_board[6][1] = piece
        if command[2][1:] == '3':
          text_board[5][1] = piece
        if command[2][1:] == '4':
          text_board[4][1] = piece
        if command[2][1:] == '5':
          text_board[3][1] = piece
        if command[2][1:] == '6':
          text_board[2][1] = piece
        if command[2][1:] == '7':
          text_board[1][1] = piece
        if command[2][1:] == '8':
          text_board[0][1] = piece
      if command[2][:1] == 'c':
        if command[2][1:] == '1':
          text_board[7][2] = piece
        if command[2][1:] == '2':
          text_board[6][2] = piece
        if command[2][1:] == '3':
          text_board[5][2] = piece
        if command[2][1:] == '4':
          text_board[4][2] = piece
        if command[2][1:] == '5':
          text_board[3][2] = piece
        if command[2][1:] == '6':
          text_board[2][2] = piece
        if command[2][1:] == '7':
          text_board[1][2] = piece
        if command[2][1:] == '8':
          text_board[0][2] = piece
      if command[2][:1] == 'd':
        if command[2][1:] == '1':
          text_board[7][3] = piece
        if command[2][1:] == '2':
          text_board[6][3] = piece
        if command[2][1:] == '3':
          text_board[5][3] = piece
        if command[2][1:] == '4':
          text_board[4][3] = piece
        if command[2][1:] == '5':
          text_board[3][3] = piece
        if command[2][1:] == '6':
          text_board[2][3] = piece
        if command[2][1:] == '7':
          text_board[1][3] = piece
        if command[2][1:] == '8':
          text_board[0][3] = piece
      if command[2][:1] == 'e':
        if command[2][1:] == '1':
          text_board[7][4] = piece
        if command[2][1:] == '2':
          text_board[6][4] = piece
        if command[2][1:] == '3':
          text_board[5][4] = piece
        if command[2][1:] == '4':
          text_board[4][4] = piece
        if command[2][1:] == '5':
          text_board[3][4] = piece
        if command[2][1:] == '6':
          text_board[2][4] = piece
        if command[2][1:] == '7':
          text_board[1][4] = piece
        if command[2][1:] == '8':
          text_board[0][4] = piece
      if command[2][:1] == 'f':
        if command[2][1:] == '1':
          text_board[7][5] = piece
        if command[2][1:] == '2':
          text_board[6][5] = piece
        if command[2][1:] == '3':
          text_board[5][5] = piece
        if command[2][1:] == '4':
          text_board[4][5] = piece
        if command[2][1:] == '5':
          text_board[3][5] = piece
        if command[2][1:] == '6':
          text_board[2][5] = piece
        if command[2][1:] == '7':
          text_board[1][5] = piece
        if command[2][1:] == '8':
          text_board[0][5] = piece
      if command[2][:1] == 'g':
        if command[2][1:] == '1':
          text_board[7][6] = piece
        if command[2][1:] == '2':
          text_board[6][6] = piece
        if command[2][1:] == '3':
          text_board[5][6] = piece
        if command[2][1:] == '4':
          text_board[4][6] = piece
        if command[2][1:] == '5':
          text_board[3][6] = piece
        if command[2][1:] == '6':
          text_board[2][6] = piece
        if command[2][1:] == '7':
          text_board[1][6] = piece
        if command[2][1:] == '8':
          text_board[0][6] = piece
      if command[2][:1] == 'h':
        if command[2][1:] == '1':
          text_board[7][7] = piece
        if command[2][1:] == '2':
          text_board[6][7] = piece
        if command[2][1:] == '3':
          text_board[5][7] = piece
        if command[2][1:] == '4':
          text_board[4][7] = piece
        if command[2][1:] == '5':
          text_board[3][7] = piece
        if command[2][1:] == '6':
          text_board[2][7] = piece
        if command[2][1:] == '7':
          text_board[1][7] = piece
        if command[2][1:] == '8':
          text_board[0][7] = piece
    else:
      show_message('ERROR')
  else:
    show_message('ERROR')
  return text_board
  