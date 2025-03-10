import glob
import os
import shutil


#Just change directory on line 11 to cut frames

def getfilelist(f=None):
	"""Reads in meta data"""
	if (f==None):
		os.chdir(".")
		kin = []
		meta = []
		accel = []

		for file in glob.glob("kin_*.txt"):
			kin.append(file)
		for file in glob.glob("meta_*.txt"):
			meta.append(file)
		for file in glob.glob("accel_*.txt"):
			accel.append(file)

	#print "Kin is: "+str(kin)
	#print "Meta is: "+str(meta)
	return (kin,meta,accel)


def framecut(f,easy=None):
	if (easy==1):
		SCUT =0;
		FCUT =30;
		print "Running In easy mode, cleaning up 40 frames..."
	else:
		SCUT = 50;
		FCUT = 50;
		print "Running In hard mode, cleaning up 200 frames..."
	#FCUT = 150;
	"""cut out beginning and end frames"""

	kindata = open(f[0],'r')
	lines = kindata.readlines()
	kindata.close()
	flength = len(lines)
	print "Original Frame Count: ",flength
	lines = lines[SCUT:(flength-FCUT)]
	# lines = lines[FCUT::]
	flength = len(lines)
	print "Cleaned Frame Count: ",flength
	kindata = open(f[0],'w')
	for line in lines:
		kindata.write(line);
	kindata.close


if __name__ == '__main__':
	print  "Cleaning Kinect Frame Data...."
	kin,meta,accel = getfilelist()
	framecut(kin,0)