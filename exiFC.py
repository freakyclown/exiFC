#!/usr/bin/python
# exiFC (exif see)
# created and maintained by Freakyclown
# Distributed under dbad http://www.dbad-license.org/

import FCExifTags
import Image
import os
import sys
colourstart = "\033[94m" # dark blue
colourend = "\033[0m" # white (this is default)

def is_jpeg(filename):
    	data = open(filename,'rb').read(2)
	if data[:2] != '\xff\xd8': return False
    	return True
    	
def singleimage(image):
	file = image
        print "file://"+os.getcwd()+"/"+file, ""
	if is_jpeg(file) == True:
	        im = Image.open(file)
	        exif(im)
	else:
		print "Not a valid jpeg!"


def usecolour(val):
        global colourstart
        global colourend
        if not val:
                colourstart = ""
                colourend = ""

def version():
	print "FCExifTags version V1.00"
# grab each exif tag from my exif tags module do this for every tag

def exif(im):
 	try:
		exif = im._getexif()
		for i in exif.keys():
				try:
					print colourstart,FCExifTags.TAGS[i], exif[i],colourend
				except:
				 	pass 	

	except:
		print "no exif"
		
try:
  singleimage(sys.argv[1])
except:
	print "usage python exiFC.py imagetoinspect.jpg"
