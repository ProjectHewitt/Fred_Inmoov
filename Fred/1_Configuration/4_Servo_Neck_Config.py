##############################################################
#                                                            #
# Program Code for Fred Inmoov                               #
# Of the Cyber_One YouTube Channel                           #
# https://www.youtube.com/cyber_one                          #
#                                                            #
# This is version 5                                          #
# Divided up into sub programs                               #
# Coded for the Nixie Version of MyRobotLab.                 #
#                                                            #
# Running on MyRobotLab (MRL) http://myrobotlab.org/         #
# Fred in a modified Inmmov robot, you can find all the      #
# origonal files on the Inmoov web site. http://inmoov.fr/   #
#                                                            #
# 4_Servo_Neck_Config.py                                     #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Servo Neck Config"
##############################################################
#                                                            #
# Servo Neck Group                                           #
#                                                            #
##############################################################
# Depending on if you build the original version or the new
# Roll neck version there will be 2 or 3 sesrvos installed.

# The HeadYaw is used to turn the head left and right, In the
# Official version this is mostly center back using a HS805BB
# in Fred's modified version its a JX PDI6221MG.
EnableHeadYaw = True
HeadYawAttachment = "Head"      # "arduinoLeft"
HeadYawPin = 0                  # 13
HeadYawMinPos = 75               # 30
HeadYawMaxPos = 180             # 150
HeadYawMaxSpeed = 30            # -1

# The HeadPitch is used to move the head up and down, this is 
# located in the center of the torso between the front and 
# back frames driving a piston up and down.  In the Official
# version this is a HS805BB servo, in Fred I used a Servo 
# Adapter and fitted a JX PDI6221MG servo.
EnableHeadPitch = True
HeadPitchAttachment = "Head"    # "arduinoLeft"
HeadPitchPin = 10                # 12
HeadPitchMinPos = 35          # 20
HeadPitchMaxPos = 180             # 160
HeadPitchMaxSpeed = 30          # -1
HeadPitchRestPos = 95           # -1

# In the original version, this servo did not exist. 
# The roll neck allows the neck plate to roll left and right
# in turn allowing the head to maintain it's orientation when
# the head turns left or right while looking slightly up or down
# The roll Neck was first introduced by Bob Huston in his 
# build and embraced by many builders, later Gael redigned
# this to eliminate its major weaknes and has included it in
# the Official parts list. This is still an optional update.
EnableHeadRoll = True
HeadRollAttachment = "Head"     # "arduinoRight"
HeadRollPin = 8                 # 13
HeadRollMinPos = 20             # 60
HeadRollMaxPos = 160            # 130
HeadRollMaxSpeed = 30           # -1

