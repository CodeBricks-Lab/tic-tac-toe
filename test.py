import unittest
from board import TTTBoard

class TestTTT(unittest.TestCase):
  def test_check_row(self):
    board = TTTBoard(3)
    board.board = [
      ['o', 'x', 'x'],
      ['o', 'x', 'x'],
      ['o', 'x', 'x'],
      ]
    self.assertTrue(board.check_row())

  def test_check_column(self):
    pass
  def test_check_diagnol(self):
    pass

if __name__ == '__main__':
  unittest.main()
