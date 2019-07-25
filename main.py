
# hero game

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
rm4 = ()

rm1Desc = 'The room is small, cold and with exits to the north, south & east'
rm1 = (rm2, rm3, rm4, 0, rm1Desc, 'Monster', 5, 3, 0.2)

# set the first room as room 1, rm1
rm = rm1

# hLife (Hero Life) = 10
hLife = 10

# hArm (Hero Armour) = 2
hArm = 2

# armour is a number from 0 to 10, 0 being the easiest to hit and 10 being the
#  hardest

# hWeap (Hero Weapon) = 0.1
hWeap = 0.1

# set Combat Turn to Hero's turn first
hTurn = True


# start
# =====

# draw
# ====
# draw/describe the room
print(rm[4])

# look up room attributes based on roomId
# if the room contains a monster then event = Combat else the event is set to
#  Other
if rm[5] == 'Monster':
    Event = 'Combat'
    mLife = rm[6]
    mArm = rm[7]
    mWeap = rm[8]
    print('Monster : Life:', mLife, ': Armour:', mArm, ': Weapon:', mWeap)
else:
    Event = 'Other'

# test if Event is being set correctly based on whether a monster is in the
#  room or not
print(Event)

# event
# =====
# each event has its own set of actions, effects, results, end of event, end of
#  game
# Combat : Attack or Run Away
# Forced Move : Move (N,S,E,W) only
# Other : Move (later : Look, Rest e.g. rest could heal 1 point of life)


# Combat
# ======

if Event == 'Combat':
    # Who's turn?
    # -----------
    # All Combat events start with the Hero's turn, hTurn is TRUE
    # hTurn is FALSE when it is the Monster's turn
    # If hTurn then: weapon = hWeap, armour = hArm, life = hLife
    # Else: weapon = mWeapon, armour = mArm, life = mLife
    if hTurn:
        life = hLife
        armour = hArm
        weapon = hWeap
    else:
        life = mLife
        armour = mArm
        weapon = mWeap

    print(hTurn, ': Life:', life, ': Armour:', armour, ': Weapon:', weapon)

    # Action
    # ------
    # If hTurn is TRUE then check if the player wants to Attack or Run_Away
    # If hTurn is FALSE i.e. its the Monster's turn, then always set Action
    #  to Attack
    # If Run_Away then End_Combat_Event
    # Else if Attack then go to Effect

    if hTurn:
        hChoice = input('Attack or Run Away -->')
        print(hChoice)
        if hChoice == 'A':
            print()
        elif hChoice == 'R':
            print('End of combat... go to Forced Move')

        # Effect
        # ------
        # Check hit or miss
        # to check hit, the attacker roles a 1d10 (add modifiers later
        #  e.g. strength, potions, rings etc)
        # if the attackRoll > armour then hit else miss

        # If hit then calculate damage, dmg = 1d10 x (1+Weapon)
        # Else If miss then dmg = 0

    # Weapon modifies damage; all damage starts at a number between 1 and 10
    # Weapon then modifies damage e.g Short sword has a 0.2 modifier

    # Result
    # ------
    # life = life - dmg

    # End_of_Event
    # ------------
    # If Not Attack (i.e. Run_Away) then set Event to Forced_Move and jump to
    #  Event
    # If life <= 0 then hero or monster is dead so Combat is ended
    # Else: flip who's turn it is, heroTurn = not heroTurn

    # End_of_Game
    # -----------
    # If heroTurn then Game_Over is True
    # Else Monster_Dead is True

    # Monster_Dead
    # ------------
    # Collect treasure, heroTurn is True, set Event to Other and jump to Event


# Forced_Move
# ===========
# A forced move is where the Hero is running away from a monster, so must
# choose a direction to run to

# Adding a print statement to test running of the script
print('end of script...')
