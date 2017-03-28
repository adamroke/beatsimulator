#!usr/bin/env python3

import random
from MidiFile3 import MIDIFile
import sys

letters = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def generateScale():
	scale = []
	nMax = -1
	while(nMax < 11):
		# Generate next note in scale
		note = random.randint(1,2)
		if nMax == 10: note = 1
		scale.append(nMax + note)
		nMax += note

	return scale

def noteToLetter(note):
	letters = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
	return letters[note]

def showScale(scale):
	"""Shows scale to user in letter form."""
	lScale = []
	for n in scale:
		lScale.append(noteToLetter(n))

	return lScale

def getExistingScale():
	"""Allows user to pick an existing scale."""
	scale = [5,6,7,9]

	return scale

def expandScale(scale, octaves):
	xScale = []
	for i in range(octaves):
		xScale += [x+(12*i) for x in scale]
	return xScale

# Get phrase details
#oLength = 20
#oTempo = 120
#oOctaves = 1
#minVel = 100
#maxVel = 127
#oKey = random.randint(0,5)
#oName = "808"
#pOfNote = 100
#minLength = 1
#maxLength = 5

oLength = sys.argv[1]
oTempo = sys.argv[2]
oOctaves = sys.argv[3]
minVel = 100
maxVel = 127
oKey = random.randint(0,5)
oName = sys.argv[4]
pOfNote = sys.argv[5]
minLength = 1
maxLength = sys.argv[6]

# Initialise MIDI file details
oFile = MIDIFile(1)
oFile.addTrackName(0, oLength, oName)
oFile.addTempo(0, oLength, oTempo)

# Generate scale or allow user to choose a scale
scale = getExistingScale()

# Expand scale to octave range
scale = expandScale(scale, oOctaves)

# Generate notes in phrase
cTime = 0.0
while(cTime < oLength):
	# Generate length of note
	nLength = (random.uniform(minLength, maxLength))

	# Generate pitch of note
	nPitch = 53 + oKey + random.choice(scale)

	# Generate velocity of note
	nVelocity = random.randint(minVel,maxVel)

	# Add note to track if it is selected to appear based on probability
	if random.randint(1,100) <= pOfNote: oFile.addNote(0,0,nPitch,cTime,nLength,nVelocity)

	cTime += nLength

binfile = open((oName+".mid"), 'wb')
oFile.writeFile(binfile)
binfile.close()

# Tell user that file has been created
print("File has been created as '" + oName + ".mid'!")
