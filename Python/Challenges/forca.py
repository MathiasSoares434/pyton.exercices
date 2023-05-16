import random
def show_word(word, correct_letters):
    show= ''
    for letter in word:
        if letter in correct_letters:
            show+=letter+' '
        else:
            show+='_ '
    return show
def game_of_strenght(word):
    wrong_letters= []
    correct_letters= []
    shoots= 7
    print("*********************************")
    print("***Bem vindo ao jogo da FORCA!***")
    print("*********************************")
    print('\n' + 'Adivinhe a palavra secreta.')    
    while True:
        print('\n' + show_word(word, correct_letters))
        if shoots==0:
                    print("    _______________         ")
                    print("   /               \       ")
                    print("  /                 \      ")
                    print("//                   \/\  ")
                    print("\|   XXXX     XXXX   | /   ")
                    print(" |   XXXX     XXXX   |/     ")
                    print(" |   XXX       XXX   |      ")
                    print(" |                   |      ")
                    print(" \__      XXX      __/     ")
                    print("   |\     XXX     /|       ")
                    print("   | |           | |        ")
                    print("   | I I I I I I I |        ")
                    print("   |  I I I I I I  |        ")
                    print("   \_             _/       ")
                    print("     \_         _/         ")
                    print("       \_______/           ")
                    print(f"MORREU OTÁRIO HAHAHAHAHA a palavra era {word}")

                    break
        if all(letter in correct_letters for letter in word):
                print(f"Parabéns, você ganhou a palavra realmente era {word}!")
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
                break
        letter= input('Digite a letra: ').upper()
        if letter in word:
              correct_letters.append(letter)
        else:
              wrong_letters.append(letter)
              shoots-=1
              print(f'Letras erradas: {wrong_letters}.')
              print(f'Você ainda tem {shoots} tentativas.')   
word_secret= ['SPORT', 'SANTACRUZ', 'NAUTICO', 'RETRO', 'SALGUEIRO', 'IBIS']   
game_of_strenght(random.choice(word_secret))    
