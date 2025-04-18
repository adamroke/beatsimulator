To run the simulation, use the following three commands in order. (Note that the 808.vst and DRUMPAD.vst files are 64-bit macOS VST binaries. Please reach out if you want to get the Windows version)

./generateMIDI <.mp3 sample> 0

./render808 808.mid 1
./render808 Kck.mid 1
./render808 Hs.mid 1
./render808 Ot.mid 1

./808compile <.mp3 sample>

5 beats (and the 5 samples used as the input) generated as output test results (average of 34.168 seconds per beat) found in Sample Output/ folder on this repo. 
