import random

def print_mensage_open():
    print("*********************************")
    print("***Bem vindo ao jogo da FORCA!***")
    print("*********************************")

    
def print_mensage_winner():
    print("Parabéns, você ganhou!")
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





def draw_forca(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
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
        print("MORREU OTÁRIO HAHAHAHAHA")

    print()

def load_word_secret():
    words= ['Jujuba', 'Carniça', 'Bob', 'Lakers', 'Santa cruz', 'Celtics', 'Sport']
    number= random.randrange(0, len(words))
    word_secret= words[number].upper()
    return word_secret
def init_letters_correct(word):
    return ["_" for letter in word] 
def ask_shoot():
    shoot= input('Digite uma letra: ')
    shoot= shoot.strip().upper()
    return shoot
def check_shoot_correct(shoot, letters_corrects, word_secret):
    index=0
    for letter in word_secret:
        if shoot==letter:
            letters_corrects[index]=letter
        index+=1



def playGame():
    print_mensage_open()
    word_secret= load_word_secret()
    letters_corrects= init_letters_correct(word_secret)
    die= False
    correct= False
    mistakes= 0
    letters_missing= len(letters_corrects)
    print(letters_corrects)
    while(not correct and not die):
        shoot= ask_shoot()
        if (shoot in word_secret):
            check_shoot_correct(shoot, letters_corrects, word_secret)
            letters_missing= str(letters_corrects.count('_'))
            if(letters_missing=="0"):
                print("Parabéns!! Você encontrou todas as letras formando uma palavra'{}'".format(word_secret.upper()))
                print_mensage_winner()
                
            else:
                mistakes+=1
                print(letters_corrects)
                print('Você ainda tem que acertar {} letras'.format(letters_missing))
                print('Você ainda tem {} tentativas'.format(7-mistakes))
                draw_forca(mistakes)

            die = mistakes == 7
            correct="_" not in letters_corrects
            print(letters_corrects)
        if (correct):
            print_mensage_winner()


    print("Fim do jogo")

            
playGame()


