# Rebecca Filardo for Udacity course homework. May 2020

# THINGS TO BE CHECKED

# IDLE

# In IDLE if I leave the cursor in a random place on the terminal,
# and then run this from the menu, with the cursor in the wrong place,
# strange things happen.

# Is this an IDLE problem or is it a flaw in my script?

# In IDLE, if I move the cursor a few lines up the output, and then press
# Return, it uses that line as output. This seems like it might be
# intentional IDLE functionality...

# NOTES

# warehouse -- list. the fixed list of pigment from which the play list
# is randomly selected.
# the player does not see nor have access to this list.

# shop -- list. the randomly generated ingredients list
# which will be made available to the player during that instance of the game.

# options -- list. the status of shop during the game
# (before and after the player has chosen)
# options is that same list, after one item has been chosen and removed

# necessary_ingredients -- list. the required ingredients
# to make the chosen colour
# this is the list that will need to be matched for the player to win the game

# for style checking:
# cd Dropbox/Rebecca-Private/Learning/Introduction-to-Programming/
# pycodestyle adventure_game.py

# IMPORT THE NECESSARIES
import time
import random
from collections import Counter
import collections

# CREATE OR INITIALIZE THE LISTS
candidate_colours = ['purple', 'orange', 'green']
warehouse = ['red', 'yellow', 'blue']

# DEFINE THE FUNCTIONS


def print_pause(message_to_print):

    print(message_to_print)
    time.sleep(0.5)


def intro():

    print_pause("** PIGMENT MIXING **\n")
    print_pause("Welcome to the pigment mixing challenge.\n\n")

    print_pause("HOW TO WIN\n")

    print_pause("You can pour two pigments into the vat. \n")
    print_pause("If you pour two correct pigments into the vat, "
                "you will succeed in making your chosen colour.\n")

    print_pause("If you choose the right pigment twice, "
                "you can try again.")

    print_pause("However, if at any time, you choose a wrong "
                "pigment, the game will end.")


def generate_the_shelf():

    in_shop = []
    total_pots = 0

    while total_pots < 6:
        in_shop.append(random.choice(warehouse))
        total_pots += 1

    in_shop.sort()
    return(in_shop)


def show_a_counted_list(in_shop):

    for key, value in Counter(in_shop).items():
        if value == 1:
            wording = "pot of"
        else:
            wording = "pots of"
        print("We have", value, wording, key, "pigment.")

    print("\n")


def valid_input_two(prompt, option1, option2):

    while True:
        response = input(prompt).lower()

# 27 May 2020. NOTE TO SELF -- similar lines, first one is backwards,
# second one is right. (Need to think about this a bit.)

# 28 May 2020. This did pass, however I now understand why the first one was
# wrong. I also see why "=="" would have been better than "in" in this context
# "in" is when there are multiple things to look at 
# e.g. "if response is in option1, option2, or option3"
# as option1 only has one value, there's no "in" to be used it
# is either equal to it, or not
# also, I see that if you say "is option in response", if option1 is
# "y" and option2 is "n". If you say "is option1 in response" and 
# response is ynynyny, then option1 is in response, even though
# response is not a good answer. 
# the other way around, you don't get that problem 
# 
#
#       if option1 in response:
        if response in option1:
            return response
        elif response in option2:
            return response
        else:
            print_pause("Sorry, I don't understand.")


# 27 May 2020 corrected, as for above
def valid_input_three(prompt, option1, option2, option3):

    while True:
        response = input(prompt).lower()
        if response in option1:
            return response
        elif response in option2:
            return response
        elif response in option3:
            return response
        else:
            print_pause("Sorry, I don't understand.")


def identify_necessary_ingredients(chosen_candidate):

    if chosen_candidate == 'purple':
        return(['blue', 'red'])
    elif chosen_candidate == 'orange':
        return(['red', 'yellow'])
    elif chosen_candidate == 'green':
        return(['yellow', 'blue'])


def invitation_to_play():

    accept = valid_input_two("\nDo you want to mix pigments today?"
                             " (y/n)\n\n", "y", "n")

    if accept == 'n':
        print("OK. Maybe next time! :-) Goodbye.")

    elif accept == 'y':
        can_it_be_done()


def go_again():

    response = valid_input_two("\nWould you like to play again? "
                               "(y/n)\n\n", "y", "n")
    if response == "n":
        print_pause("OK. Thank you for playing! :-) Goodbye!")
    elif response == "y":
        print_pause("\nAlrighty, then! Let's keep going!")
        can_it_be_done()


def can_it_be_done():

    in_shop = generate_the_shelf()

    print_pause("\nWhat colour you wanna make?")

    chosen_candidate = valid_input_three("\npurple? \norange? \ngreen?\n\n"
                                         "(Type the name of "
                                         "the colour you want to make.)\n\n",
                                         "purple", "orange", "green")

    if chosen_candidate not in candidate_colours:
        chosen_candidate = ''
        print("That is not on the menu.")

    else:
        print(f"\nOK, you want to make {chosen_candidate}\n"
              "This is what we've got on the shelf:\n")

        show_a_counted_list(in_shop)

        necessary_ingredients = identify_necessary_ingredients(
            chosen_candidate)
        necessary_ingredients_set = set(necessary_ingredients)

        options = in_shop
        options_set = set(options)
        number_of_unique_options = len(set(options))

        if options_set.intersection(necessary_ingredients_set) == (
                                    necessary_ingredients_set):
            print(f"Yes, you can make {chosen_candidate} today.\n\n"
                  "Please choose a pot of pigment from the shelf.\n"
                  "(Type the name of the pigment you choose.)\n")
            # options.sort()
            start_mixing(options, necessary_ingredients,
                         necessary_ingredients_set,
                         chosen_candidate)
        else:
            print("Sorry. That's all we have on the shelf. ")
            print(f"We won't be able to make {chosen_candidate} from that.")
            go_again()


def start_mixing(options, necessary_ingredients, necessary_ingredients_set,
                 chosen_candidate):

    the_chosen_ones = []
    choosing_error = ""

    while len(the_chosen_ones) < 2:

        # response to error on first or second pigment

        if (choosing_error != ""):
            print("Please try again. "
                  "Choose a pigment from the available pots. ")

        # offering second pigment whether
        # following a correct choice or an error

        if (len(the_chosen_ones) != 0):
            print("Please choose another ingredient from those left.\n")

        # if it's a second pigment choice, or a re-offering for a wrong choice
        # on either the first or second pigment

        if (choosing_error != "") or (len(the_chosen_ones) != 0):
            show_a_counted_list(options)

        # keep the answer as typed so that
        # when printing it back, it is shown exactly as typed

        chosen_pot_as_typed = input()

        # accept the answer, even if the case doesn't match
        chosen_pot = chosen_pot_as_typed.lower()

        if chosen_pot not in options:

            if chosen_pot == '':
                print("I didn't understand.")
            else:
                print(f"\nSorry, there is no '{chosen_pot_as_typed}'"
                      " on the shelf.")

            choosing_error = "error"

        else:

            if chosen_pot not in necessary_ingredients:
                print(f"\nYou poured {chosen_pot} into the vat.")
                print("Sorry, now your ", chosen_candidate,
                      " won't work. Goodbye.")
                break

            elif chosen_pot in the_chosen_ones:
                print(f"You've already got {chosen_pot}.")
                print("We will leave that one on the shelf.")
                choosing_error = "error"

            else:
                the_chosen_ones.append(chosen_pot)
                options.remove(chosen_pot)
                print(f"\nYou poured {chosen_pot} into the vat.")

                the_chosen_set = set(the_chosen_ones)

                if the_chosen_set == necessary_ingredients_set:
                    # you have succeeded
                    print("Yes, you have made ",
                          chosen_candidate, "! Success!")
                    go_again()


def play_game():

    intro()
    invitation_to_play()


play_game()
