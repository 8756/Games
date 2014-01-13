overall_health = 0
bf = "blank"
almuerzo = "blank"
wo = "blank"


def evening_fun():
    
    global overall_health
    print """
        You've made it nearly to the end of the day! 
        Let's see, your choices of what to do with your evening
        depend on your overall health score of %d 
        """ % overall_health
            
    if overall_health == 6:
        print """
            Congrats! You made the optimal choices.
            You get to:
            -- talk to that cute girl or guy at the gym
            -- eat out at a nice restaurant
            -- both!
            """
        evening = raw_input("cutie, restaurant, or both\n---> ")
                
    elif overall_health == 5:
        print """
            You get to:
            -- talk to that cute girl or guy over there
            -- eat out at a nice restaurant
            """
        evening = raw_input("cutie or restaurant\n---> ")
            
    else:
        print """
            You made it through the day, but your choices
            have just gotten you to the end of the day
            without feeling destroyed. Congratulations?
            You should just try this day again :D
            """
        start()
            
    if evening == "cutie":
        print """
            You go over and talk to that interesting person 
            and grab some digits.  Strong work! You can
            put a \'W\' down for the day.
            
                THE END
            """
        exit(0)
        
    elif evening == "restaurant":
        print """
            Not every evening has to be social.  You
            enjoy a tasty meal at a nice restaurant, 
            and hit the sack ready to tackle tomorrow.
            Well done!"
            
                THE END
            """
        exit(0)
            
    elif evening == "both":
        print """
            Woah! You go for all the things! The cute person
            accepts your dinner invitation, and you enjoy a
            great meal and each other's company.  After parting
            ways, you go to bed happy and healthy, ready and 
            motivated to kick some ass tomorrow!
            
                YOU WIN BIG TIME!
            """
        exit(0)
            
    else:
        print "Huh? Didn't get that, try again."
        evening_fun()           
            
            
def fitness():
    print """
    The whistle blows and you're out of work.  Your food choices 
    affect what you're able to do after work on YOUR time.
    What do you have the energy to do?
    """

    def workout():
        
        global overall_health
        if 4 >= overall_health >= 2:
            print """
            So what do you after work? Want to go workout at the
            gym, hit a coffee shop and read a book, or are you
            too tired to do either, and will you just go home and 
            bake a pizza and watch a movie?
            """
            global wo
            wo = raw_input("gym, book, or pizza?\n---> ")
            
        elif 1 >= overall_health >= 0:
            print """
            So what do you after work? Hit a coffee shop and 
            read a book, or are you too tired to do either, 
            and will you just go home and bake a pizza 
            and watch a movie? Choose carefullly...
            """ 
            wo = raw_input("book or pizza?\n---> ")
            
        else:
            print "ERROR, SHOULDN'T DO THIS, FIX workout() BUG"

        if wo == "gym":
            print """
            Nice! Since you had the energy, you hit the gym and 
            got a good workout in.  Your body loves it, and your
            head is cleared.
            """
            overall_health = overall_health + 2
            wo = "hit the gym"
            
        elif wo == "book":
            print """
            You need a bit of a break, and feeding your mind isn't a bad
            idea. 
            """
            overall_health = overall_health + 1
            wo = "hit a coffee shop and read a book"
            
        elif wo == "pizza":
            print """
                You're crushed from work and need food and a rest.
                You eat the whole pizza, make it through most of
                the movie, and then those carbs let you crash!
                Gain 5lbs to your ass.
                """
            overall_health = overall_health + 0
            wo = "went home, baked a pizza, and watched a movie"

        else:
            print "You did it wrong. Type in just: gym, book,\n"\
            "or pizza please. Try again!"
            workout()      
# I somehow crashed the program after mis-typing it in a few times here, and got line error 143 over till it 'maximum recursion depth exceeded in cmp", also it didn't like like 113 either

        print "So far, with your day, you: \nhad %s for breakfast,"\
            "\nate %s for lunch, \nand %s after work." % (bf, almuerzo, wo)

        if overall_health >= 3:
            print "You've chosen well enough so far, what can and will "\
                "you do with your evening?"
            evening_fun()
                
        else:
            print """
                Damn. Hate to tell you this, but you kinda failed. 
                Your overall health score was only %d point/s out of a 
                possible 6 points. You should make better choices
                on your next round! Unless you want to quit.
                
                Would you like to start a new day?
                """ % overall_health
                
            choice = raw_input("yes or no?\n---> ")
            
            if choice == "yes":
                overall_health = 0
                start()
                
            elif choice == "no":
                print "\n\ninsert(sad face)\n\n\t\tThe End\n\n"
                exit(0)

            else:
                print "You failed to type yes or no. \n sigh\n Try your "\
                    "day again!"
                start()

    
    global overall_health
    if overall_health == 4:
        print "You're feeling energized from making\n good food choices "\
            "during the day."
        
    elif 3 >= overall_health > 1:
        print "You're feeling a bit tired after work,\n but "\
            "ready for some action."
        
    elif 1 >= overall_health >= 0:
        print "Your food choices sucked, you're so tired."    
    
    else:
        print "ERROR, SHOULDN'T DO THIS, FIX fitness() BUG"

    workout()
    
    
def food():

    def recap():
        print "Let's recap. So far your overall health\n "\
                "rating is %d. That's because you had %s\n "\
                "for breakfast and %s for lunch." \
                % (overall_health, bf, almuerzo)
            
        oh = int(overall_health)
        if oh > 4:
            print "ERROR You sure are eating a lot. \nHow did you eat so"\
                "many meals? I must have written this wrong."
                
        elif oh == 4:
            print "You're doing it right so far."
            
        elif 3 >= oh > 0:
            print "Be careful of your choices now."
            
        else:
            print "Damn, rough day huh? Bad choices :("

        fitness()
        
    def lunch():  
        
        print """
        Time for lunch!  What'll you have? A big-ass 
        salad and chicken, burger and fries, or no time
        for lunch and simply a bar?
        """
        
        global almuerzo
        almuerzo = raw_input("salad, burger, or bar?\n--->")
        
        if almuerzo == "salad":
            print """
            Good choice! The protein and greens fuel
            you to be productive to the end of work.
            """
            global overall_health
            overall_health = overall_health + 2
            almuerzo = "a big-ass salad"
           
        elif almuerzo == "burger":
            print """
            Well done with getting some protein, but all
            those carbs have you crashing by 4pm.
            """
            overall_health = overall_health + 1
            almuerzo = "a burger and fries"
            
        elif almuerzo == "bar":
            print """
            Dang, you work too hard! No fuel means
            you're feeling the hurt and are 
            quite unproductive.
            """
            overall_health = overall_health + 0
            almuerzo = "just a bar"
            
        else:
            print "You did it wrong. Type in just: salad, burger,\n"\
            "or bar please. Try again!"
            lunch()

        recap()
    
    def breakfast():
       
        print """
        The food we buy and its quality influence our
        health and our planet's health. What do you
        choose for breakfast? Kale and eggs, 
        a bowl of cereal, or simply a cup coffee?
        """
        
        global bf
        bf = raw_input("kale, cereal, or coffee?\n---> ")
        
        if bf == "kale":
            print "No drugs or carbs for you! \nYour long burning energy "\
                "sees you through easily to lunch."
            global overall_health
            overall_health = overall_health + 2
            bf = "kale and eggs"
            
        elif bf == "cereal":
            print "At least you had time to eat something, "\
                "\nbut those carbs let you down before lunch. You're hungy."
            overall_health = overall_health + 1
            bf = "a bowl of cereal"
            
        elif bf == "coffee":
            print "No time for breakfast? \nYou're now famished by 10am"
            overall_health = overall_health + 0
            bf = "just a cup of coffee"
            
        else:
            print "You did it wrong. Type in just: kale, cereal,\n"\
            "or coffee please. Try again!"
            breakfast()
        
        lunch()
   
    print "How about we start with breakfast?"
    breakfast()


def start():
    
    print """
    We have many choices that affect ourselves, 
    the people around us, and our space vesssel.
    Let's see what choices you make on a regular basis,
    and what kind of earth you make for yourself.
    Let's start at the beginning with your morning
    food selection.
    """
    
    food()

start()




