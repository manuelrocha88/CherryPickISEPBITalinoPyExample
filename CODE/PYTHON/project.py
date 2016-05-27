import numpy
#Set bitalino Library. Can get it from github:
#https://github.com/BITalinoWorld/python-api ( http://bit.ly/BITalinoPyAPI )
import bitalino

#Set BITalino Mac Address
#macAddress = "20-15-12-22-97-57";

#If you have Apple Operating System Mac OS
#you have to use the virtual port instead
#run terminal command ls /dev/tty.*
#in order to check what is the
macAddress = "/dev/tty.BITalino-97-57-DevB"

#instanciate
device = bitalino.BITalino(macAddress)

# Read BITalino version
BITversion = device.version()
print "BITalino Version: ", BITversion

# Check if we are using version 1 or 2 of BITalino board
print "BITalino type: ", "2" if device.isBitalino2 else "1"

device.start(1000,[1])

i = 0

while i<100:
    try:
        dataAcquired = device.read(100)
        EMG = dataAcquired[-1, :]
        value = numpy.mean(abs(EMG - numpy.mean(EMG)))
        print "v = ", value

        if value > 150:
            device.trigger([0, 1])
        else:
            device.trigger([0, 0])

        i = i + 1
    except KeyboardInterrupt:
        break

device.close()


