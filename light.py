import cv2 
from imutils.video import VideoStream
import imutils

from pynput.mouse import Button, Controller
mouse = Controller()
vs = VideoStream(src=0).start()

radius = 10

initX, initY = 0,0  # random initialization

# while True:
def tracking():
	global initX, initY
	cam = vs.read()
	cam = cv2.resize(cam, (1366,768))
	cam = cv2.flip(cam, 1)
	gray = cv2.cvtColor(cam, cv2.COLOR_BGR2GRAY)
	gray = cv2.blur(gray, (100,100))
	# gray = cv2.GaussianBlur(gray, (radius,radius), 100)
	(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
	cv2.circle(cam, maxLoc, radius, (0, 0, 0), 1)
	
	# sensitivity
	sensVal = 5 # +- 5
	xVal, yVal = maxLoc[0], maxLoc[1]
	if (xVal >= initX-sensVal) and (xVal <= initX+sensVal) and (yVal >= initY-sensVal) and (yVal <= initY+sensVal):
		if maxVal >= 220:
			return initX, initY
		else:
			return initX, initY
			# mouse.position = initX, initY # mouse movement function
	else:
		initX, initY = xVal, yVal
		return initX, initY
	# ends here

	# cv2.imshow('a', cv2.resize(cam, (700,500)))
	# if cv2.waitKey(1) == ord('q'):
		# break



def scraped():  # it was not working well
	import cv2 
	from imutils.video import VideoStream
	import imutils

	vs = VideoStream(src=0).start()

	radius = 15
	while True:
		cam = vs.read()
		cam = cv2.flip(cam, 1)
		gray = cv2.cvtColor(cam, cv2.COLOR_BGR2GRAY)
		# gray = cv2.blur(gray, (100,100))
		# gray = cv2.GaussianBlur(gray, (radius,radius), 100)
		# (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
		# cv2.circle(cam, maxLoc, radius, (0, 0, 0), 2)
		template=cv2.imread('track.jpg',0)
		template = imutils.resize(template, width=50)
		#result of template matching of object over an image
		result=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF)
		sin_val, max_val, min_loc, max_loc=cv2.minMaxLoc(result)

		top_left=max_loc
		#increasing the size of bounding rectangle by 50 pixels
		bottom_right=(top_left[0]+50,top_left[1]+50)
		cv2.rectangle(cam, top_left, bottom_right, (0,255,0),5)


		cv2.imshow('a', cam)
		if cv2.waitKey(1) == ord('q'):
			break
