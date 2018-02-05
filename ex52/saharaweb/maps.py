class Scene(object):

    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game
central_corridor = Scene("The Desert Sahara", "central_corridor",
"""
You find yourself in the middle of the desert. You don't know how you got there.
The sun is burning on your skin and you are desperate to find water and shadows.

You look south and in the distance, at the very horizon, you see, very vaguely though, an oasis.
You turn around and look north. There seems to be another water point. Shall you walk south or north?
""")

south_oasis = Scene("The Oasis", "south_oasis",
"""
Luckily, you have made the right decision. You reach the oasis just before sunset.
You find the water point, get some water and also find some fruits to eat.

You before it is getting dark, you have to find a place to sleep.
There are some big trees offering space to make yourself comfortable. Do you want to
climb up the tree? You wonder if there might be any snakes hiding.
""")

the_tribe = Scene("The Tribe of Cajun", "the_tribe",
"""
Very well, you made yourself comfortable in one of the trees and sleep straight away.

When you wake up, you find yourself tied to the tree surrounded by some natives you don't understand.
They dance arround you and seem to whisper some incantations.
You can either start to negociate or try to cut the rope with a knife hidden in your trousers.
"""
)

escape_pod = Scene("Escape Pod", "escape_pod",
"""
You decide to cut your robe at night time.
The natives just got to sleep and so you take the chance. You find pods with potions in it.
There's 5 pods, which one do you take?
""")

the_end_winner = Scene("You Made It!", "the_end_winner",
"""
You drink potion number 2. This potion gives you power to fly. You take off and leave the Tribe
and all the memories behind.
You made it!
""")

the_end_loser = Scene("...", "the_end_loser",
"""
This potion kills you.
""")

generic_death = Scene("Death...", "death", "You died.")

# Define the action commands available in each scene
# I added ''(no input) as possible input which makes sure that user stays at the current scene. 
escape_pod.add_paths({
    '2': the_end_winner,
    '': escape_pod,
    '*': the_end_loser
})

the_tribe.add_paths({
    'negociate': generic_death,
    '': the_tribe,
    'cut': escape_pod
})

south_oasis.add_paths({
    'yes': the_tribe,
    '': south_oasis,
    '*': generic_death
})

central_corridor.add_paths({
    '*': generic_death,
    '': central_corridor,
    'south': south_oasis
})

# Make some useful variables to be used in the web application
SCENES = {
    central_corridor.urlname : central_corridor,
    south_oasis.urlname : south_oasis,
    the_tribe.urlname : the_tribe,
    escape_pod.urlname : escape_pod,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    generic_death.urlname : generic_death
}
START = central_corridor
