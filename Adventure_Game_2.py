
import time
import random


def print_pause(message_to_print):
    time.sleep(1)
    print(message_to_print)
    time.sleep(1)


def game_introduction():
    print_pause("\nWelcome to Christopher Colombus Voyage Game!\n")
    print_pause("You are about to start a fabulous adventure "
                "through the sea!")
    print_pause("\nYou leave the port of Palos de la Frontera in "
                "Spain in a sunday morning, with an enormous "
                "croud cheering.\n")


def intro_pirates():
    print_pause("\nWind is good, weather is beautiful, mariners are "
                "cheerful and\nthere is this endless clean blue sky "
                "above the crew...")
    print_pause("\nOut of a sudden, a squad of 4 small ships "
                "approach... \n\nAnd.. You are attacked by "
                "pirates!\n")


def pirates_question():
    while (True):
        pirates = input("What do you do?\n\n"
                        "Please press 1 to attack the pirates or..\n"
                        "Press 2 to run from them.. \n\n")
        if str(pirates) == "1":
            calm_part()
            break
        elif str(pirates) == "2":
            print_pause("\nSorry!")
            print_pause("\n\nYou have been caught by the "
                        "pirates trying to run from them.\n")
            print_pause("Game Over.")
            function_play_again()
        else:
            print_pause("Sorry, I don't understand.")


def intro_storm():
    print_pause("\nIn the first three days the weather is just "
                "beautiful, mariners are cheerful and everything "
                "seems perfect..")
    print_pause("\nOut of a sudden, there is an enormous storm!")


def intro_disease():
    print_pause("\nIn the first week the weather is so "
                "beautiful, mariners are cheerful and everything "
                "seems perfect..")
    print_pause("\nOut of a sudden, a strange desease appears on "
                "the skin of some mariners!")


def calm_part():
    print_pause("\nYou have destroyed the pirates! Congrats!\n")
    print_pause("The voyage follows nicely it's way through the"
                " Atlantic Ocean.")
    print_pause("\nFor 30 days and 30 nights things go well, wind "
                "is good, food is enough..\n")


def riot():
    print_pause("\nAfter that time, things start to become harder, "
                "food is lacking,\nmariners are tired... and...\n")
    print_pause("There is a mariners riot on the ship! \n")


def lost_ship():
    print_pause("\nBut now looks like one of your ships is "
                "missing.\n")


def lull_point():
    print_pause("You overcome all the problems! Congrats!\n\n"
                "Now you have a long period of good weather "
                "and peaceful times.\n\nBut...  the wind is "
                "getting weak for so many days and...\n"
                "You have a lull!")

    while(True):
        lull_point = input("\nWhat do you do? To make mariners "
                           "paddle harder press 1.. or..\n\n"
                           "Preserve them at all to prepare"
                           " for the next times press 2..\n\n")

        if str(lull_point) == "2":
            break
        elif str(lull_point) == "1":
            print_pause("\nSorry! You wasted all the energy of "
                        "the crew. Some of the man died from "
                        "hunger, some from insolation.")
            print_pause("\nGame Over.\n")
            function_play_again()
        else:
            print_pause("\nSorry! I don't understand what"
                        " you mean.")


def riot_defeat():
    print_pause("\nSorry you have been murdered in the riot.\n\n")
    print_pause("The game is over.\n")
    function_play_again()


def lost_ship_defeat():
    print_pause("\nSorry, you have lost yourself trying to find the "
                "missing ship.\n\n")
    print_pause("The game is over.\n")
    function_play_again()


def win_game():
    print_pause("\n\nCongratulations! You reached America!\n\n")
    print_pause("\nGo celebrate this!\n")
    print_pause("\n\nThis is a land of great civilizations, "
                "full of gorgeous people, culture, nature and "
                "beliefs.\n\nEveryone is welcome! Please be nice, "
                "and respect the diversity of our peoples!\n")
    function_play_again()


def text_stop():
    while(True):
        first_stop = input("\nPress 1 to continue "
                           "or press 2 to exit. ")
        if str(first_stop) == "2":
            print_pause("\nOk! Good Bye!\n")
            function_play_again()

        elif str(first_stop) == "1":
            break
        else:
            print_pause("Sorry, I don't understand.")


def missing_question():
    while(True):
        missing_answer = input("What do you do?\n\nGo look "
                               "for the missing ship, press 1..\n"
                               "Forget about the ship and go"
                               " ahead, press 2..\n\n")
        if str(missing_answer) == "2":
            break
        elif str(missing_answer) == "1":
            lost_ship_defeat()

        else:
            print_pause("Sorry, I don't understand"
                        " what you mean.\n")


def riot_question():
    while (True):
        riot_answer = input("\nWhat do you do?"
                            "\n\nFight against "
                            "the mariners, press 1\n\nMake agreement"
                            " with the mariners, press 2\n\n")

        if str(riot_answer) == "2":
            print_pause("\nCongrats!\n\nYou have been very "
                        "well at the negotiation with the mariners!")
            break
        elif str(riot_answer) == "1":
            riot_defeat()

        else:
            print_pause("\nSorry, I don't understand what you "
                        "mean.\n\n")


def disease_question():
    while(True):
        desease = input("\nWhat do you do?\n\nPress 1 - to isolate"
                        " the mariners with symptoms in a"
                        " separated ship, or..\n"
                        "Press 2 - to get rid of the contaminated"
                        " mariners..\n")
        if str(desease) == "1":
            print_pause("\n\nVery good job!\n\n The mariners"
                        " feel better, and the jorney continues!\n\n")
            break
        elif str(desease) == "2":
            print_pause("\nSorry! The mariners got upset with your "
                        "attitude and killed you.")
            print_pause("Game Over.\n\n")
            function_play_again()
        else:
            print_pause("\nSorry, I don't understand. ")


def speed_up_question():
    while(True):
        storm = input("\nWhat do you do?\n\n"
                      "Please press 1 to speed up or..\n\n"
                      "Press 2 to stop and wait for the storm to "
                      "finish.. \n\n")
        if str(storm) == "1":
            print_pause("Excellent decision! Mariners"
                        "are happy with you!\n\n")
            break
        elif str(storm) == "2":
            print_pause("\nSorry! You got yourself wrecked "
                        "by the storm.\n")
            print_pause("Game Over.\n\n")
            function_play_again()
        else:
            print_pause("\nSorry, I don't understand. ")


def function_play_again():
    desire = input("Would you like to play again? \n\n"
                   "Press 1 to play again or 2 to quit.. ")
    desire = desire.lower()
    if str(desire) == "1":
        main()
    elif str(desire) == "2":
        print_pause("\nOK, good bye!\n\nThe game is over!\n\nThanks"
                    " for playing!\n\n")
        quit()
    else:
        print_pause("Sorry, I don't understand. ")
        desire = input("Would you like to play again? \n"
                       "Press 1 to play again or 2 to quit.. ")
        desire = desire.lower()
        if str(desire) == "1":
            main()
        elif str(desire) == "2":
            print("OK, good bye!")
            quit()
        else:
            print("Sorry, I don't understand. ")
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
