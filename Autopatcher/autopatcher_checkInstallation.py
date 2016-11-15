import numpy as np 

print "Testing environment of Autopatcher:"

name = []
result = []

###############################################
# print "Ckecking PyQt: ",
name.append("PyQt")

try:
	from PyQt4.QtCore import *
	from PyQt4.QtGui import *
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################

name.append("sys")

try:
	import sys
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("OpenCV & numpy")

try:
	import cv2
	import numpy
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("Camera")

try:
	import CameraWidget as cw
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("Autopatcher")

try:
	import autopatcher
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("Grid")

try:
	import Grid
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("Math & copy")

try:
	import math, copy
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("MSSInterface")

try:
	import MSSInterface
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("time & datatime")

try:
	import time, datetime
	from datetime import datetime
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("CSV")

try:
	import csv
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("ManipPatcherControl")

try:
	import ManipatcherControl
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("StoredCoordinates")

try:
	import StoredCoordinates
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("gc & os")

try:
	import gc, os
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("Computer Vision")

try:
	from ComputerVision import *
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################
name.append("Scipy Cluster")

try:
	from scipy.cluster.hierarchy import *
	cache = "OK"
except ImportError:
	cache = "FAILURE"

result.append(cache)
###############################################

for x in range(len(result)):
	print name[x],
	print " " * (30 - len(name[x])), 
	print result[x]