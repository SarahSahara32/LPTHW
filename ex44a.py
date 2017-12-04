class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    # empty block, creates class but nothing new to define
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
