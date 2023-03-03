import os
from board import TTTBoard 

def clear_screen():
  
  if os.name == 'nt':
      # for windows
      os.system('cls')
  else:
      # for mac and linux(here, os.name is 'posix')
      os.system('clear')

if __name__ == '__main__':
  game_board = TTTBoard(3)

  current_turn = 0
  while True:
    clear_screen()
    game_board.print()
    position = input("pos? ")
    y = position[0]
    x = position[1]
    y = int(y)
    x = int(x)
    if current_turn % 2 == 0:
      token = 'X'
    else:
      token = 'O'
    
    if game_board.place(y, x, token):
      # add somethien to check if who win
      is_end = game_board.check()
      if is_end == True:
        clear_screen()
        game_board.print()
        print(f'{token} wins')
        break
      
      current_turn += 1
