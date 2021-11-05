#Importieren Servomotor Treiber Bib
import adafruit_pca9685
import jetson.inference
import jetson.utils



pwm = adafruit_pca9685.PCA9685
posX =90
pox = 45
speedX = 1
speedY = 2

ThresholdX = 20
ThresholdY = 10

def set_servo_pulse(channel, pulse):
    pulse_lenge = 1000000
    pulse_lenge //=60
    print('{0}us per period'.format(pulse_lenge))
    pulse_lenge //= 4096
    print('{0}us per bit'.format(pulse_lenge))
    pulse *= 1000
    pwm.set_pwm(channel, 0, pulse)

pwm.set_pwm_freq(60)    



#Einfach Programm für Steuerung die Servomotoren
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.servo[0].angle = 100

#kit.servo[1].angle = 0


#start TCP 
#server_TCP = socketserver.TCPServer(("192.168.178.48",8070), TCPServerRequest)
#th = Threading.Thread(target = server_TCP.server_forever)
#th.daemon = True
#th.start()

#server_HTTP = ThreadedHTTPServer (("192.168.178.48",8090), VideoStreamHandler)
#th2 = threading.Thread(target=server_HTTP.server_forever)
#th2.daemon =  True
#th2.start()

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file

while display.IsStreaming():
	img = camera.Capture()
    

	#detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))



