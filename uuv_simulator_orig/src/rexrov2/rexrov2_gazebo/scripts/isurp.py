#!/usr/bin/env python
# license removed for brevity

import rospy
from uuv_gazebo_ros_plugins_msgs.msg import FloatStamped


def thrusters_input():

    pub2 = rospy.Publisher('/rexrov2/thrusters/2/input', FloatStamped, queue_size=10)
    pub3 = rospy.Publisher('/rexrov2/thrusters/3/input', FloatStamped, queue_size=10)
    pub4 = rospy.Publisher('/rexrov2/thrusters/4/input', FloatStamped, queue_size=10)
    pub5 = rospy.Publisher('/rexrov2/thrusters/5/input', FloatStamped, queue_size=10)
    rospy.init_node('isurp', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg2 = FloatStamped()
        msg2.header.stamp = rospy.Time.now()
        msg2.header.frame_id = "rexrov2/thruster_2"
        msg2.data = 800
        rospy.loginfo(msg2)

        msg3 = FloatStamped()
        msg3.header.stamp = rospy.Time.now()
        msg3.header.frame_id = "rexrov2/thruster_3"
        msg3.data = 800
        rospy.loginfo(msg3)

        msg4 = FloatStamped() 
        msg4.header.stamp = rospy.Time.now()
        msg4.header.frame_id = "rexrov2/thruster_4"
        msg4.data = 800
        rospy.loginfo(msg4)

        msg5 = FloatStamped() 
        msg5.header.stamp = rospy.Time.now()
        msg5.header.frame_id = "rexrov2/thruster_5"
        msg5.data = 800
        rospy.loginfo(msg5)
        
        pub2.publish(msg2)
        pub3.publish(msg3)
        pub4.publish(msg4)
        pub5.publish(msg5)

        rate.sleep()

if __name__ == '__main__':
    try:
        thrusters_input()
    except rospy.ROSInterruptException:
        pass