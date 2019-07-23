
# hero game

# set up variables
# ================

# roomId is a list?
# e.g. roomId N = 1, S = 0, E = 3, Desc = "The room was empty ..", Monster
#  = Monster etc
# the number following the compass direction e.g. N, S, E, W is the room that
#  the exit in that compass direction leads
# e.g. head north leads to room 1, roomId is set to 1

# hLife (Hero Life) = 10
# hArm (Hero Armour) = 2
# armour is a number from 0 to 10, 0 being the easiest to hit and 10 being the
#  hardest


# start
# =====

# draw
# ====
# draw/describe the room
# look up room attributes based on roomId
# if the room contains a monster then event = Combat else the event is set to
#  Other

# event
# =====
# each event has its own set of actions, effects, results, end of event, end of
#  game
# Combat : Attack or Run Away
# Forced Move : Move (N,S,E,W) only
# Other : Move (later : Look, Rest e.g. rest could heal 1 point of life)


# Combat
# ======

# Who's turn?
# -----------
# All Combat events start with the Hero's turn, heroTurn is TRUE
# heroTurn is FALSE when it is the Monster's turn
# If heroTurn then: weapon = hWeap, armour = hArm, life = hLife
# Else: weapon = mWeapon, armour = mArm, life = mLife

# Action
# ------
# If heroTurn is TRUE then check if the player wants to Attack or Run_Away
# If heroTurn is FALSE i.e. its the Monster's turn, then always set to Action
# to Attack
# If Run_Away then End_Combat_Event
# Else if Attack then go to Effect

# Effect
# ------
# Check hit or miss
# to check hit, the attacker roles a 1d10 (add modifiers later e.g. strength,
#  potions, rings etc)
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
# If Not Attack (i.e. Run_Away) then set Event to Forced_Move and jump to Event
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

# add a line to test upload to Github
