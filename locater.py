# I just wrote this here 
import pyautogui as pg
from time import time
import numpy as np
from debug import positionCheckv1
'''
	- The user has to start this application before beginning any tests -- not anymore

'''
t1 = 0
t2 = 0

def timer(state):
	global t1, t2
if state == True:
		t1 = time()
	elif state == False:
		t2 = time()
		timeElapsed = int(t2-t1)
		return timeElapsed

# if "exitthisReview" => The user is reviewing the test, maybe we won't need to do anything about this

def image():
	buttonLocation = pg.locateOnScreen("locateImg/khanAcad.png", confidence=0.9)

	if buttonLocation != None:
		# check for SAT test
		secondButton = pg.locateOnScreen("locateImg/collegeboard.png", confidence=0.9)
		print(buttonLocation)
		print(secondButton)

maxQuestions = 11 # make a box while working in GUI

# make a 2 dimensional array to store all the question & time data
qArray = [] # probably a String Array

for index in range(maxQuestions):
	q1= []
	for index2 in range(3): # quesNo, Choice, Time
		q1.append(0)
	qArray.append(q1)
# ends here
# print(qArray)

def QuestionModule(quesNo):
	timer(True) # start the timer
	global qArray
	qArray[quesNo][0] = str(quesNo+1)

	def writeArray(Choice, Time):
		qArray[quesNo][1] = str(Choice)
		qArray[quesNo][2] = Time

	state = False
	while state != True: # hold everything until options' position has been identified
		state = positionCheckv1()

	if state == True:
		print("question found:", quesNo+1)
		Done = False
		# wait for any options to be chosen
		while Done != True:
			names = ['locateImg/optA2.png','locateImg/optB2.png','locateImg/optC2.png','locateImg/optD2.png']
			
			if pg.locateOnScreen(names[0], confidence=0.999) != None:
				# user has chosen option A
				calcTime = timer(False)
				writeArray("A", calcTime)
				print(quesNo+1, "a")
				Done = True

			elif pg.locateOnScreen(names[1], confidence=0.999) != None:
				# user has chosen option B
				calcTime = timer(False)
				print(quesNo+1, "b")
				
				writeArray("B", calcTime)
				Done = True

			elif pg.locateOnScreen(names[2], confidence=0.999) != None:
				# user has chosen option C
				calcTime = timer(False)
				print(quesNo+1,"c")
				
				writeArray("C", calcTime)
				Done = True

			elif pg.locateOnScreen(names[3], confidence=0.999) != None:
				# user has chosne option D
				print(quesNo+1, "d")
				
				calcTime = timer(False)
				writeArray("D", calcTime)
				Done = True

			else:
				# undefined option, I don't know what to do here. Yet.
				None

while True:
	buttonLocation = pg.locateOnScreen("locateImg/khanAcad.png", confidence=0.9)
	if buttonLocation != None:
		print("found: Khan Academy")
		# the user is on khan Academy website		
		beginTestImg = pg.locateOnScreen("locateImg/testOnGoing.png", confidence=0.9)
		if beginTestImg != None:
			print("found: Test ongoing")
			for quesNo in range(maxQuestions): # this is a bit janky rigt now
				QuestionModule(quesNo)
				# break
			break

np.save("test.npy", qArray)
