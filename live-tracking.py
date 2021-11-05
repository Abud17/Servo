#import jetson.inference
#import jetson.utils

#net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
#camera = jetson.utils.gstCamera(1280, 720, "/dev/video0")      # '/dev/video0' for V4L2
#display = jetson.utils.glDisplay()			#videoOutput("display://0") # 'my_video.mp4' for file

#while display.IsOpen():
#	img, width, height = camera.CaptureRGBA()
#	detections = net.Detect(img,width, height)
#	display.RenderOne(img, width, height)
#	display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
import jetson.inference
import jetson.utils
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.servo[0].angle = 80


net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file

while display.IsStreaming():
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
