board = [
  0, 0, 0,
  0, 0, 0,
  0, 0, 0
]

p1_moves = set()
p2_moves = set()

winner = None

# player 1 = 1
# player 2 = 2

def check_win(moves):
  # there are 8 ways to win
  # (1, 2, 3), (3, 6, 9), (7, 8, 9), (1, 4, 7)
  # (1, 5, 9), (3, 5, 7), (2, 5, 8), (4, 5, 6)

  return (
    {1, 2, 3}.issubset(moves)
    or
    {3, 6, 9}.issubset(moves)
    or
    {7, 8, 9}.issubset(moves)
    or
    {1, 4, 7}.issubset(moves)
    or
    {1, 5, 9}.issubset(moves)
    or
    {3, 5, 7}.issubset(moves)
    or
    {2, 5, 8}.issubset(moves)
    or
    {4, 5, 6}.issubset(moves)
  )


def print_board():
  for i in range(len(board)):
    if board[i] == 0:
      print('_ ', end='')
    elif board[i] == 1:
      print('x ', end='')
    else:
      print('o ', end='')

    if (i + 1) % 3 == 0:
      print()

def main():
  print('Welcome to Tic-Tac-Toe!')
  global board, p1_moves, p2_moves, winner
  play_again = True

  while play_again:
    board = [0] * 9
    p1_moves = set()
    p2_moves = set()
    winner = None
    print_board()
    while True:
      # player 1 input
      p1_input = int(input('Player 1 move: '))
      p1_moves.add(p1_input)
      board[p1_input - 1] = 1
      print_board()
      if check_win(p1_moves):
        winner = 'Player 1'
        break

      # player 2 input
      p2_input = int(input('Player 2 move: '))
      p2_moves.add(p2_input)
      board[p2_input - 1] = 2
      print_board()
      if check_win(p2_moves):
        winner = 'Player 2'
        break

    print(f'{winner} won!')
    response = str(input('Play again? (y/n):  '))
    play_again = True if response.lower() == 'y' else False 

if __name__ == '__main__':
  main()
  