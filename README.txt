To run the simulation, use the following three commands in order. (Note that the 808.vst and DRUMPAD.vst files are 64-bit varieties and are MACOSX VST’s. Please contact me at aroke@uci.edu for Windows version)

./generateMIDI <.mp3 sample> 0

./render808 808.mid 1
./render808 Kck.mid 1
./render808 Hs.mid 1
./render808 Ot.mid 1

./808compile


The first program (./generateMIDI) relies on an internet connection, as the actual MIDI file generation occurs on a website which takes a series of parameters and outputs it in MIDI format, so make sure you are connected.