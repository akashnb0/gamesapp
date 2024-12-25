import random
import art

def main():
    while True:
        print(art.text2art('GAMES'))
        game = choose_game()
        if game == 1:
            play_tic_tac_toe()
        elif game == 2:
            play_magic_ball()
        elif game == 3:
            play_rock_paper_scissors()
        else:
            continue
        request = input('Do you want to keep playing y/n? ').upper()
        if request in ['NO', 'N']:
            break

def choose_game():
    try:
        game_choice = int(input('welcome to Games by Akash!, If you want to exit press CTRL + C\nSelect a game :\n- 1 for Tic Tac Toe\n- 2 for Magic 8 Ball\n- 3 for Rock Paper Scissors\nAnswer: '))
        if game_choice not in [1, 2, 3]:
            raise Exception()
    except (ValueError, Exception):
        print('Please enter a valid number: 1, 2, or 3.')
    else:
        return game_choice

def play_rock_paper_scissors():
    print('Welcome to Rock Paper Scissors')
    user_choice = input("'r' for rock, 's' for scissors, 'p' for paper\n")
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        print('You tied!')
    elif is_winner(user_choice, computer_choice):
        print('You won!')
    else:
        print('You lost!')

def is_winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def play_magic_ball():
    answer_number = random.randint(1, 9)
    magic_responses = {
        1: 'It is certain',
        2: 'It is decidedly so',
        3: 'Yes',
        4: 'Reply hazy, try again',
        5: 'Ask again later',
        6: 'Concentrate and ask again',
        7: 'My reply is no',
        8: 'Outlook not so good',
        9: 'Very doubtful'
    }
    print(f'Magic 8 Ball says: {magic_responses[answer_number]}')

def play_tic_tac_toe():
    print('Tic Tac Toe started!')
    board = initialize_board()
    current_player, next_player = 'X', 'O'
    while True:
        try:
            print(display_board(board))
            position = input(f'{current_player} Role to play? ')
            if is_spot_empty(board, position):
                update_board(board, current_player, position)
                if check_winner(board, current_player):
                    print(display_board(board))
                    print(f"{current_player} has won the game.")
                    break
                if is_board_full(board):
                    print(display_board(board))
                    print('Game Over!')
                    break
                current_player, next_player = next_player, current_player
            else:
                continue
        except (ValueError, KeyError):
            print("Enter a value between 1 and 9: ")

def initialize_board():
    return {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}

def update_board(board, player, position):
    board[int(position)] = player

def is_spot_empty(board, position):
    return board[int(position)] == ' '

def check_winner(board, player):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

def is_board_full(board):
    return all(value != ' ' for value in board.values())

def display_board(board):
    return f'{board[1]}|{board[2]}|{board[3]}   1 2 3\n-----\n{board[4]}|{board[5]}|{board[6]}   4 5 6\n-----\n{board[7]}|{board[8]}|{board[9]}   7 8 9'

if __name__ == "__main__":
    main()