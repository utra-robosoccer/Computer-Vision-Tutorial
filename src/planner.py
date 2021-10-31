import rospy
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()
command_pub = rospy.Publisher("motor_commands", String)

def is_yellow(val):
  return val > 100

def plan(left, right):
  command = "STOP"
  if is_yellow(left) and is_yellow(right):
    command = "GO"
  if is_yellow(left) and not is_yellow(right):
    command = "LEFT"
  if not is_yellow(left) and is_yellow(right):
    command = "RIGHT"
  print(left, right, command)
  
  command_pub.publish(command)
  
  return command

def imgCallback(data):
  cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
  # width 800, height 800
  
  gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
  
  command = plan(gray_image[700][300], gray_image[700][500])
  
  gray_image = cv2.line(gray_image, (300,700), (500, 700), 0, 5)
  if command == "LEFT":
    gray_image = cv2.circle(gray_image, (300, 700), 5, 255, 2)
  if command == "RIGHT":
    gray_image = cv2.circle(gray_image, (500, 700), 5, 255, 2)
  if command == "GO":
    gray_image = cv2.circle(gray_image, (400, 700), 5, 255, 2)
  
  cv2.imshow("Raw Image", gray_image)
  cv2.waitKey(3)


def main():
  print("Hey Hey Universe!")
  rospy.init_node('my_planner_node')
  img_sub = rospy.Subscriber("/camera/image_raw", Image, imgCallback)
  rospy.spin()

if __name__ == "__main__":
  main()

