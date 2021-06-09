import random

TEST_TRIPLES = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (6, 4, 2)]


def play_one_round():
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    available_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player_tokens = ["x", "o"]
    player = -1
    game_won = False
    
    while not game_won and available_positions:
        player = (player + 1) % 2
        print_board(board)
        position = None
        if player == 0:   
            position = get_new_position(player, player_tokens[player], available_positions)
        else:
            position = random_choice(available_positions)
            print(f"The bot chose position {position}.")
        board[position] = player_tokens[player]
        available_positions.remove(position)
        game_won = is_game_won(board)

    print_board(board)
    
    if game_won:
        print(f"Player {player + 1} won the game.")
    else:
        print("No winners. It is a tie.")
        

def print_board(b):
    print(f"{b[0]} {b[1]} {b[2]}")
    print(f"{b[3]} {b[4]} {b[5]}")    
    print(f"{b[6]} {b[7]} {b[8]}")


def get_new_position(player, token, available_positions):
    input_str = ""
    while True:
        input_str = input(f"Player {player + 1} enter next {token} token position: ")
        try:
            i = int(input_str)
            if i in available_positions:
                return i
            print(f"{i} is not an available position, try again.")
        except ValueError:
            print(f"'{input_str}' is not an available position, try again.")


def are_all_equal(board, pos_triple):
    return board[pos_triple[0]] == board[pos_triple[1]] \
           and board[pos_triple[0]] == board[pos_triple[2]]


def are_all_equal(board, i, j, k):
    return board[i] == board[j] and board[i] == board[k]
    

def is_game_won(board):
    for i, j, k in TEST_TRIPLES:
        if are_all_equal(board, i, j, k):
            return True
    return False


def random_choice(available_positions):
    i = random.randrange(len(available_positions))
    return available_positions[i]


def main():
    print("welcome to tic-tac-toe. Let's start.")
    while True:
        play_one_round()
        s = input("Enter 'y' to play again: ")
        if s != "y":
            break
           

if __name__ == '__main__':
    main()
