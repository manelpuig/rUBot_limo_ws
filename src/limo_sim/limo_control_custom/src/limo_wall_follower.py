#! /usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class WallFollower:
    def __init__(self):
        rospy.init_node('wall_follower')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.clbk_laser)
        rospy.on_shutdown(self.shutdown)
        self.rate = rospy.Rate(25)

        self.d = rospy.get_param("~distance_laser")
        self.vx = rospy.get_param("~forward_speed")
        self.wz = rospy.get_param("~rotation_speed")
        self.vf = rospy.get_param("~speed_factor")  # No s'utilitza en el codi original, però es manté per consistència.

        self.is_scan_ranges_length_correction_factor_calculated = False
        self.scan_ranges_length_correction_factor = 2

    def clbk_laser(self, msg):
        if not self.is_scan_ranges_length_correction_factor_calculated:
            self.scan_ranges_length_correction_factor = len(msg.ranges) / 360
            self.is_scan_ranges_length_correction_factor_calculated = True
            print("Lidar_Factor= " + str(self.scan_ranges_length_correction_factor))

        bright_min = int(250 * self.scan_ranges_length_correction_factor)
        bright_max = int(270 * self.scan_ranges_length_correction_factor)
        right_min = int(270 * self.scan_ranges_length_correction_factor)
        right_max = int(300 * self.scan_ranges_length_correction_factor)
        fright_min = int(300 * self.scan_ranges_length_correction_factor)
        fright_max = int(330 * self.scan_ranges_length_correction_factor)
        front_min = int(330 * self.scan_ranges_length_correction_factor)
        front_max = int(360 * self.scan_ranges_length_correction_factor)

        regions = {
            'bright': min(min(msg.ranges[bright_min:bright_max]), 3),
            'right': min(min(msg.ranges[right_min:right_max]), 3),
            'fright': min(min(msg.ranges[fright_min:fright_max]), 3),
            'front': min(min(msg.ranges[front_min:front_max]), 3),
        }

        self.take_action(regions)

    def take_action(self, regions):
        msg = Twist()
        linear_x = 0
        angular_z = 0

        state_description = ''

        if regions['front'] > self.d and regions['fright'] > 2 * self.d and regions['right'] > 2 * self.d and regions['bright'] > 2 * self.d:
            state_description = 'case 1 - nothing'
            linear_x = self.vx
            angular_z = 0
        elif regions['front'] < self.d:
            state_description = 'case 2 - front'
            linear_x = 0
            angular_z = self.wz
        elif regions['fright'] < self.d:
            state_description = 'case 3 - fright'
            linear_x = 0
            angular_z = self.wz
        elif regions['front'] > self.d and regions['right'] < self.d:
            state_description = 'case 4 - right'
            linear_x = self.vx
            angular_z = 0
        elif regions['bright'] < self.d:
            state_description = 'case 5 - bright'
            linear_x = 0
            angular_z = -self.wz
        else:
            state_description = 'case 6 - Far'
            linear_x = self.vx
            angular_z = -self.wz

        rospy.loginfo(state_description)
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        self.pub.publish(msg)
        self.rate.sleep()

    def shutdown(self):
        msg = Twist()
        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z = 0
        self.pub.publish(msg)
        rospy.loginfo("Stop rUBot")


if __name__ == '__main__':
    try:
        wall_follower = WallFollower()
        rospy.spin()  # Manté el node en funcionament fins que es rep una interrupció (Ctrl+C).
    except rospy.ROSInterruptException:
        pass # El 'pass' aquí fa que el programa finalitzi sense errors quan es rep Ctrl+C.  El shutdown s'encarrega de parar el robot.