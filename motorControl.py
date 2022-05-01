import RPi.GPIO as GPIO
from time import sleep, time

class Motor:

	def __init__(self):
		self.pwmFreq = 1000

	def shelfCall(self, targetShelf):
		if (targetShelf != currShelf):
			GPIO.output(DIR_PIN_1, True)
			GPIO.output(DIR_PIN_2, False)
			for duty in range (0, 101):
				pi_pwm.ChangeDutyCycle(duty)
				sensor.trackShelf()
				sleep(0.01)
			while (currShelf != targetShelf):
				sensor.trackShelf() # Placeholder
			for duty in range(100, -1, -1):
				pi_pwm.ChangeDutyCycle(duty)
				if (sensor.getDistance() <= finDist):
					GPIO.output(DIR_PIN_1, False)
					GPIO.output(DIR_PIN_2, False)
				sleep(0.01)
			GPIO.output(DIR_PIN_1, False)
			GPIO.output(DIR_PIN_2, False)
			

class UltraSonic:
	
	def __init__(self):
		self.calibrationDistance = 5
		# the previous measurement is used for determining if a shelf has gone by
		self.previousMeasurement = self.calibrationDistance



	# Calibrates the sensor for proper distance measurments
	def calibrate(self):
		knownDistance = self.calibrationDistance
		distanceAverage = 0
		
		# Compares known distance to average calibration distances
		# Creates a calibration constant based on this comparison
		for i in range(CALIBRATIONS):
			distance = self.getDistance()
			distanceAverage += distance
			sleep(CALIBRATION_DELAY)
			
		distanceAverage /= CALIBRATIONS
		correctionFactor = knownDistance / distanceAverage
		return(correctionFactor)
		
	# Finds the distance from the US sensor in cm
	def getDistance(self):

		GPIO.output(TRIG, GPIO.HIGH)
		sleep(TRIGGER_TIME)
		GPIO.output(TRIG, GPIO.LOW)
		
		while (GPIO.input(ECHO) == GPIO.LOW):
			start = time()
		while (GPIO.input(ECHO) == GPIO.HIGH):
			end = time()
			
		duration = end - start
		
		distance = duration * SPEED_OF_SOUND
		
		distance /= 2
		distance *= 100
		
		return distance
	
	def trackShelf(self):
		global currShelf
		distance = sensor.getDistance() * correctionFactor
		distance = round(distance, 4)
		difference = distance - sensor.previousMeasurement
		if (difference > 5):
			currShelf += 1
		sensor.previousMeasurement = distance
		print(distance)

########
# Main #
########
	
# constants
SETTLE_TIME = 2
CALIBRATIONS = 5

CALIBRATION_DELAY = 1

TRIGGER_TIME = 0.00001

SPEED_OF_SOUND = 343

# pin sets
GPIO.setmode(GPIO.BCM)

# pins
TRIG = 12
ECHO = 20
MOTOR_SIGNAL = 27
DIR_PIN_1 = 26
DIR_PIN_2 = 25

# pin setups
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setwarnings(False)			#disable warnings
GPIO.setup(MOTOR_SIGNAL,GPIO.OUT)
GPIO.setup(DIR_PIN_1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(DIR_PIN_2, GPIO.OUT, initial = GPIO.LOW)

sensor = UltraSonic()
correctionFactor = sensor.calibrate()
motor = Motor()
pi_pwm = GPIO.PWM(MOTOR_SIGNAL, 1000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 

currShelf = 1

finDist = sensor.calibrationDistance

sensor.calibrate()

motor.shelfCall(4)


