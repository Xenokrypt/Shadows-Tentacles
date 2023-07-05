#============================================================== Python Game ==============================================================
# with open("health.py") as f:
#     exec(f.read())

from time import sleep as s
import random

# Creating an empty list for the health bar
health_bar = []

player_health = 80

#------------------------------ Recallable health system ------------------------------

# Creating a function to decide what the health bar will look like at any moment when called
def health():
    global health_bar
    if player_health == 100:
        health_bar = ["♥","♥","♥","♥","♥","♥","♥","♥","♥","♥"]
    elif player_health ==90:
        health_bar = ["♥","♥","♥","♥","♥","♥","♥","♥","♥","♡"]
    elif player_health ==80:
        health_bar = ["♥","♥","♥","♥","♥","♥","♥","♥","♡","♡"]
    elif player_health ==70:
        health_bar = ["♥","♥","♥","♥","♥","♥","♥","♡","♡","♡",]
    elif player_health ==60:
        health_bar = ["♥","♥","♥","♥","♥","♥","♡","♡","♡","♡"]
    elif player_health ==50:
        health_bar = ["♥","♥","♥","♥","♥","♡","♡","♡","♡","♡"]
    elif player_health ==40:
        health_bar = ["♥","♥","♥","♥","♡","♡","♡","♡","♡","♡"]
    elif player_health ==30:
        health_bar = ["♥","♥","♥","♡","♡","♡","♡","♡","♡","♡"]
    elif player_health ==20:
        health_bar = ["♥","♥","♡","♡","♡","♡","♡","♡","♡","♡"]
    elif player_health ==10:
        health_bar = ["♥","♡","♡","♡","♡","♡","♡","♡","♡","♡"]
    else:
        health_bar = ["♡","♡","♡","♡","♡","♡","♡","♡","♡","♡"]
        print("\n")
        print("YOU DIED")
        print("""\n
              
                  *              )               (     
 (        (      (  `          ( /(               )\ )  
 )\ )     )\     )\))(   (     )\()) (   (   (   (()/(  
(()/(  ((((_)(  ((_)()\  )\   ((_)\  )\  )\  )\   /(_)) 
 /(_))_ )\ _ )\ (_()((_)((_)    ((_)((_)((_)((_) (_))   
(_)) __|(_)_\(_)|  \/  || __|  / _ \\\\ \ / / | __|| _ \  
  | (_ | / _ \  | |\/| || _|  | (_) |\ V /  | _| |   /  
   \___|/_/ \_\ |_|  |_||___|  \___/  \_/   |___||_|_\  
                                                        
        
              \n""")
        menu()

#------------------------------ The main function the holds most of the game story ------------------------------

# Creating the, damage and coin system
numbers = [10, 20, 30]
damage = random.choice(numbers)

global coins
coins = 100



# Main game function
def game():
    global x
    print("\nYou are flying over an ocean, heading towards an unknown island. \nSuddenly, a storm englufs the plane, causing it to crash on the island. \nYou, the sole survior, emerge from the wreckage, unfazed and determinded to survive!")
    s(5)
    # Calcuting how much health the user has and dispalying it 
    global player_health
    player_health = 80
    health()
    print("\n", player_health, " HP ", " ".join(health_bar))
    s(1.5)
    print("\nYou now are in a weaker condition")
    s(2)
    global player_name
    # Asking user for name
    player_name = input("\nYou walk around confused, remembering that your name is: ").capitalize()

    s(1)
    print("\nAs you venture deeper into the dense forest, you stumble upon a graceful elf, \nstanding beneath a towering oak tree.")

#------------------------------ Use triple " in order to create mulitple lines of print ------------------------------

     # Elf Ascii image
    s(7)
    print("""
            _.----._     _.---.
         .-'        `-.-'      `.
       .'                 .:''':.`.
     .'        .:'''':. .' .----.  `.
 .-./        .' .----.    /  .-. \   `.
/.-.           /  .-. \   \ ' O ' |    \\
||        `.   | ' O '/    \ `-' /     |
|| (        \   \ `-'/      `-.__     / `.
 \`-'        )   .-'  --         )        `.
  `-'     _.'   (            _.-'    _/\    \\
     `.       /\_ `-.____..-'     .-' _/    /
       `.     \_ `-._         _.-'_.-'   .'
         `--.._ `-._ `-.__..-'_.-'     .'
       .-'     `-._ `--.__..-'  _.----'`.
      /            `---.......-' _     \ \\
     /                          ( `-._.-` )
    /  /     _                  .-    _.-'
   (  `-._.-' )                (_   .'    \\
    `-._      -.               (_.-'       |
        `.     _)                   __..---'
       |  `-._) ''...__ .-. __...'''__..---'
        \      '''...__((=))__...'''      /
         |              `-'             .'
         \                             /
          |                           |
          \     \    \      /    /   /
           `. \               /     /
             `.    \   \   /   /   /
               `--.._   ` '  _.--'
                      [====]
                       )  (
                    .-'    '-.
                   |          |
                   | .------. |
                   | |      | |
                   | '------' |
                   |          | 
                   '----------'""")
    
    # Elf interaction
    s(1)
    print(player_name,": \"Excuse me, noble elf. I seek your guidance.”\n")
    s(2.5)
    print("The elf turns with a serene expression\n")
    s(2.5)
    print("Elf: \"Greetings, weary traveller. What brings you to these enchanted woods?”\n")
    s(3)
    print(player_name,": I'm mashed up and stranded on this mysterious island. Can you help me, can you shed light on this quest?”\n")
    s(5)
    print("Elf: “Ah, the Gemstone of legend. It holds the power to open the path that binds you to this realm. But before I reveal its secrets, \nI must test your wits. Answer me this riddle, and I shall impart upon you the knowledge you seek.”\n")
    s(14)
    print(player_name,": I am ready. Pose your riddle, wise elf.")
    s(2.5)
    print("\nWith a mischieveous glint in their eyes, the elf asks:")
    s(3)
    # Asking the user to complete a riddle, which will lead to different paths
    print("\n\"I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?”\n")
    s(7)
    riddle_one = input("You pause, pondering the riddle, then believe the answer is: ").lower()
    # If the riddle is correct then restore health and move on
    if riddle_one == "echo" or riddle_one == "echos":
        player_health = 100
        s(2)
        print("\nThe Elf nods approvingly.")
        s(3)
        print("\nElf: \"Correct traveller! Your answer rings true like the melody of the forest. Your health shall be restored, \nand the path to the Gemstone awaits you. May fortune favor your journey.”\n")
        s(10)
        health()
        print(player_health, " HP ", " ".join(health_bar), "\n")
        s(1.5)
        print(player_name, ": \"Thank you, noble elf, for your guidance and the restoration of my health. \nI shall continue my quest and find the Gemstone. Farewell.”\n")
        s(8)
        print("Elf: Farewell, brave adventurer. May the whispers of the wind guide your steps and lead you to your destiny.\n")
        s(7)
        print("""
                      [====]
                       )  (
                    .-'    '-.
                   |          |
                   | .------. |
                   | |      | |
                   | '------' |
                   |          | 
                   '----------'""")
    # If the riddle is incorrect then no health is restored
    else:
        s(2)
        print("\nThe Elf shakes his head gently. \n\nElf: I'm afraid that is not the correct answer, brave traveller. Your health remains unchanged, \nbut fear not, for the path to the Gemstone still awaits you. May luck be on your side as you venture forth.\"\n")
        s(10)
        print(player_name,": \"Thank you for your guidance, noble elf. I shall continue my journey, undeterred by this setback. Farewell.\"")
        s(7)
        print("\nElf: \"Farewell, courageous adventurer. May the shadows of the forest shield you from harm as you pursue your destiny.\"")
        s(6)
        print("""
                      [====]
                       )  (
                    .-'    '-.
                   |          |
                   | .------. |
                   | |      | |
                   | '------' |
                   |          | 
                   '----------'""")
    s(1.5)
    # Troll Interaction
    print("\nYou walk down a path and encounter a bridge. You are faced with an ugly troll, Grumbletooth. \n")
    s(5)
    # Troll ASCII art
    print("""
                .-““““.  
               /       \\
           __ /   .-.  .\\
          /  `\  /   \/  \\
          |  _ \/   .==.==.
          | (   \  /____\__\\
           \ \      (_()(_()
            \ \            '---._
             \                   \_
          /\ |`       (__)________/
         /  \|     /\___/
        |    \     \||VV
            |     \     \|““““,
        |      \     ______)
        \       \  /`
                 \(
    \n""")
    print("And yet again another riddle was stumbled upon you.")
    s(1.5)
    # Asking the player another riddle
    riddle_two = input("\nTroll: \"I can fly without wings, cry without eyes. Wherever I go, darkness follows me. What am I?\": ").lower()
    # Like before the troll asks a riddle , if you get it right you get hp, but this time if you get it wrong you take damage
    if riddle_two == "cloud" or riddle_two == "clouds":
        s(2)
        print("\nTroll: \"Correct! You are a cloud!\"")
        player_health = 100
        health()
        print(player_health, " HP ", " ".join(health_bar), "\n")
        s(1.5)
        print("\nGrumbletooth's surprise turned to amusement as he granted passage, leaving behind a trail of laughter and newfound respect for the clever wanderer. \nHe lets you pass through the bridge and you stumble between 2 paths.")
    else:
        s(2)
        print("""  
                .-““““.
               /       \\
           __ /   .-.  .\\
          /  `\  /   \/  \\
          |  _ \/   .__.__.
          | (   \  /____\__\\
           \ \      (_()(_()
            \ \            '---._
             \               .    \_
          /\ |`       (__)________/
         /  \|      ___/
        |    \     /||VV
        |     \    \|\|““““,
        |      \     ______)
        \       \  /`
                 \( 

        \n""")
        print("\nTroll: \"Incorrect!\"")
        s(1.5)
        player_health = player_health - damage
        health()
        print("\nGrumbetooth looks at you in disgust and rage, and starts running towards you with his wooden club. \nYour player fails to dodge the attack as the troll swings at you. \n")
        s(6)
        print("He hits you straight in your head and you lose () HP. \nAfter the attack, the troll is holding his weapon down the side of his leg, which leaves him open to attack. \n\nYou stab him through his neck, immediately killing him!")
        
    print("\n")
    s(1.5)
    print("After the encounter, you pass through the bridge and encounter 2 paths.\n")
    s(2)
    print("On the left, there is a dark mysterious cave, on the right there is a muddy path.")
    print("You walk forward, stumbling and falling, but continue onward.\n")
    s(6)

#------------------------------------- BAT BATTLE -------------------------------------

    # This fucntion contain the bat battle
    def fighting():
        if x == 2:
            s(1.5)
            print("\n")
            print("You stand up against the giant bat, draw your axe, and strikes the bat with a mighty blow, slicing it in half.\n")
            s(5)
            print("You kill the giant bat and searches its remains.\n")
            s(3)
            print("You then see a key hanging underneath one of the bat's wings, annd take it.\n")
            s(3)
            print("Around a dark corner, there's what appears to be a hidden treasure chest.\n")
            s(4)
            print("Intruged, you open the chest, finding 100 shining gold coins inside.\n")
            # Giving player 100 coins if they defeat the bat
            s(1.5)
            global coins
            coins = 100
            print("You have", coins, "coins\n")
        else:
            # Causing the player to lose damage (if they dont have the axe)
            print("\n")
            print("The bat was too strong, you take some damage, so you head back to the pathway\n")
            global player_health
            player_health = player_health - damage
            health()
            print(player_health, " HP ", " ".join(health_bar), "\n")
            muddy_path()

#------------------------------------- BAT ENCOUNTER -------------------------------------

    #Bat interation
    def bat():
        print ("You enter the dark cave, looking for a way to safety.\n")
        s(2)
        print("The cave is eerily quiet, heightening the tension in the air.\n")
        s(3)
        print("Suddenly, a giant object falls from the ceiling right in front of you.\n")
        s(3)

        print("""
     _________________               _________________
      ~-.              \  |\___/|  /              .-~
          ~-.           \ / o o \ /           .-~
             >            \\  W  //           <
            /             /~---~\             \\
           /_            |       |            _\\
              ~-.        |       |        .-~
                 ;        \     /        i
                /___      /\   /\      ___\\
                     ~-. /  \_/  \ .-~
                        V         V """)
                
        s(1)
        print("\n")
        print("It is a giant bat with its wings wide open, blocking the passage forward\n")
        s(1)

        # Conversation with the giant bat
        print(player_name, "(shivering voice): “Who are you?”\n")
        s(1)
        print(player_name, "“I mean no harm, please don't harm me.”\n")
        s(2)
        print("Giant bat: “I am Nocturuns, the guardian of this sacred cave for centuries.”\n")
        s(3)
        print("Giant bat: “What brings you to this desolate place, human?”\n")
        s(3)
        print(player_name, "“I was in the plane that crashed near your cave, Nocturuns. Have you not heard the bang?”\n")
        s(5)
        print("Giant bat: “I hear everything, human.”\n")
        s(2)
        print(player_name, "“Please don't hurt me. I just need to find a way to safety through your cave.”\n")
        s(4)
        print("Giant bat: “You shall not pass. Your existence in this cave disturbs the souls of my ancestors.”\n")
        s(4)
        print("Giant bat: “Now I have to sacrifice you for the peace of those resting souls.”\n")
        s(3)

        # Fight with the giant bat

        d = True
        while d == True:
            fight = input("Do you flee or fight? ")
            #If they flee they go back to the the muddy path but take damamge
            if fight == "flee":
                s(1.5)
                print("You turns around and run in a dark path, hurting himself in the process.\n")
                s(2)
                print("He stumbles and falls, hitting sharp rocks.\n")
                s(2)
                print("As he gets himself back up the axe vanishes into thin air.\n")
                s(3)
                print("The giant bat hovers over the you, slapping him with its giant wings, inflicting considerable damage.\n")
                s(4)
                print("You finally escape the cave, hurt and tired, stumbling back to the muddy path with damaged HP.\n")
                s(4)
                global player_health
                player_health = player_health - damage
                health()
                print(player_health, " HP ", " ".join(health_bar), "\n")
                print("You then turn around and return back to the 2 paths.\n")
                muddy_path()
                return
            # If the player chooses fight , it will call the fighting function
            elif fight == "fight":
                fighting()
                return
            else:
                print("Invalid option!")
                d = False

#------------------------------------- MUDDY PATH -------------------------------------

    # muddy path function
    def muddy_path():
        global x
        x = 0
        # Asks which path the user likes to take, and will continuie to loop the question until a valid answer is given
        while x == 0:
            print("\n")
            path_choice = input("Which path do you take? (Left or Right) ").lower()
            if path_choice == "left":
                x = 1
                print("\n")
                print("You chose the dark cave!\n")
                bat()
                s(1)
            elif path_choice == "right":
                # If the player chose the muddy path , this sets x to 2, which checks in fighting function for the axe
                x = 2
                # Muddy path narration
                print("\nYou chose the muddy path!\n")
                s(1)
                print("As the heavy rain pours from the ominous dark clouds above, you trudge down a treacherous, muddy path.\n")
                s(5)

                print("Every step you seem to sink deeper into the murky earth, making progress an arduous task.\n")
                s(4)

                print("With a cloak tightly wrapped around your frame and a weathered hat shielding your face from the relentless downpour, you press on.\n")
                s(6)

                print("As you venture deeper into the mystical forest, you come across a massive tree, its gnarled trunk seemingly embracing a gleaming, \nancient axe buried within its woody grasp.\n")
                s(8)

                print("Intrigued, you approach cautiously, reaching out to touch the hilt of the weapon.\n")
                s(3)

                print("As your fingers make contact, a surge of power courses through you, and a voice echoes in your mind, revealing the axe's forgotten tale.\n")
                s(5)

                print("+ ENCHANTED AXE\n")

                print("""
 .------------------._______________________:__________j
/                   |                      |           |`-.,_
\###################|######################|###########|,-'`
 `------------------'                       :    ___   l
                                            /   (   )   \\
                                           /     `-'     \\
                                         ,'               `.
                                      .d8b.               .d8b.
                                      "Y8888p..       ,.d8888P"
                                        "Y88888888888888888P"
                                           ""YY8888888PP""

                """)

                print("With a sense of awe and anticipation, you realize that this enchanted relic will become an invaluable ally in your upcoming battles.\n")
                s(5)

                print("You headed back to the cave.\n")
                s(1)

                bat()
        
            else:
                print("Invalid option")
                s(1)
                muddy_path()

    muddy_path()

    # Another small elf interation
    s(1)
    print("After the you killed the giant bat, an elf suddenly appears from behind the rocks, where he was watching the whole encounter.\n")
    s(5)
    print("The elf offers the lantern to get through the dark cave.\n")
    s(2)

    # Bandits interaction
    print("You finally stumbles his way out of the dark cave, breathing a sigh of relief.\n")
    s(3)
    print("But his relief is short-lived as he is surrounded by six bandits, demanding him to surrender the gold.\n")

#------------------------------------- BANDITS ENCOUNTER (NOT IN ITS OWN FUNCTION) -------------------------------------

    y= 0
    while y == 0:
        global coins
        robbery = input("Do you fight or flee the bandits? ")
        # Fighting or flee loop/interaction
        if robbery == "flee":
            y = 1
            print("\n")
            print("You are brave enough to engagage with the bandits. You end up feeling outnumbered by the bandits as they surround you completely \nfrom all sides. The leader of the bandits, Grimlee, stands right looking into your eyes menanicinly\n")
            s(7)
            print("Grimlee: “Looks like you have come down the wrong path human! Why should I not oblierate you right now with my bandits?\n")
            s(5)
            print("You are frighetned and has decided to flee. You spot a little gap between the line of bandits and you rush through the tight gap.\n")
            s(8)
            print("You successfully get through to the other side of the path but you were shot up with arrows from the bandits as you ran through them. \n\nYou have lost health.\n")
            s(7)
            player_health = player_health - damage
            health()
            print(player_health, " HP ", " ".join(health_bar), "\n")
        elif robbery == "fight":
            y = 1
            b = [1, 2]
            bandits = random.choice(b)

            # If the player fights, choose a random output, either win with no consequences, or just make it out but without any coins
            if bandits == 1:
                print("\n")
                print("You are brave enough to engage with the bandits. With swift strikes and unmatched skill, you defeat them one by one. \nTheir leader, Grimlee tried to escape but was captured. He pathetically lies there, weak and panting\n")
                s(10)
                print(player_name, ": “Your minions were merely child's play! Look around you, what is left?”\n")
                s(6)
                print("Grimlee: “There were 6 of us and only one of you! How did we succumb to such fate?”\n")
                s(5)
                print(player_name, ": “You failed to consider how powerful I am. This is the end of the road for you Grimlee and your dirty bandits!”\n")
                s(6)
                print("You throw Grimlee onto the floor and reaches down with his axe, chopping off his head. \nHis head rolls down the road, while you watch it flow down the gritty path.\n")
            else:
                print("\n")
                print("You are brave enough to engage with the bandits. You end up feeling outnumbered by the bandits as they surround you completely from all sides. \n\nThe leader of the bandits, Grimlee, orders his bandits to hold fire. Grimlee looks into your eyes angrily, \n\nWhat brings you to these treacherous mountains? I should have your head ripped off!\n")
                s(15)
                print(player_name, ": “I ask for your mercy Grimlee. I don't want any trouble. I am on a quest to find the mystical gemstone on Mount Everest.”\n")
                s(7)
                print("Grimlee: “And you thought you could merely show up on my path? No one is allowed through here, \nno one! Why should we spare you human?” **pulls sword out of sheath.\n")
                s(8)
                print(player_name, ": “I didn't come for trouble, I really didn't! Please Grimlee, stop this madness, you will not gain anything by killing me.”\n")
                s(7)
                print("Grimlee: “I suppose so... **returns sword into sheath**. The village will know that you came by this \npath and they will know I didn't kill you. I refuse to be emberassed by a mere mortal.”\n")
                s(8)
                print(player_name, ": “Just take this money Grimlee, I don't want any trouble”\n")
                s(3)
                print("*You pull out a bag of 100 coins.\n")
                coins = 0
                s(1.5)
                print("You now have 0 coins\n")
                s(1.5)
                print("Grimlee snatches it out of your hand with force. He picks you up and shoves you off his path. \n\nYou get through with no money but you were spared.\n")
                s(7)
        else:
            print("Invalid option!")

#------------------------------------- DWARF SHOP -------------------------------------

    # Dwarf treehouse shop
    def dwarf_shop():
        global coins, x
        print("\n")
        print("You chose the path which takes you to the dwarf treehouse as you approach the entrance of the towering dwarf Treehouse, \ngripping your trusty axe tightly...\n")
        s(10)
        # Dwars ASCII art
        print("""
        
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠤⠤⠤⠤⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⡄⠀⠀⠀⠀⠀⠀⠈⠉⠒⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣜⣄⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠘⢾⣆⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣊⠁⣀⣀⣀⣀⣀⠤⠤⠔⠒⠒⠚⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠉⠓⠦⡀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡠⠒⠉⠁⠀⠈⠉⠉⠉⠁⠀⣀⣀⣀⡤⠤⠤⠴⠒⠒⠲⠤⠤⢤⣀⡀⠀⠀⠀⠀⣈⡆⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣹⢤⢤⣀⣀⣀⣠⣤⠴⢲⣏⣽⠧⣄⠀⠀⠀⠀⠀⠀⢰⡶⡦⢤⡀⠹⡟⢖⠒⠒⢻⡀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⢼⠁⠀⡽⣿⣼⠃⠀⠹⠿⠷⠟⠛⠃⠀⠀⠀⠀⠀⠈⠉⠛⠚⠾⠆⣷⠸⡅⠙⢦⡇⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⡇⢈⢤⡞⡝⣫⢻⠀⠀⠀⠀⢰⣶⣤⣄⠀⠀⠀⠀⠀⠀⣴⣶⣂⠀⠀⢸⠀⢻⡄⣾⡇⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣞⣘⣾⣕⡿⡸⠀⠀⠀⠀⠺⠿⣿⠗⠀⢀⣠⠤⢄⡘⢿⣿⠟⠀⠀⠈⡆⢸⣟⡿⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣟⡾⡞⠀⡇⠀⠀⠀⠀⠀⠀⠉⠀⣠⠏⠀⠀⠀⠑⣟⠉⠀⠀⠀⠀⢱⠀⣯⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣿⣼⣘⡁⠀⢧⡀⠀⠀⠀⠀⠀⢀⣠⡿⣖⠦⠤⢖⣲⢯⣀⠀⠀⠀⠀⢸⠀⢸⡄⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠖⠋⠁⠀⠀⠀⠉⠓⢤⠙⠒⢒⣒⣒⡿⣝⡯⠋⠁⣀⣀⡀⠉⠻⣯⢍⠑⠒⢴⡚⠒⢸⠃⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠈⠩⠓⠋⣁⡠⠴⣏⣁⣈⣩⠷⠦⣈⡚⠽⢖⠤⠤⣠⣿⡀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠘⣷⡄⠀⠀⠀⠀⠀⠀⠀⣠⠏⢑⡖⠒⠒⣫⠏⠀⠀⠀⠸⡆⠀⠀⠀⠈⢉⠒⠒⠒⠒⠁⢸⠙⣆⠀⠀ ⠀⠀⠀⠀⠀
⠀⢀⣴⡿⠚⠦⠤⠤⠤⠤⢤⠞⠋⢠⠋⠀⣰⢲⠇⠀⠀⠀⠀⠀⢹⠀⠀⢀⠀⠀⠳⡀⠀⠀⠀⣠⡇⠘⣄⠀ ⠀⠀⠀⠀⠀
⣠⡟⡞⠀⠀⠀⠀⠀⠀⠀⣼⡃⢀⡟⠀⣰⠃⣽⡄⠀⠀⠀⠀⠀⠈⣆⠀⠀⠀⠀⠀⢣⠀⠀⠀⢻⢿⣯⣽⠽ ⠶⣄⠀⠀⠀
⢽⡇⠇⠀⠐⠒⠒⠒⠒⠋⠁⣻⡎⠁⢠⠃⠀⢹⡇⠀⠀⠀⠀⠀⢠⠏⠀⠀⣇⠀⠀⢸⠀⠀⢴⡾⠀⢷⡉⢱ ⡀⠈⠳⣄⠀
⢸⠀⡇⠀⠀⢤⣀⣀⣀⣀⠔⢹⡧⡄⠸⡄⠀⢸⡇⠀⠀⠀⠀⢀⡞⠀⠀⠀⣿⠀⠀⡎⠀⢰⣸⢧⠉⠙⣟⠊ ⢁⣴⠆⠈⣇
⠘⣇⠹⣆⠀⣀⡈⠉⠉⢀⣠⡛⠀⠙⠲⣏⠀⠘⠃⠀⠀⠀⠀⡞⠀⠀⠀⢠⡏⠀⠀⡇⣄⣴⠋⢈⡷⠀⣿⠀ ⠀⣻⡤⢴⡏
⠀⠘⠦⣈⣣⣌⣉⠒⠚⠉⣸⠁⠀⠀⠀⠘⢦⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⡞⠀⠀⠀⢁⡿⠁⠀⣼⡀⠀⠀⢀ ⣸⣏⠀⣠⠇
⠀⠀⠀⠀⢉⡏⠉⠉⡹⠉⡇⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⢸⠀⠀⠀⡸⠁⠀⠀⣺⠋⠀⠀⣴⠃⠙⠢⣄⣈ ⣿⠉⣿⡟⠀
⠀⠀⠀⠀⡜⠀⠀⢠⠃⢰⠁⠀⠀⠀⠀⠀⠀⠀⠈⠣⣄⡀⠈⠀⢀⠜⠁⢀⡤⠴⠋⠀⢀⣜⠁⠀⠀⠀⠀⠻ ⠼⠿⠉⠀⠀
⠀⠀⠀⢀⡇⠀⢀⠏⠀⠈⡣⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⡀⢋⡤⠔⠊⢀⣀⡤⠖⠁⢹⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⣾⠀⠀⡜⠀⢠⡏⠀⠀⠉⠉⠉⠒⠒⠒⠤⠤⠤⡤⠤⠽⠟⠒⠒⠉⠉⠀⠀⢀⡤⠊⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⡟⠀⣰⠁⠀⢨⠇⠦⠤⣄⣀⣀⠀⠀⠀⠀⠀⢀⣷⠀⠀⠀⠀⠀⣀⣀⠤⠚⠙⣇⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⡇⢀⡏⠀⠀⡎⠀⠀⠀⠀⠀⠉⠉⠑⠒⠒⠚⠉⡇⠐⠒⠒⠉⠉⠉⠀⠀⠀⠀⠙⠦⣀⡀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⢠⡇⠸⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⢤⡀⠀ ⠀⠀⠀⠀⠀
⠀⠀⢸⡇⠁⣠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆ ⠀⠀⠀⠀⠀
⠀⠀⢸⡇⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈ ⣇⠀⠀⠀⠀
⠀⠀⢸⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣔⡋⠙⠒⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣽⠀⠀⠀⠀
⠀⠀⠘⢧⣀⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢏⡼⠛⠒⠤⢄⣀⠉⠒⠢⠤⢄⣀⣀⣀⣀⣀⣀⣀⠤⢜⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣈⠙⠒⠦⠤⠤⠤⠤⠤⠤⠔⢊⡵⠋⠀⠀⠀⠀⠀⠈⠉⠒⠒⠢⠤⠤⠤⠤⠤⠤⠤⠤⠴⠚ ⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠙⠒⠒⠒⠒⠒⠒⠒⠒⠂⠉⠀


        """)
        print("The Dwarf emerges from the depths of the Treehouse, wiping sweat from his brow, and sucking in all power from the axe.")
        s(3)
        print("Dwarf: “Well traveller, What brings you to my humble abode?\n\n“A new upgrade maybe?”\n")
        s(7)
        print(player_name, ": “Greetings, stout dwarf. I come seeking wisdom and perhaps some assistance. \nI already possess and axe, from which you stole its power.”\n")
        s(8)
        print("Dwarf: Eyes your axe with a discerning gaze. “Ah, I see, \nbut let me tell you, my friend, the path you tread is treacherous, and what you hold now may not suffice. Behold the mighty MK2 Axe. \n\nA true marvel of craftsmanship and power. For a mere 100 gold coins, it can grant you the strength you may soon require.”\n")
        s(12)
        print(player_name, ": *Puzzled* “Strength I may require? Why would i.. what exact dangers lie ahead?”\n")
        s(5)
        print("Dwarf: Leans closer, speaking in a hushed tone. “This island holds challenges and adversaries far more formidable than you can imagine. \n\nThe MK2 Axe, with its superior durability and enhanced capabilities, will provide you with the edge you need to face the perils that await. \n\nIt is not merely about strength, but about the resilience and potency that a better weapon can offer.”\n")
        s(14)

        k=True
        # Looping for a valid input from player
        while k == True:
            global x
            x = 4
            weapon_purchase = input("Do you buy the MK2 Weapon? ").lower()
            # Checking if they want to buy the upgraded axe
            if weapon_purchase == "yes":
                # Making sure the player has enough coins
                if coins != 100:
                    print("\n")
                    print("You do not have enough coins, come back when you do!\n")
                    x= 4
                    shop_choice()
                print("\n")
                print(player_name, ": “Your words have given me pause. Very well, stout dwarf. I shall purchase the MK2 Axe. Here are your 100 gold coins.”\n")
                s(7)
                print("Dwarf: - Grinning widely, accepting the coins. “A wise decision, my friend! With the MK2 Axe in your possession, you shall wield a tool of true might. \n\nMay it aid you in your journey and keep you safe from harm. Good luck, brave adventurer, the path to the Rainbow Waterfall is your destiny!”\n")
                s(10)
                x = 3
                coins = 0
                s(1.5)
                print(player_name, ": “Thank you, stout dwarf, for your insight. I appreciate your guidance. Farewell!”\n")
                s(4)
                print("+ ENCHANTED AXE MK.II\n")
                shop_choice()
                return
            elif weapon_purchase == "no":
                print(player_name, ": “I appreciate your advice, but I shall trust in the axe I currently wield. Thank you for the offer, dwarf.”\n")
                s(6)
                print("Dwarf: *Nods solemnly, with a touch of concern in their eyes.* “Your choice, my friend, but remember that danger lurks around every corner. \n\nIf ever you find yourself in need, don't hesitate to return. Good luck on your journey, traveller, the path to the Rainbow Waterfall is your destiny!”\n")
                s(12)
                print(player_name, ": “Thank you, sturdy dwarf. I'll keep that in mind. Farewell!”\n")
                s(2)
                x = 4
                shop_choice()
                return
            else:
                print("Invalid option!")
                k=False

#------------------------------------- End Game -------------------------------------

    # When end game called it ends the game
    def end_game():
        print("CONGRATULATIONS, YOU HAVE FOUND THE GEMSTONE! You gain powerful magic from the gemstone that allowed you to return home!\n")
        print("THANK YOU FOR PLAYING!\n")
        menu()

#------------------------------------- DRAGON BATTLE -------------------------------------

    def dragon():

        print("Now that the octopus is dead, you start feasting on the octopus's raw flesh, to restore health and strength, \n\nRipping the flesh apart as if you were starving hyenas.\n")
        s(10)

        print("While engaged in the feast, the sun has disappeared, darkness fills the space, NO, it is not a solar eclipse, it is an enormous shadow casting over\n the sun and over the mountains.")
        print("An enormous shadow descends from above, from between the humongous mountains, rapidly moving over the twisted alleyway passage.\n")
        s(20)

        print("The earth starts shaking underneath the your feet, your heart pounding with fear and curiosity, eyes rolling, inspecting every inch of land he could see.")
        print("A mighty creature snorting flames from their nose, their red eyes wide open glaring with evil and rage, has descended onto your domain.\n")
        s(20)

        print("Dragon: “I am the mighty Draconice, the guardian of the sacred mountains.”\n")
        s(3)
        print(player_name, ": “Who are you?”\n")
        s(1)
        print("Dragon: “How dare you trespass my sacred mountains?”\n")
        s(2)
        print(player_name, "( mumbling with fear): “I am ",player_name,", I am a lost soul, I bear no harm, I am not an enemy, I humbly bow down against your enormous statue, your wisdom, and your knowledge.”\n")
        s(8)
        print(player_name, ": “I seek your immense powers and wisdom to aid me in my quest for glory.”\n")
        s(5)

        print("Dragon: “What is the glory you are seeking?”\n")
        s(3)
        print(player_name, ": “I seek to reach the gemstone in the mountains.”\n")
        s(3)
        print("Dragon: “many have tried, many have failed, many have lost their souls, and many have had my wrath spilled over them.”\n")
        s(6)
        print(player_name, ": “I bear no harm, I'm only seeking the glory, I accept your challenge.”\n")
        s(5)

        print("Dragon: “I shall put you to a test to see your worthiness.”")
        s(3)
        print("Dragon: “I command you to share your food with me.”\n")

        s(2)

        global player_health
        global j
        j = 0
        # Looping the question until a valid input is selected
        while j == 0:
            share_food = input("Do you share your food? ").lower()
            # Players choice whether or not to share the food
            if share_food == "yes":
                j = 1
                print(player_name, ": “I shall, with utmost humbleness, offer my food to you, great Draconice.”")
                s(5)
                print("Dragon: “I shall be at your service now. I shall use my immense powers, knowledge, and wisdom to serve you, to aid you in conquering your quest. \n\nAnd I shall offer you this potion to restore your health and strength.”\n")
                s(10)
                player_health = 100
                health()
                s(1)
                print(player_health, " HP ", " ".join(health_bar), "\n")
                s(2)
                print(player_name, ": “You shall now serve your master. Take me to the gemstone.”")
                s(4)
                print("Dragon: “I shall. (Hop in, bitch)\n”")
                s(2)
                print("And so you ride the mighty Draconice, holding the reins around Draconice's neck.")
                s(5)
                print("The mighty Draconice flies over the mountains and valleys until they reach Mount Everest, where the gemstone is hidden, directing you to its exact location.\n")
                s(8)
                end_game()
            elif share_food == "no":
                j = 1
                print("\n")
                print(player_name, ": “I shall not share my food with you, mighty Draconice, as this food is the only means for me to restore my health and strength.”\n")
                s(5)
                print("Dragon (Roaring and snorting flames): “How dare a wicked creature like yourself disobey my command?! I shall now cast my wrath over you.”\n")
                s(5)
                player_health = 0
                health()
                s(1)
                print(player_health, " HP ", " ".join(health_bar), "\n")
                print("The mighty Draconice captures you with his giant claws, rips him apart, dips you in the octopus's blood and flesh \n( with a side of Hummus) and munches every bit of him.\n")
                s(7)
            else:
                print("Invalid input!")

#------------------------------------- OCTOPUS BATTLE -------------------------------------

    def octopus_scene():
        print("But your moment of tranquility is abruptly shattered when a monstrous creature emerges from the depths of the pool beneath the waterfall. \n\nWith menacing tentacles and malevolent eyes, a giant octopus rises from the abyss, its intention clearly hostile. \n\nYour heart races and you instinctively draw your weapon, preparing for the imminent battle.\n")
        s(8)
        print("Adrenaline surges through your veins as you square off against the colossal cephalopod. Your skills and strategic prowess are pushed to the limit, \n\nfor this formidable opponent possesses both strength and cunning.\n")
        s(10)

        # If the player has the upgraded axe (x will = 3), then they can defeat the ocotpus
        global player_health
        if x == 3:
            print("Dodging tentacles and countering with well-timed strikes, your determination soars. The battle rages on amidst the thunderous roar of the waterfall, \nthe clash of steel, and the magical bursts of energy illuminating the forest. \n\nYour perseverance and resourcefulness became your greatest allies as you seek to bring down this monstrous foe.")
            s(12)
            print("\n")
            print("Ultimately, after an arduous struggle, you emerge victorious. The behemoth lets out a final, deafening cry before collapsing in the shallows. \nGasping for breath and covered in sweat, you stand triumphant, your achievement resonating within the tranquil surroundings.\n")
            s(10)
            print("As the adrenaline subsides, you take a moment to catch your breath and marvel at the majestic waterfall once more. \nYou have overcome a formidable challenge and emerged stronger for it.\n")
            s(7)
            dragon()
        # Otherwise they lost the fight automatically and they have to start again
        else:
            print("Your heart sinks, realising too late that your weapon, once your faithful companion, will prove futile against such a formidable adversary.\n")
            s(7)
            print("Desperation fuels your every move as you swing your feeble blade. But with each strike it becomes clear your efforts are in vain. \nThe creature's amorphous flesh is impenetrable and deflects your fruitless attacks effortlessly, its tentacles lashing out with lethal precision. \n\nOverwhelmed and outmatched, your strength wanes, and despair settles in.\n")
            s(18)
            print("The relentless assault proves too much to bear, with its slimy tentacles wrapped around you, constricting with bone-crushing force, you gasp for air, \nyour vision blurs as darkness encroaches upon your consciousness. Your weapon slips from your grasp, your valiant efforts falling short.\n")
            s(15)
            print("Your life force fades away, consumed by the relentless power of your adversary. The forest grows silent, save for the melancholic rumble of the waterfall, \nbearing witness to your tragic demise.\n")
            s(8)
            player_health = 0
            health()

#------------------------------------- QUICK WATERFALL FUNCTION -------------------------------------

    def waterfall():
        print("As you continue on your journey, your eyes catch sight of a shimmering waterfall nestled within the lush, enchanted forest. \n\nThe cascading waters sparkle in the moonlight, beckoning you to explore its hidden secrets. \n\nIntrigued by the ethereal beauty, you approach cautiously, feeling the cool mist on your skin and hearing the soothing melody of the rushing water.\n")
        s(4)
        octopus_scene()

#------------------------------------- SHOP OR WATERFALL DECISION -------------------------------------

    # The first function called after the bandit interaction, player choosing to go shop, or skip iit (waterfall)
    def shop_choice():
        print("You notice a huge waterfall on the right, and on left, an odd looking treehouse in the distance.\n")
        s(1.5)
        
        global z, x
        z = 0
        while z == 0:
            global choice2
            choice2 = input("Which path do you choose? ").lower()
            if choice2 == "left":
                z = 1
                dwarf_shop()
                return
            elif choice2 == "right":
                z = 1
                waterfall()
                return
            else:
                print("Invalid option!")

    print("There are now 2 paths in which you can take.\n")
    shop_choice()

# Menu function
def menu():
    #------------------------------ Title Screen ------------------------------
    print("\n")
    print("---------------------------------------------------------------")
    print("  _________.__                .___                      ____   ")
    print(" /   _____/|  |__ _____     __| _/______  _  ________  /  _ \  ")
    print(" \_____  \ |  |  \\__  \   / __ |/  _ \ \/ \/ /  ___/  >  _ </")
    print(" /        \|   Y  \/ __ \_/ /_/ (  <_> )     /\___ \  /  <_\ \/")
    print("/_______  /|___|  (____  /\____ |\____/ \/\_//____  > \_____\ ")
    print("        \/      \/     \/      \/                 \/         \/")
    print("___________            __                .__                   ")
    print("\__    ___/___   _____/  |______    ____ |  |   ____   ______  ")
    print("  |    |_/ __ \ /    \   __\__  \ _/ ___\|  | _/ __ \ /  ___/  ")
    print("  |    |\  ___/|   |  \  |  / __ \\  \___|  |_\  ___/ \___ \   ")
    print("  |____| \___  >___|  /__| (____  /\___  >____/\___  >____  >  ")
    print("             \/     \/          \/     \/          \/     \/   ")
    print("---------------------------------------------------------------\n")

    global start_menu
    start_menu = input("Type 'Play' to play the game! \nType 'Quit' to quit the game!\n\n").lower()

    # Checking what option the user selected
    if start_menu == "play":
        game()
    elif start_menu == "quit":
        #exit
        quit()
    else:
        print("\nInvalid option!\n")
        menu()

menu()
#-----------------------------------------------------------------------------