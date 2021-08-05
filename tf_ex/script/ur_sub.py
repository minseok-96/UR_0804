import sys
import rospy
import moveit_commander

rospy.init_node("test_ur", anonymous=True)
moveit_commander.roscpp_initialize(sys.argv)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

robot.get_group_names()

