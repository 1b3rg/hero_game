# hero game

import random

# set up variables
# ================

# roomId is a list?
# e.g. roomId N = 1, S = 0, E = 3,
#  Desc = "The room was empty ..", Monster, mLife, mArm, mWeap
# the number following the compass direction e.g. N, S, E, W is the room that
#  the exit in that compass direction leads
# e.g. head north leads to room 1, roomId is set to 1
# including the exits in the room description is a bit limiting, consider
#  changing later

rm1 = ()
rm2 = ()
rm3 = ()

rm1Desc = """The room is small, cold and with exits to the north,
           east & west .."""
rm2Desc = """The room is a dark dead end, the only exit is to the south .."""
rm3Desc = """This is a small, narrow passage leading to nowhere, the only
           exit is back to the west .."""

rm1 = (rm2, 0, rm3, 0, rm1Desc, 'Monster', 5, 3, 0.2)
rm2 = (0, rm1, 0, 0, rm2Desc, 'No Monster', 0, 0, 0)
rm3 = (0, 0, 0, rm1, rm3Desc, 'No Monster', 0, 0, 0)

# set the first room as room 1, rm1
rm = rm1

# hLife (Hero Life) = 10
hLife = 10

# hArm (Hero Armour) = 2
hArm = 6

# armour is a number from 0 to 10, 0 being the easiest to hit and 10 being the
#  hardest

# hWeap (Hero Weapon) = 0.1
hWeap = 0.1

# set Combat Turn to Hero's turn first
hTurn = True

# set hit to false
hit = False

# set move to false
move = False

# set game over to false
gameOver = False


# start
# =====

# while hLife is not zero (hero is alive) or big goal is not achieved then do:
#   draw room
#   check room for monster, if room contains monster then event is combat
#      run combat until hero or monster is dead
#      if monster is dead then update room to show monster is dead, rm[5] =
#      no monster
#   while not move (to another room) do other events e.g. move, search, rest
#      if move then get direction and update room, rm = new room and set move
#      to True i.e. don't do anything else until the room is redrawn and the
#      room attributes have been refreshed
#      if search then search
#      if rest then rest


# draw
# ====
# draw/describe the room
print(rm[4])

# look up room attributes based on roomId
# if the room contains a monster then event = Combat else the event is set to
#   Other
# (but what if the monster has been killed? need to append the list to say that
#   the monster is dead?)

if rm[5] == 'Monster':
    monsterDead = False
    Event = 'Combat'
    mLife = rm[6]
    mArm = rm[7]
    mWeap = rm[8]
    print('Monster : Life:', mLife, ': Armour:', mArm, ': Weapon:', mWeap)
    print('')

# event
# =====
# each event has its own set of actions, effects, results, end of event, end of
#  game
# Combat : Attack or Run Away
# Forced Move : Move (N,S,E,W) only
# Other : Move (later : Look, Rest e.g. rest could heal 1 point of life)


# Combat
# ======

while Event == 'Combat':

    # Who's turn?
    # -----------
    # All Combat events start with the Hero's turn, hTurn is TRUE
    # hTurn is FALSE when it is the Monster's turn
    # If hTurn then: weapon = hWeap, armour = mArm, life = mLife
    # Else: weapon = mWeapon, armour = hArm, life = hLife
    if hTurn:
        print("It is the hero's turn..")
        life = mLife
        print("The monster's life is: ", mLife)
        armour = mArm
        print("The monster's armour is: ", mArm)
        weapon = hWeap
        print("The hero's weapon is: ", hWeap, "\n")

        # Action
        # ------
        # If hTurn is TRUE then check if the player wants to Attack or Run_Away
        # If hTurn is FALSE i.e. its the Monster's turn, then always set Action
        #  to Attack
        # If Run_Away then End_Combat_Event
        # Else if Attack then go to Effect
        hChoice = input('Attack or Run Away -->')
        if hChoice == 'A':
            print()
        elif hChoice == 'R':
            print('End of combat... go to Forced Move')
    else:
        print("It is the monster's turn..")
        life = hLife
        print("The hero's life is: ", hLife)
        armour = hArm
        print("The hero's armour is: ", hArm)
        weapon = mWeap
        print("The monster's weapon is: ", mWeap, "\n")

    print(hChoice)
    if hChoice == 'R':
        break

    # Effect
    # ------
    # Check hit or miss
    # to check hit, the attacker roles a 1d10 (add modifiers later
    #  e.g. strength, potions, rings etc)
    # if the attackRoll > armour then hit else miss

    attackRoll = random.randint(0, 10)
    print('Attack Roll', attackRoll, ': Armour', armour)
    if attackRoll > armour:
        hit = True
        print('The attack hit...')

    # If hit then calculate damage, dmg = 1d10 x (1+Weapon)
    # Else If miss then dmg = 0
    if hit:
        # Weapon modifies damage; all damage starts at a number
        #    between 1 and 10
        # Weapon then modifies damage e.g Short sword has a 0.2 modifier
        dmg = int(random.randint(0, 6)*(1+weapon))
        print('... and the damage is', dmg)
        # reset hit
        hit = False
    else:
        dmg = 0
        print('The attack missed...')

    # Result
    # ------
    # life = life - dmg
    life = life - dmg
    print("Hero's turn?", hTurn, ".. Defender's life remaining: ", life, "\n")

    # Check for end of combat
    # -----------------------
    # If life <= 0 then:
    #   hero or monster is dead so combat is over, event = ''
    #   if heroTurn then:
    #      gameOver = True
    #   else:
    #      monsterDead = True
    #      collect treasure
    #      (reset) heroTurn = True
    # else:
    #   (resolve life) if heroTurn then hLife = life, else mLife = life
    #   flip who's turn it is, heroTurn = not heroTurn
    if life <= 0:
        Event = 'Other'
        print(Event, "\n")
        if hTurn:
            monsterDead = True
            print("Monster is dead ..")
            # collect treasure
        else:
            gameOver = True
            print("Hero is dead ..\nGame over ..")
    else:
        if hTurn:
            mLife = life
            hTurn = False
        else:
            hLife = life
            hTurn = True

# Adding a print statement to test running of the script
print('end of script...')
