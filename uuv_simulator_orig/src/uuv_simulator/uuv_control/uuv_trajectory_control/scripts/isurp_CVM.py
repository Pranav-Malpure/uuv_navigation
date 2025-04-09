#!/usr/bin/env python

import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
# import geometry_msgs.msg as geometry_msgs
from geometry_msgs.msg import Twist
import math
import matplotlib.pyplot as plt

from dynamic_reconfigure.server import Server
from uuv_control_cascaded_pid.cfg import PositionControlConfig
from nav_msgs.msg import Odometry
from rospy.numpy_msg import numpy_msg

r_obs = 2 #This is actually the approx radius of vehicle
max_linear_vel = 1.5 # 1.5 m/s
max_angular_vel = 1  # 1 rad/sec

#For sonar_p900
# angle_min= -0.7853999733924866
# angle_max= 0.7853999733924866
# angle_increment= 0.003073972649872303

#For sss_front
angle_min= -0.5235990285873413
angle_max= 0.5235990285873413
angle_increment= 0.0177491195499897

obstacle_on = False
inf = float('inf')
ranges_plot = []
rv_plot = []
# current_curvature = 
tv = 0.3 #Setting the velocity in x in vehicle frame as 0.2 
# rate = rospy.Rate(3)

class curvature_velocity_method:
	def __init__(self):
		# rospy.init_node("isurp_CVM", anonymous = True)
		# print("starttttt")
		self.cmd_vel_pub = rospy.Publisher('/rexrov2/cmd_vel', Twist, queue_size = 10)
		self.sub_odometry = rospy.Subscriber('odom', numpy_msg(Odometry), self.odometry_callback)
		self.range_subscriber = rospy.Subscriber('/rexrov2/sss_front', LaserScan, self.sonar_p900_callback)

	def odometry_callback(self, data):
		print("Odometry!!!!!!")

	def sonar_p900_callback(self, data):
		print('Subscriber call backed')

		global obstacle_on
		
		ranges = data.ranges
		
		
		cmd_vel_pub_msg = Twist()

		ranges = list(map(lambda x: float('inf') if x > 5 else x, ranges))
		
		print("minimum_range %f" %min(ranges))

		d_v = []
		c_min = []
		c_max = []
		curvature_desired = []
		# x_obs
		"""
		min_element = min(enumerate(ranges), key=lambda x: x[1])

		theta = angle_min + angle_increment*min_element[0]

		min_range = min(ranges)

		x_obs = float(min_range)*np.cos(theta)
		y_obs = float(min_range)*np.sin(theta)

		c_min = (2*(x_obs-y_obs)/(np.sqrt(x_obs**2 + y_obs**2 + r_obs**2)))
		# c_max = (2*(x_obs+y_obs)/(np.sqrt(x_obs**2 + y_obs**2 + r_obs**2)))

		rv = -c_min*tv

		print("rv %f" %rv)
		

		cmd_vel_pub_msg.linear.x = tv
		cmd_vel_pub_msg.angular.z = rv	
		self.cmd_vel_pub.publish(cmd_vel_pub_msg)

		return
		"""

		# a = np.arange(len(ranges))

		for i in range(len(ranges)):
			cmd_vel_pub_msg = Twist()

			if ranges[i] == float('inf'):
				curvature_desired.append(0)
				d_v.append(float('inf'))
				c_max = 0
				c_min = float('inf')
				continue
			theta = angle_min + angle_increment*i
			x_obs = float(ranges[i])*np.cos(theta)
			y_obs = float(ranges[i])*np.sin(theta)
			# print('x_obs %f' %x_obs)
			# print('y_obs %f' %y_obs)

			if np.isnan(x_obs):
				d_v.append(float(inf))
				curvature_desired.append(0)
				continue

			if np.isnan(y_obs):
				d_v.append(float(inf))
				curvature_desired.append(0)
				continue

			# if y_obs == float('inf'):
			# 	curvature_desired.append(0)
			# 	d_v.append(0)
			# 	c_max = 0
			# 	c_min = float('inf')
			# 	continue

			# if x_obs == float('inf'):
			# 	curvature_desired.append(0)
			# 	d_v.append(0)
			# 	c_max = 0
			# 	c_min = float('inf')
			# 	continue
			# print(x_obs)
			# print(y_obs)


			c_min = (2*(x_obs-y_obs)/(np.sqrt(x_obs**2 + y_obs**2 + r_obs**2)))
			c_max = (2*(x_obs+y_obs)/(np.sqrt(x_obs**2 + y_obs**2 + r_obs**2)))
			# print("c_min %f" %c_min)
			# print("c_max %f" %c_max)
			x_min = (x_obs - r_obs)/(1 - c_min*r_obs)
			y_min = y_obs/(1 - c_min*r_obs)

			x_max = (x_obs + r_obs)/(1 + c_min*r_obs)
			y_max = y_obs/(1 + c_min*r_obs)

			# Calculation for d_c_min
			if c_min<0:
				theta_curvature_min = np.arctan(y_min/(x_min - 1/c_min))
			elif c_min>0:
				theta_curvature_min = np.pi - np.arctan(y_min/(x_min - 1/c_min))

			if abs(c_min) < 0.00001:
				d_c_min = y_min
			else:
				d_c_min = np.abs(1/c_min)*theta_curvature_min


			#Calculation for d_c_max
			if c_max<0:
				theta_curvature_max = np.arctan(y_max/(x_max - 1/c_max))
			elif c_max>0:
				theta_curvature_max = np.pi - np.arctan(y_max/(x_max - 1/c_max))

			if abs(c_max) <0.00001:
				d_c_max = y_max
			else:
				d_c_max = np.abs(1/c_max)*theta_curvature_max


			#Calculation of d_v, assuming now that current curvature is between c_min and c_max
					# if c_min<current_curvature and c_max>current_curvature:

			d_v.append(min(d_c_max, d_c_min))
			if d_c_max>=d_c_min:
				curvature_desired.append(c_min)
			else:
				curvature_desired.append(c_max)


		min_element = min(enumerate(d_v), key=lambda x: x[1])
		d_v_min_index = min_element[0]

		min_curvature = curvature_desired[d_v_min_index]

		# if obstacle_on == False:
		# 	sign = np.sign(angle_min + angle_increment*d_v_min_index)

		# if min(ranges) != float('inf'):
		# 	obstacle_on = True

		# if min(ranges) == float('inf'):
		# 	obstacle_on = False



		if np.isnan(min_curvature):
			min_curvature = 0

		if min_curvature == float('inf'):
			rv = 0
		else:
			rv = -min_curvature*tv/5 #*sign  # rv/tv = curvature, so rv = min_curvature*tv, and tv is fixed and defined above.
		

		print("rv %f" %rv)
		

		cmd_vel_pub_msg.linear.x = tv
		cmd_vel_pub_msg.angular.z = rv	
		self.cmd_vel_pub.publish(cmd_vel_pub_msg)

		# rate.sleep()

		ranges_plot.append(min(ranges))
		rv_plot.append(rv)


		# if (rospy.Time.now() - start).to_sec() >100:
		# 	print("HELLLLOOOO")
		# 	plt.plot(np.arange(len(ranges_plot)), ranges_plot)
		# 	plt.xlabel('sonar scan index')
		# 	plt.ylabel('minimum range')
		# 	plt.draw()
		# 	plt.show()
		# 	plt.plot(np.arange(len(rv_plot)), rv_plot)
		# 	plt.xlabel('rv instance')
		# 	plt.ylabel('rv')
		# 	plt.draw()
		# 	plt.show()
	    #     # plt.pause(0.001)
		return

		
		
		# print(data.ranges[1])

		# min_range = min(ranges)
		# print("minimum range: %f", min_range)

		# if min_range< 1:
		# 	curvature = -1/min_range
		# 	if curvature<-1:
		# 		curvature  = -1
		# 	if curvature >1:
		# 		curvature = 1
		# 	linear_velocity = 0.5 # Adjust the linear velocity as needed
		# 	angular_velocity = curvature * linear_velocity
		# 	# Publish the Twist message to control the robot's velocity and direction

		# 	cmd_vel = Twist()
		# 	cmd_vel.linear.x = linear_velocity
		# 	cmd_vel.angular.z = angular_velocity
		# 	self.cmd_vel_pub.publish(cmd_vel)

		# else:
		# 	cmd_vel = Twist()
		# 	cmd_vel.linear.x = 1.0
		# 	self.cmd_vel_pub.publish(cmd_vel)	


if __name__ == "__main__":
	print('Starting navigation by curvature velocity method')

	rospy.init_node('isurp_CVM', anonymous=True)
	start = rospy.Time.now()
	print(start.to_sec())
	rate = rospy.Rate(3)
	obstacle_on = False

	try:
		avoidance = curvature_velocity_method()
		np.savetxt('cvm_plot.txt', ranges_plot)
		
		
		rospy.spin()
	except rospy.ROSInterruptException:
		print('caught ROSInterruptException')





"""
SAMPLE LASERSCAN DATA PUBLISHED ON THE TOPIC - /rexrov2/sonar_p900
header: 
  seq: 8
  stamp: 
    secs: 94
    nsecs:   3000000
  frame_id: "sonar_link"
angle_min: -0.7853999733924866
angle_max: 0.7853999733924866
angle_increment: 0.003073972649872303
time_increment: 0.0
scan_time: 0.0
range_min: 1.0
range_max: 100.0
ranges: [98.11670684814453, 98.05255126953125, 98.07433319091797, 98.12045288085938, 98.26567840576172, 98.45110321044922, 98.69129943847656, 98.9432601928711, 99.32210540771484, 99.78234100341797, inf, inf, 79.85543060302734, 78.87003326416016, 80.528564453125, inf, inf, inf, inf, inf, inf, 42.19253158569336, 40.22243118286133, 39.88397216796875, 40.26454544067383, 13.58920669555664, 13.050414085388184, 12.76253890991211, 12.550019264221191, 12.464275360107422, 12.475377082824707, 12.506279945373535, 12.645805358886719, 12.895563125610352, 13.286386489868164, 14.292241096496582, 39.920013427734375, 39.973758697509766, 40.86155700683594, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 82.57723236083984, 83.02552032470703, 99.56649017333984, 99.15323638916016, 98.85286712646484, 98.56851196289062, 98.37638092041016, 98.23138427734375, 98.13385772705078, 98.05582427978516, 98.08622741699219, 99.41613006591797, 99.5224609375, 99.55911254882812, 99.58402252197266, 99.6461410522461, 99.74366760253906, 99.70199584960938, 99.83453369140625, 99.83988189697266, 99.92805480957031, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 80.57186126708984, 80.10442352294922, 79.65294647216797, 79.4368667602539, 79.2427978515625, 79.08828735351562, 79.0102767944336, 78.96781921386719, 78.90198516845703, 78.86524963378906, 78.88568115234375, 78.91180419921875, 78.95683288574219, 79.10455322265625, 79.13115692138672, 79.3327407836914, 79.56885528564453, 79.7725830078125, 80.23817443847656, 81.12080383300781, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 41.82480239868164, 41.38541030883789, 41.149024963378906, 40.95753479003906, 40.75886917114258, 40.66035461425781, 40.41786193847656, 40.3440055847168, 40.269081115722656, 40.172874450683594, 40.11488723754883, 40.084415435791016, 40.01993942260742, 40.01704788208008, 39.92184829711914, 39.90833282470703, 39.97282028198242, 39.90285110473633, 39.92556381225586, 39.92477798461914, 39.847450256347656, 39.899959564208984, 39.89344024658203, 39.97114181518555, 39.99612045288086, 40.065311431884766, 40.11342239379883, 40.186492919921875, 40.20499038696289, 40.29130172729492, 40.41519546508789, 40.50400161743164, 40.581642150878906, 14.416766166687012, 14.151524543762207, 13.947953224182129, 13.86994743347168, 13.770745277404785, 13.615867614746094, 13.589983940124512, 13.50905704498291, 13.445150375366211, 13.380276679992676, 13.362608909606934, 13.190072059631348, 13.183295249938965, 13.163524627685547, 13.096171379089355, 13.10986042022705, 13.043474197387695, 12.963071823120117, 12.931504249572754, 12.930724143981934, 12.894937515258789, 12.841160774230957, 12.871026039123535, 12.765214920043945, 12.754542350769043, 12.763692855834961, 12.683334350585938, 12.685437202453613, 12.596532821655273, 12.722487449645996, 12.657953262329102, 12.635771751403809, 12.617414474487305, 12.584667205810547, 12.575401306152344, 12.543291091918945, 12.571818351745605, 12.472501754760742, 12.482169151306152, 12.534337997436523, 12.504388809204102, 12.498235702514648, 12.475970268249512, 12.533224105834961, 12.479337692260742, 12.444162368774414, 12.432512283325195, 12.44942569732666, 12.482244491577148, 12.445308685302734, 12.48066520690918, 12.484889030456543, 12.434160232543945, 12.480779647827148, 12.382875442504883, 12.437614440917969, 12.432723999023438, 12.439001083374023, 12.473464012145996, 12.49821662902832, 12.479920387268066, 12.480778694152832, 12.496024131774902, 12.503979682922363, 12.462869644165039, 12.478886604309082, 12.542047500610352, 12.514683723449707, 12.518257141113281, 12.571581840515137, 12.534286499023438, 12.562957763671875, 12.533246994018555, 12.613541603088379, 12.554849624633789, 12.598466873168945, 12.65489387512207, 12.617276191711426, 12.687556266784668, 12.730023384094238, 12.76103687286377, 12.756300926208496, 12.787511825561523, 12.866997718811035, 12.859526634216309, 12.91518497467041, 12.867108345031738, 12.982020378112793, 12.959413528442383, 13.020621299743652, 13.045384407043457, 13.12209701538086, 13.165184020996094, 13.240767478942871, 13.236074447631836, 13.269888877868652, 13.33306884765625, 13.40305233001709, 13.505982398986816, 13.554341316223145, 13.63418197631836, 13.747247695922852, 13.799299240112305, 13.951354026794434, 14.034581184387207, 14.260526657104492, 14.624175071716309, 40.449920654296875, 40.31800842285156, 40.295345306396484, 40.17343521118164, 40.11965560913086, 40.0399169921875, 40.03978729248047, 40.000240325927734, 39.94499206542969, 39.90130615234375, 39.92365646362305, 39.887725830078125, 39.868045806884766, 39.87443161010742, 39.895721435546875, 39.940948486328125, 39.913719177246094, 39.97636795043945, 40.01420974731445, 40.06727600097656, 40.13602828979492, 40.20771408081055, 40.30426025390625, 40.33425521850586, 40.4810791015625, 40.5503044128418, 40.685523986816406, 40.818878173828125, 41.03329086303711, 41.30067825317383, 41.537498474121094, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 83.86322784423828, 83.50436401367188, 83.23494720458984, 82.97467041015625, 82.82425689697266, 82.71244812011719, 82.54902648925781, 82.56254577636719, 82.55542755126953, 82.53076934814453, 82.53695678710938, 82.5867691040039, 82.66697692871094, 82.84362030029297, 82.98804473876953, 83.1938247680664, 83.45027160644531, 83.92156982421875, 84.87899780273438, 99.7408447265625, 99.61947631835938, 99.58071899414062, 99.52767181396484, 99.50840759277344, 99.46293640136719, 99.41641998291016, 99.3451156616211, 99.32135009765625, 99.22842407226562, 99.21813201904297, 99.1588134765625, 99.15074920654297, 99.0798568725586, 98.98849487304688, 98.98834991455078, 98.93069458007812, 98.8970718383789, 98.87564086914062, 98.83003997802734, 98.74565124511719, 98.78907775878906, 98.71753692626953, 98.69742584228516, 98.6177749633789, 98.60675048828125, 98.57984924316406, 98.55982208251953, 98.53510284423828, 98.51203155517578, 98.46067810058594, 98.41942596435547, 98.37648010253906, 98.39308166503906, 98.36067199707031, 98.28352355957031, 98.32424926757812, 98.29598236083984, 98.31388092041016, 98.22661590576172, 98.23711395263672, 98.21550750732422, 98.19093322753906, 98.19856262207031, 98.16452026367188, 98.13453674316406, 98.1576919555664, 98.1314468383789, 98.14215087890625, 98.14471435546875, 98.1597900390625, 98.11221313476562, 98.04598999023438, 98.11612701416016, 98.06269073486328, 98.06303405761719, 98.09501647949219, 98.0553207397461, 98.0964126586914, 98.09729766845703, 98.06932830810547, 98.08950805664062]
intensities: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

"""


"""
#!/usr/bin/env python

import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class curvature_velocity_method:
    def __init__(self):
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.range_subscriber = rospy.Subscriber('/rexrov2/sonar_p900', LaserScan, self.range_callback)

    def range_callback(self, data):
        ranges = data.ranges
        angle_min = -0.7853999733924866
        angle_max = 0.7853999733924866
        angle_increment = 0.003073972649872303

        min_range = min(ranges)

        if min_range < 1:
            curvature = -1/min_range
            if curvature < -1:
                curvature = -1
            if curvature > 1:
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
    avoidance = curvature_velocity_method()
    rospy.spin()
"""