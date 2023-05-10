board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
choice_player1 = ""
choice_player2 = ""
times_played = 0
game_on = False

def restart_game():
    global board
    global choice_player2
    global choice_player1
    global times_played
    global game_on
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    choice_player1 = ""
    choice_player2 = ""
    times_played = 0
    game_on = True
    display_board()
    marker_choice()
    make_choice()


def marker_choice():
    # What Will our Player Be
    global choice_player1
    global choice_player2
    marker = ''
    while marker != 'X' and marker != "O":
        marker = input("Choose Who Player 1 will be ( X or O): ")
    choice_player1 = marker

    # Assigning Player2 the Opposite Symbol
    if marker == "X":
        choice_player1 = "X"
        choice_player2 = "O"
    elif marker == 'O':
        choice_player1 = "O"
        choice_player2 = "X"
    global who_lastplayed
    who_lastplayed = choice_player1


def display_board():
    # Displays the Board

    # Separate the Boards From Each other
    print("\n" * 10)

    # The Board itself
    print(board[6] + '|' + board[7] + '|' + board[8])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[0] + '|' + board[1] + '|' + board[2])

    print("\n")


def make_choice():
    # inputing the area, That user wants to put his thing in
    global game_on
    global board
    global times_played
    final = ""

    if game_on:
        while True:
            try:
                choice = int(input("Where do you want to put it (NumPad Layout): "))
            except ValueError:
                print("invalid Answer")
                continue
            if choice in range(1, 10) and board[choice - 1] == " ":
                break
            elif choice in range(1, 10) and board[choice - 1] != " ":
                print("There is already something there so stop cheating")
                continue
            else:
                continue
        if times_played % 2 == 0:
            board[choice - 1] = choice_player1
        else:
            board[choice - 1] = choice_player2
        check_won()
        times_played += 1
        make_choice()
    elif not game_on:
        print("\n")
        while True:
            answer = input("Do You Still Want to Play? (Y/N): ")
            if answer == "Y":
                break
            elif answer == "N":
                print("\nAAHHH Man.... okay... Goodbye... :(")
                exit()
            else:
                continue

        # Reached IF user says "Y"
        restart_game()


def who_played_last():
    if times_played % 2 == 0:
        return choice_player1
    elif times_played % 2 != 0:
        return choice_player2


def check_won():
    # We gotta show the user how the game going right?
    display_board()
    global game_on

    # Row Checker
    if (board[0] == board[1] == [2] != " ") or (board[3] == board[4] == board[5] != " ") or (
            board[6] == board[7] == board[8] != " "):
        print(f"\n{who_played_last()} Won!")
        game_on = False
    # Colum Checker
    elif (board[6] == board[3] == board[0] != " ") or (board[7] == board[4] == board[1] != " ") or (
            board[8] == board[5] == board[2] != " "):
        print(f"\n{who_played_last()} Won!")
        game_on = False
    # Diagonal Checker
    elif (board[6] == board[4] == board[2] != " ") or (board[8] == board[4] == board[0] != " "):
        print(f"\n{who_played_last()} Won!")
        game_on = False
    # If Draw
    elif " " not in board:
        print(f"\nDraw!")
        game_on = False

    # If nothing we continue


# Now We start Running the game
display_board()
marker_choice()
make_choice()
