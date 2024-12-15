import random

WIN_CONDITIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def check_win(board):
    for a, b, c in WIN_CONDITIONS:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None


def is_draw(board):
    return " " not in board


def check_game_status(board):
    winner = check_win(board)
    if winner:
        return winner, False
    if is_draw(board):
        return None, False
    return None, True


def get_valid_move(board, current_player):
    while True:
        move = input(f"Player {current_player}, choose a position (1-9): ")
        if not move.isdigit():
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        position = int(move) - 1
        if position < 0 or position > 8:
            print("Out of range. Please enter a number between 1 and 9.")
            continue
        if board[position] != " ":
            print("That position is already taken. Choose another.")
            continue
        return position


def ai_move(board, ai_player, human_player):
    print(f"AI thinking...")
    available_positions = [i for i, v in enumerate(board) if v == " "]

    for pos in available_positions:
        board[pos] = ai_player
        if check_win(board) == ai_player:
            board[pos] = " "
            return pos
        board[pos] = " "

    for pos in available_positions:
        board[pos] = human_player
        if check_win(board) == human_player:
            board[pos] = " "
            return pos
        board[pos] = " "

    return random.choice(available_positions)


def play_game(mode):
    board = [" "] * 9
    current_player = "X"
    ai_player = "O" if mode == 2 else None

    while True:
        print_board(board)

        if mode == 1 or current_player == "X":
            position = get_valid_move(board, current_player)
        else:
            position = ai_move(board, ai_player, "X")

        board[position] = current_player

        winner, ongoing = check_game_status(board)
        if not ongoing:
            print_board(board)
            if winner:
                print(f"Player {winner} wins!")
            else:
                print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    while True:
        mode = get_game_mode()
        play_game(mode)
        if not restart_game():
            print("Exiting the game. Goodbye!")
            break


def get_game_mode():
    while True:
        mode_select = input("Choose a mode: \n1) Player 1 vs Player 2 \n2) Player 1 vs AI \n: ")
        if mode_select not in ["1", "2"]:
            print("Invalid choice. Please select 1 or 2.")
        else:
            return int(mode_select)


def restart_game():
    restart = input("Do you want to play again? (y/n): ").lower()
    return restart == 'y'


if __name__ == "__main__":
    main()
