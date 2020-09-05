#!/usr/bin/python3

import rospy
from std_msgs.msg import Int32


def callback(msg):
    print(msg.data)


rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('timer', Int32, callback=callback)

rospy.spin()




