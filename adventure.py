#!/usr/bin/python
# -*- coding: utf-8 -*-
# You can use this workspace to write and submit your adventure game project.

import time
import random
import sys
import unicodedata
import enum


class Color(enum.Enum):

    red = "\033[91m"
    purple = "\033[95m"
    blue = "\033[94m"
    cyan = "\033[96m"
    green = "\033[92m"
    black = "\033[0m"
    bold = "\033[1m"
    underline = "\033[4m"

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def print_pause(message, delay=2):
    print(Color.get_color() + message)
    time.sleep(delay)


# def print_pause(message_to_print, sleep_time=2):
# print(message_to_print)
# time.sleep(sleep_time)


def valid_input(message_to_print, options):
    while True:
        response = input(message_to_print).lower()
        if response in options:
            return response
        print("Wrong expected input")


def play_again():
    output_option3 = valid_input(
        "Would you like to play again? (y/n)", options=["y", "n"]
    )
    if output_option3 == "y":
        print_pause("Excellent! Restarting the game ...")
    elif output_option3 == "n":
        print_pause("Thanks for playing! See you next time.")
        exit(0)


def runAction():
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.\n", 2)
    # play_game


def fightAction(fight_texts):
    for text in fight_texts:
        print_pause(text)
    print_pause("\n")


def fight_choice(fight_texts):
    output_option2 = valid_input(
        "Would you like to do fightAction OR runAction ?\n", ["1", "2"]
    )
    if output_option2 == "1":
        fightAction(fight_texts)
        return True
    elif output_option2 == "2":
        runAction()
        return False


def house(creatures, weapon):
    print_pause("\nYou approach the door of the house.")
    print_pause(
        "\nYou are about to knock when the door opens and out steps a "
        + creatures
        + "."
    )
    print_pause("\nEep! This is the " + creatures + "'s house!")
    print_pause("\nThe " + creatures + " attacks you!\n")
    if weapon == "badKnife":
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
        playerChoice = fight_choice(
            [
                "You do your best...",
                "but your dagger is no match for the "
                + creatures
                + ".You have been defeated!",
            ]
        )
    elif weapon == "newKnife":
        playerChoice = fight_choice(
            [
                "As the "
                + creatures
                + " moves to attack, "
                + "you unsheath your new newKnife.",
                "The newKnife of Alexzandra the great shines "
                + "brightly in your hand as you "
                + "brace yourself for the attack.",
                "But the pirate takes one look at your "
                + "shiny new weapon and runs away!",
                "You have rid the town of the "
                + creatures
                + ". "
                + "You are victorious!",
            ]
        )
    return playerChoice


def cave(weapon):
    if weapon == "badKnife":
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical newKnife!")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        weapon = "newKnife"
    elif weapon == "newKnife":
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
    print_pause("You walk back out to the field.\n")
    return weapon


def intro(creatures):
    print_pause(
        "You find yourself standing in an open field, filled with "
        + "grass and yellow wildflowers."
    )
    print_pause(f"Rumor has it that a {creatures} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def play_game(creatures, weapon):
    while True:
        print_pause("Enter 1 to approach and knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        print_pause("What would you like to do?")
        output_option = valid_input("(Please enter 1 or 2).\n", ["1", "2"])
        if output_option == "1":
            playerChoice = house(creatures, weapon)
            if playerChoice:
                break
        elif output_option == "2":
            weapon = cave(weapon)


def adventure_game():
    weapon = "badKnife"
    creaturesList = ["medusa", "pirate", "dinosaur", "wicked fairie"]
    while True:
        creatures = random.choice(creaturesList)
        intro(creatures)
        play_game(creatures, weapon)
        play_again()


if __name__ == "__main__":
    adventure_game()
