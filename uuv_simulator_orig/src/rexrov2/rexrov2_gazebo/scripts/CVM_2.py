import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
import geometry_msgs.msg as geometry_msgs

class curvature_velocity_method:
	def __init__(self):
		self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
		self.range_subscriber = rospy.Subscriber('/rexrov2/sonar_p900', LaserScan, self.range_callback)

	def range_callback(self, data):
		ranges = data.ranges
		angle_min = -0.7853999733924866
		angle_max = 0.7853999733924866
		angle_increment = 0.003073972649872303

		min_range = min(ranges)

		if min_range< 1:
			curvature = -1/min_range
			if curvature<-1:
				curvature  = -1
			if curvature >1:
				curvature = 1
			linear_velocity = 0.5 # Adjust the linear velocity as needed
			angular_velocity = curvature * linear_velocity
			# Publish the Twist message to control the robot's velocity and direction

			cmd_vel = Twist()
			cmd_vel.linear.x = linear_velocity
			cmd_vel.angular.z = angular_velocity
			self.cmd_vel_pub.publish(cmd_vel)

		else:
			cmd_vel = Twist()
			cmd_vel.linear.x = 1.0
			self.cmd_vel_pub.publish(cmd_vel)	


if __name__ == "__main__":
	rospy.init_node('CVM_2')
	avoidance = curvature_velocity_method
	rospy.spin()

