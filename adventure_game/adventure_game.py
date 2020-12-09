

import time


import random


def random_choice():
    list = ["Mumbai", "Hyderbad", "Delhi", "Kolkata", "Calicut", "Chennai"]
    city = random.choice(list)
    print_pause("He has his hidden research lab somewhere here.So he will be"
                + " somewhere here in "+city+"'s dumpward.")
    print_pause("Now we are in "+city+" dumpward.")


def print_pause(text):
    print(text)
    time.sleep(2)


def intro():
    print_pause("You are Kahil and you are in so angry and diappointment mood"
                + " " + "that your parents were kidnapped recently.")
    print_pause("World's one of most smartest person kidnapped them.")
    print_pause("So to find them you want to take the help of Rabath.")
    print_pause("Rabath is the only smarter and intelligent guy who"
                + " can help you,he's the angry guy too....")
    random_choice()
    print_pause("SO,LET'S FIND RABATH"+"!!"+" and convince him....")


def after_end():
    while True:
        play_again = input("DO you want to play again y/n\n").lower()
        if play_again == "y":
            print_pause("Loading your game....")
            return "y"
        elif play_again == "n":
            print_pause("GOOD BYE"+"!!")
            return "n"
        else:
            print_pause("I did not get you....")


def game():
    while True:
        intro()
        while True:
            print_pause("It's dark here.\n1.Will you find torch.\n2.Or will"
                        + " you directly enter the dumpward.")
            response1 = input("Please enter the number:")
            if response1 == "1":
                print_pause("There's a box right side of you search in that."
                            + " You will get it and enter the dumpward"
                            + " silently.")
                print_pause("THAD, THAD, THAD, THAD....\nThere's a sound from"
                            + " middle of the dumpward..")
                while True:
                    print_pause("1.Do you want to go there to check out\n"
                                + "2.Or wait for a while to see what happens?")
                    response2 = input("Pleas enter the number:")
                    if response2 == "1":
                        print_pause("Ohhhh"+"!!!!"+" finally we found Rabath.."
                                    + "HE SAY YOU AND HE IS IN ANGRY MOOD")
                        print_pause("Thinking of someone, he shot you with"
                                    + " laser gun in his hand"+"!!!!!!!!!")
                        print_pause("THANKGOD IT MISSED YOU...")
                        print_pause("WAAAAHHHH,WAAAAHHH,WAAAAAAHHHH...."
                                    + "Police siren")
                        print_pause("Because of that gun sound, Police are"
                                    + " on the way, if run back they may get"
                                    + " you.")
                        while True:
                            print_pause("1.Do you want to stay there praise"
                                        + " him....convincingly tell him your"
                                        + " story.")
                            print_pause("2.Or run back.")
                            response3 = input("Please enter the number:")
                            if response3 == "1":
                                print_pause("LUCKILY"+"!!"+" He got convinced"
                                            + " with your story....")
                                print_pause("And he promised that he will help"
                                            + " you to find your parents....")
                                break
                            elif response3 == "2":
                                print_pause("You ran back and police"
                                            + " cought you")
                                print_pause("You lost your chance of"
                                            + " finding your parents....")
                                break
                            else:
                                print_pause("I did not get you....")
                        after_end()
                        break
                    elif response2 == "2":
                        print_pause("It's waste of waiting here...")
                        print_pause("Sound keeps on getting louder...its"
                                    + " better to go there...")
                    else:
                        print_pause("I did not get you....")
                break
            elif response1 == "2":
                print_pause("If you are in so hurry and confident go head"
                            + "!!")
                print_pause("OHHhh....Here's a pit...You fell in "
                            + "that and died")
                print_pause("Better Luck Next time"+"!!")
                after_end()
                break
            else:
                print_pause("I did not get you....")
        if after_end() == "n":
            break


game()
