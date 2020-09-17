#!/usr/bin/python3
import rospy
from Custom_Msg.msg import Complex



def callback(msg):
    print('Real:', msg.real)
    print('Imaginary:', msg.imaginary)
    print("\n----------------------------\n")


rospy.init_node('message_subscriber')
sub = rospy.Subscriber('complex', Complex, callback)
rospy.spin()