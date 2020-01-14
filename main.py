#!/usr/bin/python3
from threading import Timer, Thread
import random
from os import system
from time import sleep
import numpy


class main:
    def run(self):
        self.title_screen()

    # Get input from user with time constraint in seconds
    def timed_input(self, timeout: int, on_timeout_func):
        # If timer runs out on_timeout_func is called
        timer = Timer(timeout, on_timeout_func)
        timer.start()

        # If answer is given timer is stopped
        answer = input()
        timer.cancel()
        return answer

    def input(self):
        answer = input()
        return answer

    # Asks multiplication fact with little time to answer
    def ask_quick_facts(self, num_facts: int):
        self.quick_facts_left = num_facts
        while self.quick_facts_left > 0:
            self.clear_screen()

            x = random.randint(1, 12)
            y = random.randint(1, 12)
            self.print_to_screen("Quick! What is {x} * {y}?".format(x=x, y=y))
            answer = self.timed_input(3.6, self.timout_on_quick_fact)

            if str(answer) == str(x * y):
                self.print_to_screen("Good job!")
                self.quick_facts_left -= 1
            else:
                self.print_to_screen(
                    "{quib} The answer was {answer}".format(
                        quib=self.get_wrong_answer_quib(), answer=(x * y)
                    )
                )
                self.failed_quick_fact()

            sleep(1.2)

        self.clear_screen()

    def failed_quick_fact(self):
        self.quick_facts_left += 2
        self.score -= 14

    def timout_on_quick_fact(self):
        self.print_to_screen(
            "\nTimes up! Sorry. \n Still try to get the right answer though!"
        )
        self.failed_quick_fact()
        return

    def get_wrong_answer_quib(self):
        wrong_answer_quibs = [
            "Darn!",
            "Yikes!",
            "Oops!",
            "Ugh.",
            "What!",
            "Typo?!",
            "Uh oh!",
            "Geez!",
            "Rats!",
        ]

        quib = wrong_answer_quibs[random.randint(0, len(wrong_answer_quibs) - 1)]
        return quib

    def print_to_screen(self, message):
        print(message)

    def title_screen(self):
        self.clear_screen()
        self.print_to_screen(
            "Welcome to this math adventure thing!\nIf you already know what to do"
            " press enter. Otherwise type 1.\n  Also, `exit` is a thing if you "
            "want to be out of here."
        )
        answer = self.input()
        if answer:
            if not "exit" in answer:
                self.intro()
        else:
            self.play()

    def intro(self):
        self.clear_screen()
        self.print_to_screen(
            "The bothersome wizard Jargon has been stealthily stealing parts of homework, "
            "but has been found out by the magical cat Callie. Callie's been working hard "
            "on a lawsuit and now is the time for the fiend to relent! Under court "
            "order he is required to relinquish the stolen work, however the wizard has come "
            "up with an especially devious plan of his own. He has transported the homework here, "
            "but you will have to get through a series of math puzzles to access it! Hurry up "
            "and show this spiteful wizard who's smart! (He severely under payed me for this program)"
        )
        self.wait_for_input()

        self.clear_screen()
        self.print_to_screen(
            "Throughout this journey you will solve various time limited math puzzles. Make sure to "
            "get them right, because you'll have to play the quick multiplication math minigame if "
            "you don't. You get a few seconds to answer each fact and have to do two extra if time runs "
            "out plus another two if you get an answer wrong.\n To finish off this intro you have to "
            "beat a 3 problem game, so Prepare yourself!"
        )
        self.wait_for_input()
        self.score = 1000
        self.ask_quick_facts(3)

        self.print_to_screen(
            "Good job! Make sure to have fun and beat this quick. I really don't like that wizard guy.\n "
            "   ps. you start with a score of 1000 and lose points for every challenge you fail.\n "
            "       If you get zero points you're out. "
        )
        self.wait_for_input()

        self.title_screen()

    def play(self):
        # A list of all the functions for the various math puzzles included
        #  in the game. Just add a function to this list to add it to the game.
        puzzle_functions = [
            self.true_function_door_puzzle,
            self.linear_function_castle_escape_puzzle,
            self.matrices_encoding_split_path_puzzle,
            self.consecutive_number_adding_gateway_tower_puzzle,
        ]
        random.shuffle(puzzle_functions)

        # Starting score. May want to make this higher if more puzzles are added.
        self.score = 1000

        for i, puzzle in enumerate(puzzle_functions):
            self.out_of_time_on_puzzle = None

            if self.score <= 0:
                self.failed_0_score_left()

            # If they get the puzzle wrong than they have to do quick facts and will
            # receive the puzzle again
            if not puzzle():
                if not self.out_of_time_on_puzzle:
                    self.wait_for_input()

                self.ask_quick_facts(i + 1)
                puzzle_functions.append(puzzle)

                self.score -= 100
            else:
                self.wait_for_input()

        self.finished_game()

    def failed_0_score_left(self):
        self.clear_screen()
        self.print_to_screen(
            "I'm sorry, but I've got to kick you out now. "
            "You ran out score and that's what the world runs on. See ya later?"
        )
        self.wait_for_input()
        self.title_screen()

    def finished_game(self):
        # A code to a safe or something like that
        final_passcode = 123456

        self.clear_screen()

        self.print_to_screen(
            "Congrats! You have cleared all the devious puzzles and unlocked the "
            "sought for prize.\nYour score was {score} and the super secret security "
            "key is ...\n {key}".format(score=self.score, key=final_passcode)
        )
        self.wait_for_input()
        self.title_screen()

    def clear_screen(self):
        system("clear")

    def wait_for_input(self):
        self.print_to_screen("\n")
        self.print_to_screen("--Press enter to continue--")
        self.input()

    # There are three doors that get randomly associated
    # with an equation each. Only one of them is a true
    # function. That one is the solution.
    def true_function_door_puzzle(self):
        self.clear_screen()

        function = "-2x / sin(x) + 3"
        equations = ["0.11y⁶ + -41", "x² + 9y² - 8x = -4", function]
        random.shuffle(equations)

        doors = ["spruce", "birch", "oak"]
        self.print_to_screen(
            "There are three doors. One is spruce, one "
            "is birch, and one is oak. Inscribed on the "
            "spruce is '{}', inscribed on the birch is "
            "'{}', and inscribed on the oak is '{}'. "
            "Which door is true and shan't bring death on you?".format(
                equations[0], equations[1], equations[2]
            )
        )
        self.print_to_screen("You have three minutes")
        answer = self.timed_input(60 * 3, self.ran_out_of_time_on_puzzle)
        if self.out_of_time_on_puzzle:
            return False

        self.clear_screen()
        if doors[equations.index(function)] in answer.lower():
            self.print_to_screen(
                "\nAmazing! You managed to not fall into an endless void you "
                "didn't notice until stepping through a door."
            )
            return True
        else:
            self.print_to_screen(
                "\nOops. You fell into an endless void you didn't notice "
                "until stepping through a door."
            )
            return False

    def ran_out_of_time_on_puzzle(self):
        self.out_of_time_on_puzzle = True

        self.clear_screen()
        self.print_to_screen(
            "\n Sadly you ran out of time. \n --Press enter to continue--"
        )

    # You are trapped in a castle and have to come up with
    # the propper linear function to conjure a zipline to escape across the moat.
    def linear_function_castle_escape_puzzle(self):
        self.clear_screen()

        self.print_to_screen(
            "You are at a window in a rival wizard's castle and have "
            "to conjure a rope to escape. Unfortunately there is a huge moat, so "
            "you will have to make a floating zipline."
        )
        x = random.randint(30, 300)
        y = random.randint(20, 100)
        self.print_to_screen(
            "You are {y} meters in the air and the moat is {x} meters wide.\nConsidering "
            "that the moat is to your left what slope can be used to make a rope "
            "connecting to the edge of the moat.".format(x=x, y=y)
        )
        self.print_to_screen(
            "Your enemy's minions are closing in, so you only have a minute or two to escape"
        )
        answer = self.timed_input(80, self.ran_out_of_time_on_puzzle)
        if self.out_of_time_on_puzzle:
            self.clear_screen()
            self.print_to_screen(
                "Fool! The minions are upon you now. There is no telling what could happen next."
            )
            return False

        if len(answer.split("/")) > 1:
            a_y, a_x = answer.split("/", maxsplit=1)
        else:
            a_y = answer
            a_x = 1
        if str(y / x).startswith(str(float(a_y) / float(a_x))[:4]):
            self.clear_screen()
            self.print_to_screen("Huzzah! You're speeding away to freedom")
            return True
        else:
            self.clear_screen()
            self.print_to_screen(
                "You may want to go back to math class if you survive this. "
                "Remember slopes are in the form rise/run"
            )
            return False

    # You have to decode the message in a 3x3 matrix
    def matrices_encoding_split_path_puzzle(self):
        self.clear_screen()

        encoding_matrix = self.generate_matrix(3, 3, [0, 20])

        message = "deathtrap"
        # 'deathtrap' with letters switched (ie a=z, b=y) and made into numbers (ie a=1, b=2)
        message_matrix = numpy.matrix([[23, 22, 26], [7, 19, 7], [9, 26, 11]])

        encoded_matrix = encoding_matrix * message_matrix

        self.print_to_screen(
            "You have run into a split in the passage you are following "
            "and have to figure out which way to go. There are a couple sets "
            "of markings on the floor and a strange picture above each doorway.\n"
            "On the floor the first set of markings says 'The way forwards is "
            "backwards'. That last word could also translate to 'reversed'. \n"
            "The second set of markings says 'The right way to go is guided by the left'."
        )
        self.print_to_screen(
            "Above the left doorway is carved: \n " + str(encoding_matrix)[1:-1]
        )
        self.print_to_screen(
            "\n Above the right doorway is carved: \n " + str(encoded_matrix)[1:-1]
        )
        self.print_to_screen(
            "\n What message is this puzzle communicating?\n"
            "You have limited suplies, so you will have to randomly choose a "
            "passageway if you don't figure this out in eight minutes."
        )

        answer = self.timed_input(8 * 60, self.ran_out_of_time_on_puzzle)
        if self.out_of_time_on_puzzle:
            self.clear_screen()
            self.print_to_screen(
                "You ran out of time and choose one of the passages at random. "
                "I haven't heard from you since."
            )
            return False

        if answer.lower().strip() == message:
            self.clear_screen()
            self.print_to_screen(
                "That was a close one. I doubt you want to know what is down deathtrap row"
            )
            return True
        else:
            self.clear_screen()
            self.print_to_screen(
                "That doesn't seem quite Right. Better luck next time! "
                "Have fun with Multiplication facts after this."
            )
            return False

    def generate_matrix(self, num_rows: int, num_columns: int, num_range: list):
        rows = []
        for row in range(num_rows):
            rows.append([])
            for column in range(num_columns):
                num = random.randint(num_range[0], num_range[1])
                rows[row].append(num)

        matrix = numpy.matrix(rows)
        return matrix

    def consecutive_number_adding_gateway_tower_puzzle(self):
        self.clear_screen()

        num_portals = random.randrange(1000, 10000001, step=10)
        self.print_to_screen(
            "You are at the bottom of a spiralling staircase looking up and imagining the "
            "practically infinite levels of portals to increasingly higher realities above "
            "you. In reality there are only {x} portals with each one's dimension coming up "
            "the staircase able to hold more worlds. The first holds 1, the second 2, the "
            "third 3, ect. How many worlds can be accessed at any moment from this one "
            "gateway tower?".format(x=num_portals)
        )
        self.print_to_screen(
            "You have an appointment with a dying hydra, so you'll have to "
            "finish this within the next ten minutes"
        )
        answer = self.timed_input(60 * 10, self.ran_out_of_time_on_puzzle)
        if self.out_of_time_on_puzzle:
            self.clear_screen()
            self.print_to_screen(
                "Guess you'll have to chew on that some more later. "
                "You do NOT want to keep a hydra waiting."
            )
            return False

        num_worlds = (num_portals * (num_portals + 1)) // 2
        if answer.startswith(str(num_worlds)[:4]):
            self.clear_screen()
            self.print_to_screen(
                "That's pretty crazy. What's more crazy though is how many "
                "stairs you are about to walk up"
            )
            return True
        else:
            self.clear_screen()
            self.print_to_screen("Nah. that answer just doesn't add up.")
            return False


main = main()
main.run()
