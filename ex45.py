from sys import exit
from random import randint
import random

class Scene(object):

    def enter(self):
        print "This is a parent scene. Subclass it and implement enter()."
        # value 1 means abnormal termination, not successful
        exit(1)


class SortingHat(Scene):

    def enter(self):
        print "Welcome to Hogwarts School of Witchcraft and Wizardry."
        print "In order to determine the house you belong to"
        print " you are going to wear the Sorting Hat."
        print "-----------Sorting Hat---------------"
        print "Sorting Hat: "'Hmmm difficult, where am I going to put you?'""
        print "Please tell me which one of the following features describes you best:"
        print "brave? decisive? clever? loyal?"

        feature = raw_input("> ")

        if feature == "brave":
            print "Well, if you think you are brave, then you belong to Gryffindor!"
            print "I'll tell you something. Keep in mind the word 'butterbeer'."
            print "\n\n\n"
            return 'gryffindor'

        elif feature == "decisive":
            print "Well, if you think you are decisive, then you belong to Slytherin!"
            print "I'll tell you something. Keep in mind the word 'slughorn'."
            print "\n\n\n"
            return 'slytherin'

        elif feature == "clever":
            print "Well, if you think you are clever, then you belong to Ravenclaw!"
            print "You'll have to prove your intelligence soon."
            print "\n\n\n"
            return 'ravenclaw'

        elif feature == "loyal":
            print "Well, if you think you are loyal, then you belong to Hufflepuff!"
            print "I hope you know the full name of the founder of Hufflepuff."
            print "\n\n\n"
            return 'hufflepuff'

        else:
            print "Sorry, there must have been a mistake. You are a squib."
            print "If you like to stay at Hogwarts, we can offer you an internship with the caretaker Filch."
            exit(1)


class Gryffindor(Scene):

    def enter(self):
        print "Welcome to Gryffindor. You would like to enter the common room."
        print "The Fat lady, the portrait, asks you for the password."

        password = raw_input("> ")

        if password == "butterbeer":
            print "Correct. Please enter."
            return 'quidditch'

        else:
            print "This is wrong. If you cannot remember the password"
            print "you might not be a Gryffindor."
            print "Please go back to the Sorting Hat."
            return 'sorting_hat'


class Slytherin(Scene):

    def enter(self):
        print "Welcome to Slytherin. You would like to enter the common room."
        print "You find yourself deep down in the dungeons. Please enter the password now."

        password = raw_input("> ")

        if password == "slughorn":
            print "Correct. Please enter."
            return 'quidditch'

        else:
            print "This is wrong. If you cannot remember the password"
            print "you might not be a Slytherin."
            print "Please go back to the Sorting Hat."
            return 'sorting_hat'


class Ravenclaw(Scene):

    def enter(self):
        print "Welcome to Ravenclaw. You would like to enter the common room."
        print "What are the names of the Weasley twins?"

        twins = raw_input("> ")

        if twins == "Fred and George":
            print "Correct. Please enter."
            return 'quidditch'

        else:
            print "This is wrong."
            print "You might not be as smart as a Ravenclaw should be."
            print "Please go back to the Sorting Hat."
            return 'sorting_hat'


class Hufflepuff(Scene):

    def enter(self):
        print "Welcome to Hufflepuff. You would like to enter the common room."
        print "As you just have to tap a barrel, you can just enter."
        return 'quidditch'


class Finished(Scene):

    def enter(self):
        print "You won a voucher for free butterbeer in Hogsmeade. Congratulations!"
        return 'finished'


class Quidditch(object):

    def enter(self):
        print "I hope you like your the common room, your house, your new home."
        print "Let's explore Hogwarts. What else can you do? What about sports?"
        print "-----------------------------"
        return 'player'


class Player(object):

    def enter(self):
        print "Let's play some Quidditch."
        print "Please enter a number between 1 and 150."

        your_num = int(raw_input("> "))
        ran_num = random.randint(1,150)

        if your_num > ran_num:
            print "You won!"
            print "That's the result: %r : %r." % (your_num, ran_num)
        else:
            print "You lost!"
            print "That's the result: %r : %r." % (your_num, ran_num)

        exit(0)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()



class Map(object):
    scenes = {
        'sorting_hat': SortingHat(),
        'gryffindor': Gryffindor(),
        'slytherin': Slytherin(),
        'ravenclaw': Ravenclaw(),
        'hufflepuff': Hufflepuff(),
        'quidditch': Quidditch(),
        'finished': Finished(),
        'player': Player()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('sorting_hat')
a_game = Engine(a_map)
a_game.play()
