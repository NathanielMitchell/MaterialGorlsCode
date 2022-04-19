#################################################################
# Name: Nathaniel Mitchell
# Date: 11/17/2021
# Description: Collects distances with US sensor and then sorts.
#################################################################

# imports
import RPi.GPIO as GPIO
from time import sleep, time


class UltraSonic:
	
	def __init__(self):
		self.calibrationDistance = 10
		# the previous measurement is used for determining if a shelf has gone by
		self.previousMeasurement = self.calibrationDistance



	# Calibrates the sensor for proper distance measurments
	def calibrate(self):
		print("Calibrating...")
		print("Place the sensor a known distance away from am object")
		knownDistance = self.calibrationDistance
		print("Getting calibration measurements")
		print("Done.")
		distanceAverage = 0
		
		# Compares known distance to average calibration distances
		# Creates a calibration constant based on this comparison
		for i in range(CALIBRATIONS):
			distance = self.getDistance()
			distanceAverage += distance
			sleep(CALIBRATION_DELAY)
			
		distanceAverage /= CALIBRATIONS
		
		print(f"Average distance is {distanceAverage}")
		
		correctionFactor = knownDistance / distanceAverage
		
		print(f"Correction factor is {correctionFactor}")
		print("")
		
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

# pin setups
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

sensor = UltraSonic()



# Allowing for the sensor to remain off for two seconds
print(f"Waiting for sensor to settle ({SETTLE_TIME}s)")
GPIO.output(TRIG, GPIO.LOW)
sleep(SETTLE_TIME)

# Sets the calibration factor in main
correctionFactor = sensor.calibrate()
 
# Finds distances based on user input and then stores the distances in a list

distanceList = []


while (True):
	distance = sensor.getDistance() * correctionFactor
	sleep(0.2)

	distance = round(distance, 4)
	difference = distance - sensor.previousMeasurement
	if (difference > 2):
		print("there is a new shelf")

	print(distance)
	sensor.previousMeasurement = distance

"""So, i pulled a lot of this straight from the old pi assignment, but i made it more object oriented.
The idea in my head is that the ultrasonic sensor is able to do everything that the ir sensor could do also.
The sensor will basically have a set callibration distance in the end 
(the distance that we know the shelf will set from the sensor)
and so the sensor, when the shelves are supposed to start moving, checks the distance on a certain interval
and then if the difference between two measurments is big enough, then the system will know that a shelf has gone by
and we can track which shelf is where with this"""
