from sys import exit

def day():
    print "Alright, I hope you are ready to start the day."
    print "You have two options. Either you can go to the zoo or you can stay at home."
    print "What would you like to do?"

    choice = raw_input("> ")

    if choice == "zoo":
        print "Excellent. Let's go and see some animals."
        zoo()
    elif choice == "home":
        print "Wow, you are really lazy today. I'll ask you again."
        day()
    else:
        dead("Sorry, but I can't do that with you today.")


def zoo():
    print "Welcome to Hagenbecks Tierpark."
    print "Would you like to to see the animal park or the tropical aquarium?"

    choice = raw_input("> ")
    if choice == "animal park":
        print "Oh, I can't wait to explore the park."
        park()
    elif choice == "tropical aquarium":
        print "Cool, I am looking forward to seeing the flora and fauna of the equatorial regions."
        aquarium ()
    elif choice == "both":
        print "I knew you would like to see both."
        print "In order to decide where to start, type 1 or 2."
        choice = raw_input("> ")
        if choice == "1":
            print "Let's see the animal park."
            park()
        else:
            print "Let's see the tropical aquarium."
            aquarium()
    else:
        print "Sorry, I'll repeat in case you did not understand."
        zoo()


def park():
    print "Oh wow, through the park we have seen amazing animals."
    print "Just to name a few, we have already seen flamingos, monkeys, elephants and giraffes."
    print "Now, we are walking directly to the tigers."
    print "Oh no, a little boy just fell from the wall directly into the tiger's enclosure."
    print "Are you jumping after the boy? Or call for help? What are you going to do?"

    choice = raw_input("> ")

    if "jump" in choice:
        dead("Heroic choice but you won't save the boy. You both got killed by the tiger.")
    elif "call" in choice:
        print "Thanks for calling. Because of you, we could save the boy. Bless you!"
        print "We like to invite you to visit the tropical aquarium as well."
        aquarium()
    else:
        dead("Oh gosh, you've just woke up. What a nightmare. Please go back to sleep.")


def aquarium():
    print "Now, let's see the tropical aquarium."
    print "You open the first door and you see a bunch of ring-tailed lemurs."
    print "Oh my god, they are so cute. You like to pet them."
    print "You read the sign 'Please do not touch!'"
    print "What are you going to do? Touch or not touch?"

    choice = raw_input("> ")

    if choice == "touch":
        dead("Can't you read? You got kicked out of the zoo as you don't respect the rules.")
    elif choice == "not touch":
        print "Thanks for being so respectful. Have a lovely day in our tropical aquarium."
        exit(0)
    else:
        print "Sorry, that is not an option. We'll enter again."
        aquarium()


def dead(why):
    print why, "Goodbye!"
    exit(0)


def start():
    print "Please type in your name."
    name = raw_input("> ")
    print "Good morning %s!" % name
    print "What would you like for breakfast? Coffee or tea?"

    choice = raw_input("> ")

    if choice == "coffee":
        print "Great choice. I'll get you a lovely Brazilian coffee."
        day ()
    elif choice == "tea":
        print "No problem, I'll get you the best English tea we can offer."
        day ()
    else:
        dead("Sorry, but we don't have %s." % choice)


start()
