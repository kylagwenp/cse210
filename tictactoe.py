from colorama import init, Fore, Back, Style

init()

numbers = []

def main():
    play = None
    while play != 'no':

        numbers.clear()
        for num in range(1,10):
            numbers.append(num)
        
        display_tictactoe()

        turn = False
        while turn != True:
            x_move = int(input(Fore.MAGENTA + Style.BRIGHT + "x's turn to choose a square (1-9): " ))
            print(Style.RESET_ALL)
            display_x_move(x_move)
            print(Style.RESET_ALL)
            display_tictactoe()
            print(Style.RESET_ALL)
            turn = check_winner()
            if turn == True:
                continue
            o_move = int(input(Fore.YELLOW + "o's turn to choose a square(1-9): "))
            print(Style.RESET_ALL)
            display_o_move(o_move)
            print(Style.RESET_ALL)
            display_tictactoe()
            print(Style.RESET_ALL)
            turn = check_winner()

        else:
            print(Fore.GREEN + Style.BRIGHT + 'Winner!')
            play = input('Do you want to play again? ')
    else:
        print('Thank you for playing!')

def display_tictactoe():
    one = numbers[0]
    two = numbers[1]
    three = numbers[2]
    four = numbers[3]
    five = numbers[4]
    six = numbers[5]
    seven = numbers[6]
    eight = numbers[7]
    nine = numbers[8]

    print(f'{one}|{two}|{three}')
    print('-+-+-')
    print(f'{four}|{five}|{six}')
    print('-+-+-')
    print(f'{seven}|{eight}|{nine}')
    print()

def display_x_move(move):
    index = move - 1
    numbers[index] = 'x'

def display_o_move(move):
    index = move - 1
    numbers[index] = 'o'

def check_winner():
    if numbers[0] == numbers[1] == numbers[2]:
        turn = True
        return turn
    elif numbers[3] == numbers[4] == numbers[5]:
        turn = True
        return turn
    elif numbers[6] == numbers[7] == numbers[8]:
        turn = True
        return turn
    elif numbers[0] == numbers[3] == numbers[6]:
        turn = True
        return turn
    elif numbers[1] == numbers[4] == numbers[7]:
        turn = True
        return turn
    elif numbers[2] == numbers[5] == numbers[8]:
        turn = True
        return turn
    elif numbers[0] == numbers[4] == numbers[8]:
        turn = True
        return turn
    elif numbers[2] == numbers[4] == numbers[6]:
        turn = True
        return turn

main()
