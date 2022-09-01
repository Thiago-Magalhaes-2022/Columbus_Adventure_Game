
import time
import random


def print_pause(message_to_print):
    time.sleep(1)
    print(message_to_print)
    time.sleep(1)


def game_introduction():
    print_pause("\nBem-vindos à Viagem de Colombo!\n")
    print_pause("Você irá iniciar uma aventura fabulosa "
                "pelo mar-oceano!")
    print_pause("\nVocê deixa o porto de Palos de la Frontera na "
                "Espanha num domingo pela manhã, com uma multidão "
                "presente para se despedir e desejar boa sorte!\n")


def intro_pirates():
    print_pause("\nO vento está bom, o tempo está aberto, "
                " os marinheiros estão animados e há um infinito "
                "céu limpo e azul sobre as cabeças da tripulação... ")
    print_pause("\nDe repente, uma esquadra de 4 pequenas caravelas "
                "se aproxima... É um ataque pirata!\n")


def pirates_question():
    while (True):
        pirates = input("O que você faz?\n\n"
                        "Tecle 1 para atacar os piratas, ou..\n"
                        "Tecle 2 para fugir deles.. \n\n")
        if str(pirates) == "1":
            calm_part()
            break
        elif str(pirates) == "2":
            print_pause("\nOh não!")
            print_pause("\n\nVocê foi capturado pelos piratas "
                        "quando tentava fugir deles...\n\n")
            print_pause("Fim do jogo.")
            function_play_again()
        else:
            print_pause("Não entendi.")


def intro_storm():
    print_pause("\nNos primeiros três dias o tempo está ótimo, os "
                "marinheiros estão animados e tudo parece "
                "andar muito bem..")
    print_pause("\nDe repente o tempo fecha, e surge uma "
                "tempestade aterrorizante!")


def intro_disease():
    print_pause("\nNa primeira semana o tempo está lindo, a "
                "tripulação está otimista e animada e tudo "
                "parece perfeito..")
    print_pause("\nDe repente, uma estranha doença ataca a pele "
                "de parte dos marinheiros!")

def calm_part():
    print_pause("\nVocê conseguiu vencer os piratas! Parabéns!\n")
    print_pause("A viagem segue seu rumo pelo Oceano Atlântico.")
    print_pause("\nPor 30 dias e 30 noites as coisas vão bem, o "
                "vento segue firme e a comida é suficiente..\n")


def riot():
    print_pause("\nApós um certo tempo, as coisas começam "
                "a ficar mais difíceis.. \n\n"
                "Há falta de comida, a tripulação está "
                "exausta... e... \n")
    print_pause("Há uma rebelião dos marinheiros a bordo! \n")


def lost_ship():
    print_pause("\nMas agora uma de suas caravelas se perdeu "
                "pelo caminho.\n")


def lull_point():
    print_pause("Parabéns, você superou mais um desafio!\n\n"
                "Agora você tem um longo período de paz e bom tempo.."
                "\n\nMas... o vento está ficando cada vez mais "
                "fraco e... Ocorre uma calmaria!")

    while(True):
        lull_point = input("\nO que você faz? Tecle 1: Para forçar "
                           "os marinheiros a remar mais forte"
                           "... ou..\nTecle2: Para preservar a "
                           "tripulação para os próximos desafios... ")
                          
                           
        if str(lull_point) == "2":
            break
        elif str(lull_point) == "1":
            print_pause("\nQue pena! Você gastou toda a energia "
                        "dos marujos.. Alguns morreram de fome, "
                        "outros de insolação.")
            print_pause("\nFim do jogo.\n")
            function_play_again()
        else:
            print_pause("\nDesculpe, não entendi.")


def riot_defeat():
    print_pause("\nOh não! Você foi assassinado "
                "durante a rebelião.\n\n")
    print_pause("Fim do jogo.\n\n")
    function_play_again()


def lost_ship_defeat():
    print_pause("\nQue pena, você se perdeu pelo mar tentando encontrar a caravela desviada.\n\n")
    print_pause("Fim do jogo.\n\n")
    function_play_again()


def win_game():
    print_pause("\n\nParabéns! Terra à vista! Você chegou "
                "na América!\n\n")
    print_pause("\nPode comemorar!\n")
    print_pause("\n\nEsta é uma terra de fabulosas civilizações"
                ", cheia da mais bonita gente, cultura, "
                "crenças e natureza exuberante! Todos são "
                "bem-vindos! Favor respeitar a terra e a"
                " diversidade de nosso povo!\n\n")
    function_play_again()


def text_stop():
    while(True):
        first_stop = input("\nTecle 1 para continuar "
                           "ou tecle 2 para sair. ")
        if str(first_stop) == "2":
            print_pause("\nCerto, até logo!\n")
            function_play_again()

        elif str(first_stop) == "1":
            break
        else:
            print_pause("Desculpe, não entendi.")


def missing_question():
    while(True):
        missing_answer = input("O que você faz?\n\nTecle 1: Partir "
                               "em busca da caravela perdida.. ou..\n"
                               "Tecle 2: Esquecer a caravela perdida "
                               "e seguir viagem..\n\n")
        if str(missing_answer) == "2":
            break
        elif str(missing_answer) == "1":
            lost_ship_defeat()

        else:
            print_pause("Desculpe, não entendi.\n")


def riot_question():
    while (True):
        riot_answer = input("\nWhat do you do?"
                            "\n\nFight against "
                            "the mariners, press 1\n\nMake agreement"
                            " with the mariners, press 2\n\n")

        if str(riot_answer) == "2":
            print_pause("\nParabéns! Você foi muito bem na "
                        "negociação com os marinheiros!\n\n")
            break
        elif str(riot_answer) == "1":
            riot_defeat()

        else:
            print_pause("\nDesculpe, não entendi.\n\n")


def disease_question():
    while(True):
        desease = input("\nO que você faz?\n\nTecle 1: Para isolar "
                        "os marujos com sintomas num barco separado.."
                        " ou.. \nTecle 2: Para se livrar dos"
                        " contaminados e seguir viagem..\n")
        if str(desease) == "1":
            print_pause("\n\nÓtimo trabalho!\n\nA tripulação se sente"
                        " melhor e a jornada marítima continua!\n\n")
            break
        elif str(desease) == "2":
            print_pause("\nOh não! Os marinheiros se revoltaram com "
                        "a sua atitude e o assassinaram numa "
                        "emboscada.\n")
            print_pause("Fim do jogo.\n\n")
            function_play_again()
        else:
            print_pause("\nDesculpe, não entendi. ")


def speed_up_question():
    while(True):
        storm = input("\nO que você faz?\n\n"
                      "Tecle 1: Para fazer a tripulação acelerar "
                      "a velocidade, ou..\nTecle 2: Para parar "
                      "e aguardar o fim da tempestade.. \n\n")
        if str(storm) == "1":
            print_pause("Ótima decisão! Vocês fugiram da "
                        "tempestade! Festa a bordo!\n\n")
            break
        elif str(storm) == "2":
            print_pause("\nQue pena! Você teve as caravelas "
                        "destruídas pela tempestade e todos "
                        "morreram afogados em alto mar.\n")
            print_pause("Fim do jogo.\n\n")
            function_play_again()
        else:
            print_pause("\nDesculpe, não entendi. ")


def function_play_again():
    desire = input("Você gostaria de jogar de novo? \n\n"
                   "Tecle 1 para jogar de novo ou"
                   " tecle 2 para sair... ")
    desire = desire.lower()
    if str(desire) == "1":
        main()
    elif str(desire) == "2":
        print_pause("\nCerto, até logo!\n\nFim do jogo.\n\n")
        quit()
    else:
        print_pause("Desculpe, não entendi. ")
        desire = input("Você gostaria de jogar de novo? \n\n"
                   "Tecle 1 para jogar de novo ou"
                   " tecle 2 para sair... ")
        desire = desire.lower()
        if str(desire) == "1":
            main()
        elif str(desire) == "2":
            print("Certo, até logo!")
            quit()
        else:
            print("Desculpe, não entendi. ")
            function_play_again()


def main_01():
    game_introduction()
    text_stop()
    intro_pirates()
    pirates_question()
    riot()
    riot_question()
    lost_ship()
    missing_question()
    win_game()


def main_02():
    game_introduction()
    text_stop()
    intro_storm()
    speed_up_question()
    lull_point()
    lost_ship()
    missing_question()
    win_game()


def main_03():
    game_introduction()
    text_stop()
    intro_disease()
    disease_question()
    intro_pirates()
    pirates_question()
    lost_ship()
    missing_question()
    win_game()


def main_04():
    game_introduction()
    text_stop()
    intro_disease()
    disease_question()
    intro_storm()
    speed_up_question()
    lull_point()
    win_game()


def main():
    version = random.choice(["1", "2", "3", "4"])

    if (version) == "1":
        main_01()

    if (version) == "2":
        main_02()

    if (version) == "3":
        main_03()

    if (version) == "4":
        main_04()

if __name__ == '__main__':
    main()
