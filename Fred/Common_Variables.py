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
# Common_Variables.py                                        #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Creating the Common Variables"
##############################################################
#                                                            #
# System wide global variable creation                       #
#                                                            #
##############################################################

# This is how much quiet time must elapse for the robot 
# goes to sleep. The time is in mili-seconds.
TimeToSleep = 15 * 60000    

# when the sleep timer is enabled, this allows the robot to sleep.
Awake = True                

# To simplify the head movements, we need to keep track of
# where the head is pointed, for that we use following variables
HeadPanPos = 0
HeadTiltPos = 0
HeadRollRos = 0
