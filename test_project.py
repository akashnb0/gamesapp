from project import choose_game, play_rock_paper_scissors, is_winner, play_magic_ball, play_tic_tac_toe, initialize_board, update_board, is_spot_empty, check_winner, is_board_full, display_board

def test_choose_game():
    # Simulate user input and test for valid choices
    assert choose_game() is not None

def test_is_winner():
    assert is_winner('r', 's') == True
    assert is_winner('s', 'p') == True
    assert is_winner('p', 'r') == True
    assert is_winner('r','r') == False
    assert is_winner('p', 's') == False

def test_play_magic_ball(capfd):
    play_magic_ball()
    out, err = capfd.readouterr()
    assert out == 'Magic 8 Ball says : It is certain\n' or \
                   out == 'Magic 8 Ball says : It is decidedly so\n' or \
                   out == 'Magic 8 Ball says : Yes\n' or \
                   out == 'Magic 8 Ball says : Reply hazy try again\n' or \
                   out == 'Magic 8 Ball says : Ask again later\n' or \
                   out == 'Magic 8 Ball says : Concentrate and ask again\n' or \
                   out == 'Magic 8 Ball says : My reply is no\n' or \
                   out == 'Magic 8 Ball says : Outlook not so good\n' or \
                   out == 'Magic 8 Ball says : Very doubtful\n'

def test_initialize_board():
    assert initialize_board() == {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

def test_display_board():
    board = initialize_board()
    assert display_board(board) == f"{board[1]}|{board[2]}|{board[3]}   1 2 3\n-----\n{board[4]}|{board[5]}|{board[6]}   4 5 6\n-----\n{board[7]}|{board[8]}|{board[9]}   7 8 9"

def test_update_board():
    board = initialize_board()
    player = 'X'
    position = 2
    update_board(board, player, position)
    assert board == {1: ' ', 2: 'X', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

def test_is_spot_empty():
    board = initialize_board()
    player = 'X'
    position = 2
    update_board(board, player, position)
    assert is_spot_empty(board, 2) == False
    assert is_spot_empty(board, 4) == True

def test_check_winner():
    board = {1: 'X', 2: 'X', 3: 'X', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    assert check_winner(board, 'X') == True
    board = {1: 'X', 2: 'X', 3: 'O', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    assert check_winner(board, 'X') == False
    board = {1: 'X', 2: 'X', 3: 'O', 4: 'X', 5: 'O', 6: 'X', 7: 'O', 8: ' ', 9: ' '}
    assert check_winner(board, 'O') == True
    board = {1: 'X', 2: 'X', 3: 'X', 4: '', 5: ' ', 6: 'X', 7: ' ', 8: ' ', 9: 'X'}
    assert check_winner(board, 'X') == True

def test_is_board_full():
    board = {1: 'X', 2: 'X', 3: 'X', 4: '', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    assert is_board_full(board) == False
    board = {1: 'X', 2: 'X', 3: 'X', 4: 'O', 5: 'X', 6: 'O', 7: 'X', 8: 'O', 9: 'X'}
    assert is_board_full(board) == True
