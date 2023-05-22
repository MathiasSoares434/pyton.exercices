def show_gameBoard(gameBoard):
    for line in gameBoard:
        print(' | '.join(line))
        print("-" * 9)
def seeing_winner(gameBoard, player):
    for line in gameBoard:
       if line.count(player)==3:
           return True
    for column in range(3):
        if gameBoard[0][column]==gameBoard[1][column]==gameBoard[2][column]==player:
            return True
    if gameBoard[0][0]==gameBoard[1][1]==gameBoard[2][2]==player:
        return True
    if gameBoard[0][2]==gameBoard[1][1]==gameBoard[2][0]==player:
        return True
    return False
def play():
    gameBoard= [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player= 'X'
    game_is_over= False

    while not game_is_over:
        show_gameBoard(gameBoard)
        line=int(input('Digite o número da linha na posição entre 0 1 2: '))
        column=int(input('Digite o número da coluna na posição entre 0 1 2: '))

        if gameBoard[line][column] == " ":
            gameBoard[line][column] = player

            if seeing_winner(gameBoard, player):
                show_gameBoard(gameBoard)
                print(f'O {player} ganhou o jogo')
                print("       ___________      ")
                print("      '._==_==_=_.'     ")
                print("      .-\\:      /-.    ")
                print("     | (|:.     |) |    ")
                print("      '-|:.     |-'     ")
                print("        \\::.    /      ")
                print("         '::. .'        ")
                print("           ) (          ")
                print("         _.' '._        ")
                print("        '-------'       ")
                game_is_over=True
            elif " " not in gameBoard[0] and " " not in gameBoard[1] and " " not in gameBoard[2]:
                show_gameBoard(gameBoard)
                print('EMPATOU')
                game_is_over=True
            else:
                player= "O" if player=="X" else "X"
        else:
            print("Você executou algum comando errado, tente novamente")

play()           