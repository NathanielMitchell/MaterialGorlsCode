import RPi.GPIO as GPIO
from time import sleep

class Motor:

	def __init__(self):
		self.pwmFreq = 1000

	def shelfCall(self, targetShelf, currShelf):
		if (targetShelf != currShelf):
			GPIO.output(dirPin1, True)
			GPIO.output(dirPin2, False)
			for duty in range (0, 101):
				pi_pwm.ChangeDutyCycle(duty)
				sleep(0.01)
			while (currShelf != targetShelf):
				sensor.trackShelf() # Placeholder
				currShelf = "Whatever the current shelf on the rest of the code is"
			while (sensor.getDistance > "stopPoint"):
				duty = (100/"totDIst") * ("currDist - finDist")
				if (duty > 0):
					pi_pwm.ChangeDutyCycle(duty)
				elif ("currDist <= finDist"):
					pi_pwm.ChangeDutyCycle(0)
			GPIO.output(dirPin1, False)
			GPIO.output(dirPin2, False)
			

		
		





motorSignal = 13
dirPin1 = 16
dirPin2 = 17# PWM pin connected to LED
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BCM)		#set pin numbering system
GPIO.setup(motorSignal,GPIO.OUT)
GPIO.setup(dirPin1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(dirPin2, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(dirPin1, True)
GPIO.output(dirPin2, False)
pi_pwm = GPIO.PWM(motorSignal,1000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 
while True:
    for duty in range(0,101,1):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        sleep(0.01)
    sleep(0.5)
    
    for duty in range(100,-1,-1):
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.5)