import tty
import sys
import termios
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm.start(0)
DC=3
orig_settings=termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
x=0
while x!= chr(27):
	x=sys.stdin.read(1)[0]
	if(DC>=3):
		if(x=="D"):
			DC=DC+1
			if(DC>13):
				DC=13
			pwm.ChangeDutyCycle(DC)
		if(x=="A"):
			DC=DC-1
			if(DC<3):
				DC=3
			pwm.ChangeDutyCycle(DC)
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)

