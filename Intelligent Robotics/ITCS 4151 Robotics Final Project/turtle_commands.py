#!/usr/bin/env python

import rospy
import time
import math
from geometry_msgs.msg import Twist

'''
Instructions
Accept keyboard commands for the following:
    i. Move forward or backwards for X number of seconds               --- done
        1. Limit the time to 2 seconds
    ii. Move forward or backwards X distance                           --- done
        1. Limit to 0.33m
    iii. Turn 90 degrees clockwise                                     --- done?
    iv. Turn 90 degrees counter-testing for nowclockwise               --- done?
    v. Turn X degrees                                                  ---
        1. Limit to [--180, 180] degrees
    vi. Change the linear and angular velocities of the Robot          --- done
        1. Limit the linear velocity to 0.33m/s and angular velocity
           to 0.52rad/s

Publish msgs of type geometry_msgs/Twist to the topic
'mobile_base/commands/velocity' to drive the Turtlebot

Sorta helpful link(s):
http://wiki.ros.org/geometry_msgs

'''

# MENU--------------------------------------------------------------------- #
def showMenu():
    print "Menu: "
    print "1. Move forward or backwards for X number of seconds"
    print "2. Move forward or backwards X distance"
    print "3. Turn 90 degrees clockwise."
    print "4. Turn 90 degrees counter-clockwise"
    print "5. Turn X degrees."
    print "6. Change the linear and angular velocities of the robot."

    choice = int(raw_input("> "))

    while (choice < 1 or choice > 6):
        print "Wrong Input. Enter a number from 1 to 6."
        choice = int(raw_input("> "))

    return choice

# PUBLISH TWIST------------------------------------------------------------ #
def run_robot(twist, pub, t):
    r = rospy.Rate(10)
    '''
    limit = time.time() + t

    while time.time() < limit:
        pub.publish(twist)
        r.sleep()
    '''

    d = rospy.Duration(t)
    #d = rospy.Duration(degToRad(90)/twist.angular.z)
    s = rospy.Time.now()
    while rospy.Time.now() - s < d:
        pub.publish(twist)
        r.sleep()


# MOVEMENT FUNCTIONS------------------------------------------------------- #
def moveX(twist, pub, speed, direction, t):
    twist.linear.x = speed * direction
    twist.angular.z = 0

    run_robot(twist, pub, t)

def rotate(twist, pub, degrees, angular_vel):

    degree_error = 25 # For some reason, when testing with turtlesim
                      # everything was 25 degrees off :(!!

    if degrees < 0:
        seconds = float(degToRad((degrees*-1)-degree_error) / abs(angular_vel))
        twist.angular.z = (angular_vel * -1)
    else:
        seconds = float(degToRad(degrees-degree_error) / abs(angular_vel))
        twist.angular.z = angular_vel
        print "seconds: ", seconds, " t: ", twist.angular.z

    twist.linear.x = 0

    run_robot(twist, pub, seconds)

def degToRad(deg):
    return ( (deg * 3.14159) / 180.0)

# MAIN--------------------------------------------------------------------- #
def run():
    rospy.init_node('turtle_commands', anonymous=True)

    # Use the below for connecting to the actual Turtlebot
    # pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

    # Currently using this to connect to the required topic for Turtlesim
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    #r = rospy.Rate(10)

    twist = Twist() # create new Twist() msg. Used for publishing to the topic.

    speed = 0.3 # Set as default value (meters/second). Also 'velocity'
    angular_vel = 0.5 # Set as default value. This is the 'angular velocity'

    while not rospy.is_shutdown():
        choice = showMenu()

        if choice == 1:
            print "The Turtlebot will move forward or backwards for X number of seconds."

            print "Forwards or Backwards? Enter 1 or -1: "
            direction = int(raw_input("> "))
            while not (direction == -1 or direction == 1):
                print "Must be 1 or -1. Please enter again."
                direction = float(raw_input("> "))

            print "Please enter the number of seconds (max 2)."
            seconds = float(raw_input("> "))
            while seconds > 2:
                print "Must be less than 2 seconds. Please enter again."
                seconds = float(raw_input("> "))

            moveX(twist, pub, speed, direction, seconds)

        elif choice == 2:
            print "The Turtlebot will move forward or backwards X distance."

            print "Forwards or Backwards? Enter 1 or -1: "
            direction = int(raw_input("> "))
            while not (direction == -1 or direction == 1):
                print "Must be 1 or -1. Please enter again."
                direction = float(raw_input("> "))

            print "Please enter the distance (max 0.33m)."
            distance = float(raw_input("> "))
            while distance > 0.33:
                print "Must be less than 0.33m. Please enter again."
                distance = float(raw_input("> "))

            # time (in seconds) = distance (meters) / speed (meters/second)
            seconds = distance / speed

            moveX(twist, pub, speed, direction, seconds)

        elif choice == 3:
            print "The Turtlebot will turn 90 degrees clockwise."

            #seconds = float(degToRad(90) / angular_vel)
            # multiply angular_vel by -1 to give clockwise direction
            rotate(twist, pub, -90, angular_vel)

            # Notes
            # angular_vel = radians/seconds
            # we want 90 degrees (don't forget to convert to radians)
            # math.radians(90) = math.pi/2

            # math.radians(90) works correctly
            # seconds = float(math.radians(90) / angular

            # ******************************************************
            # In theory, if angular_vel = math.radians(90), this should also
            # rotate 90 degrees, correct? (line 144) (Except there's a limit
            # to angular_vel...)
            # Because in one second, it would rotate for 1.57079... radians
            # rotate(twist, pub, 1, angular_vel)
            # ******************************************************

        elif choice == 4:
            print "The Turtlebot will turn 90 degrees counter clockwise."

            #seconds = float(degToRad(90) / angular_vel)
            rotate(twist, pub, 90, angular_vel)

        elif choice == 5:
            print "The Turtlebot will turn X degrees."

            print "How many degrees would you like to turn? (from -180 to 180 degrees)."
            degrees = float(raw_input("> "))

            while degrees > 180 or degrees < -180:
                print "Invalid input. Must be between -180 and 180 degrees."
                degrees = float(raw_input("> "))

            rotate(twist, pub, degrees, angular_vel)

            '''
            if degrees < 0:
                #seconds = float(degToRad(degrees*-1) / angular_vel)
                rotate(twist, pub, degrees, angular_vel*-1)
            else:
                #seconds = float(degToRad(degrees) / angular_vel)
                rotate(twist, pub, degrees, angular_vel)
            '''

        elif choice == 6:
            print ("%s %.2f %s %.2f" %
                  ("The current velocity is", speed,
                   " and the current angular velocity is ", angular_vel))

            print "Enter a new velocity (less than 0.33)."
            speed = float(raw_input("> "))
            while speed > 0.33:
                print "Invalid input. Must be less than 0.33. Please enter again."
                speed = float(raw_input("> "))

            print "Enter a new angular velocity (less than 0.52)."
            angular_vel = float(raw_input("> "))
            while angular_vel > 0.52:
                print "Invalid input. Must be less than 0.52. Please enter again."
                angular_vel = float(raw_input("> "))



# ------------------------------------------------------------------------- #
if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
        pass
