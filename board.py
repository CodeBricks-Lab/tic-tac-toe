class Board():
  def __init__(self, size):
    self.board = []
    self.size = size
    self.empty = '*'
    
    for j in range(self.size):
      row = []
      for i in range(self.size):
        row.append(self.empty)
      self.board.append(row)

  def print(self):
    for i in range(len(self.board)):
      row = self.board[i]
      r = ''
      for j in range(len(row)):
        r = f'{r} {row[j]}'
        
      print(r)

  def place(self, y, x, token):
    if self.board[y][x] == self.empty:
      self.board[y][x] = token
      return True
    return False

  def check(self):
    pass

class TTTBoard(Board):
  def check(self):
    if self.check_row() or self.check_column() or self.check_diagonal():
      return True
    return False
  
  def check_row(self):
    for i in range(self.size):
      item_set = set(self.board[i])
      if len(item_set) == 1 and item_set.pop() != self.empty:
        return True
    return False

  def check_column(self):
    for i in range(self.size):
      items = []
      for j in range(self.size):
        items.append(self.board[j][i])
      
      item_set = set(items)
      if len(item_set) == 1 and item_set.pop() != self.empty:
        return True
    return False

  def check_diagonal(self):
    items = []
    for i in range(self.size):
      items.append(self.board[i][i])
    
    item_set = set(items)
    if len(item_set) == 1 and item_set.pop() != self.empty:
      return True
    
    items = []
    for i in range(self.size):
      items.append(self.board[i][self.size - i - 1])

    item_set = set(items)
    if len(item_set) == 1 and item_set.pop() != self.empty:
      return True
    
    return False


if __name__ == '__main__':  
    second_board = TTTBoard(5)
    second_board.print()

    my_board = Board(3)
    my_board.print()
