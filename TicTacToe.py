#by neksha
import tkinter as tk

class TicTacToe(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Tic-Tac-Toe')
    self.board = [[' ' for _ in range(3)] for _ in range(3)]
    self.buttons = [[tk.Button(self, text=' ', width=10, height=5, font=('Helvetica', 24), command=lambda row=i, col=j: self.move(row, col)) for j in range(3)] for i in range(3)]
    for i in range(3):
      for j in range(3):
        self.buttons[i][j].grid(row=i, column=j)
    self.player = 'X'
    self.mainloop()

  def move(self, row, col):
    if self.board[row][col] != ' ':
      return
    self.board[row][col] = self.player
    if self.player == 'X':
      self.buttons[row][col]['fg'] = 'red'
    else:
      self.buttons[row][col]['fg'] = 'blue'
    self.buttons[row][col]['text'] = self.player
    self.player = 'O' if self.player == 'X' else 'X'
    result = self.game_over()
    if result is not None:
      self.game_over_message(result)

  def game_over(self):
    # Check for a winning row
    for row in self.board:
      if row[0] == row[1] == row[2] and row[0] != ' ':
        return row[0]

    # Check for a winning column
    for col in range(3):
      if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
        return self.board[0][col]

    # Check for a winning diagonal
   
    if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
      return self.board[0][0]
    if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
      return self.board[0][2]

    # Check for a draw
    for row in self.board:
      if ' ' in row:
        return None

    return 'D'

  def game_over_message(self, result):
    if result == 'D':
      message = "It's a draw!"
    else:
      message = f'{result} wins!'
    tk.Label(self, text=message, font=('Helvetica', 24)).grid()

if __name__ == '__main__':
  TicTacToe()
#by Neksha
