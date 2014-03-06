class Myself(object):

    def __init__(self):
        self.sleep = 0
        self.food = 0
        self.water = 0
        # want to make dictionary of weapon so it can retrieve what weapon
        # character has, and it's points of strength
        self.weapon = 0 
        self.strength = self.food #self.sleep + self.food + self.water
        self.confidence = self.weapon + self.sleep

class Backpack(object):

    # Keeping 'contents' here instead of in the '__init__' fuction allows
    # it to act like a global variable, instead of each class making 
    # a blank list
    contents = []

    findable_items = {
        'hammer': 1,
        'knife': 2,
        'sword': 3,
        'twinke': 1,
        'beans': 2,
        'jerky': 3,
        'bottle_h20': 1,
        'nalgene_h20': 2,
        'jug_h20': 3
    }

    def __init__(self):
        self.myself = Myself()

    def add_item(self, aquired_item):
        print "Adding %s to your backpack." % aquired_item
        self.contents.append(aquired_item)
        print "You have these things in your backpack:\n", self.contents
        print "can I make it look like this too?" 
        for index, item in enumerate(self.contents):
            print index, item
        
    def eat_drink(self):
        print "Mmm, thirsty or hungy you are? Gooood."
        print "Let's look in your backpack"
        #print self.contents
        for index, item in enumerate(self.contents):
            print index, item

        print "What do you want to consume?"
        consumable = str(raw_input("---> "))
        print "Is what you typed actually in your backpack?"

        print any(consumable.lower() == val.lower() for val in self.contents)
        eat = any(consumable.lower() == val.lower() for val in self.contents)
        if eat == True:
            if consumable in ('twinke', 'beans', 'jerky'):
                category = "food"
                points = Backpack.findable_items.get(consumable)
                self.myself.food = self.myself.food + points

            elif consumable in ('bottle_h20', 'nalgene_h20', 'jug_h20'):
                category = "water"
                points = Backpack.findable_items.get(consumable)
                self.myself.water = self.myself.water + points

            print "That added %d points to %s category." % (points, 
                    category) 
            return 'the_street'

        else:
            print "You don't have that in your backpack."
            choice = raw_input("Try again or back to the Street?\n-->")

            if choice in ("ta", "try again", "Try again"):
                #doesn't work yet!
                Backpack.eat_drink()

            else:
                return 'the_street'









#        def weapon():
#        if consumable in ('hammer', 'knife', 'sword'):
#            category = "weapon"
#            self.myself.weapon = points
#            print "now your weapon =", self.myself.weapon

class Engine(object):
    
    def __init__(self, area_map):
       print "The Engine has recieved %s area_map." % area_map
       self.area_map = area_map

    def survive(self):
        current_area_map = self.area_map.opening_area()
        print "Play first area_map", current_area_map

        while True:
            print "\n_-_-_-_-_-_-_"
            next_area_map_name = current_area_map.enter()
            print "next area_map", next_area_map_name
            current_area_map = self.area_map.next_area(next_area_map_name)
            print "You now wander to", current_area_map


class TheStreet(object):

    def __init__(self):
        self.myself = Myself()
        self.backpack = Backpack()

    def enter(self):
        print """
            The Biters abound and all you're thinking of is surviving.
            You've survived the initial onslaught, and are wandering Boulder.
            What do you want to do?
        """
        print """
             Your sleep is at %d, %d points of food,
             %d points of water, %d points of weapon,
             feeling %d strong, and %d confident.
        """ % (self.myself.sleep, self.myself.food, 
                    self.myself.water, self.myself.weapon,
                    self.myself.strength, self.myself.confidence)

        choice = raw_input("--->")
        print "\n_-_-_-_-_-_-_\n"

        if choice in ("sc", "scavenge"):
            print "Time to look for supplies eh? Good call"
            print "Where do you want to start scavenging?"
            building = raw_input("""That random house, Walgreens, or Vitamin 
                                  Cottage?\n--->""")

            if building in ("rh", "random house"):
                return 'random_house'

            if building in ("w", "Walgreens", "walgreens"):
                return 'walgreens'

            if building in ("vc", "Vitamin Cottage", "vitamin cottage"):
                return 'vitamin_cottage'

        elif choice in ("sl", "sleep"):
            print "sleepy eh?"

            if self.myself.sleep == 0:
                print "You sure need it"
                return 'the_street'

            elif self.myself.sleep > 0:
                print "Really? You're not that sleepy."
                return 'the_street'

            else:
                print "Ok"
                return 'the_street'

        elif choice in ("e", "eat"):
            print "What's in there?", self.backpack.contents
            self.backpack.eat_drink()
            return 'the_street'

        else:
            print """
                What? I can't quite understand you.
                Try to get some sleep, eat, or scavenge.
            """
            return 'the_street'


class RandomHouse(object):

    def enter(self):
        print "I am a house full of random!"
        return 'walgreens'

class Walgreens(object):

    def enter(self):
        print "Now in Walgreens."
        return 'savers'

class Savers(object):

    def enter(self):
        print "Find any awesome clothes here?"
        return 'vitamin_cottage'

class VitaminCottage(object):

    def __init__(self):
        self.myself = Myself()
        self.backpack = Backpack()

    def enter(self):
        print "Here to pick up some food"
        print "What asile do you want to go down?"
        
        asile = raw_input("1, 2, 3, 4, or 5?\n---->")
        # from here i want to randomize what is found in the asile 

        if asile in ("1", "one"): 
            print "You found some jerky!"
            self.backpack.add_item('jerky')
            go = raw_input("Want to explore any other asiles?\ny or n? ")
            if go in ("y", "yes"):
                return 'vitamin_cottage'
            if go in ("n", "no"):
                return 'the_street'

        if asile in ("2", "two"):
            print "Nothin here."
            go = raw_input("Want to explore any other asiles?\ny or n? ")
            if go in ("y", "yes"):
                return 'vitamin_cottage'
            if go in ("n", "no"):
                return 'the_street'

class Chautauqua(object):

    def enter(self):
        print "Where are all the Boulderites hiding?"
        return 'death'

class Death(object):

    def enter(self):
        print "They all died, damn"
        exit(1)

class Maps(object):

    areas = {
        'the_street': TheStreet(),
        'random_house': RandomHouse(),
        'walgreens': Walgreens(),
        'savers': Savers(),
        'vitamin_cottage': VitaminCottage(),
        'chautauqua': Chautauqua(),
        'death': Death()
    }

    def __init__(self, start_area):
        self.start_area = start_area
        print "start_area in __init__", self.start_area

    def next_area(self, area_name):
        print "start_area in next_area()"
        val = Maps.areas.get(area_name)
        print "you got an area", val
        return val
    
    def opening_area(self):
        return self.next_area(self.start_area)

an_area = Maps('the_street')
a_game = Engine(an_area)
a_game.survive()
