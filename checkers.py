# final project - checkers v1
# bijan - erik - john - levi

# v1 changelog - erik:
# created draw_board function which takes a 2D list and draws the board
# checkers() currently being used just to test speed and design
# added coordinate letters and numbers to side
# added piece counts - can seperate regular and king pieces if desired

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
