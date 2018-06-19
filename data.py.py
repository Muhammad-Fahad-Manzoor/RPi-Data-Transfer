import subprocess
import time

def copyData():
        # Connect Device first with RPi and then sd card
        
        # Unmount and delete all sd* folders and EmbeddedSystem folder from Tool repo 
	print("Unmounting existing EmbeddedSystems")
	subprocess.call("cd /home/pi/Tool && sudo umount -f sd.* 2> /dev/null", shell=True)
	subprocess.call("cd /home/pi/Tool && sudo rmdir sd.* 2> /dev/null", shell=True)
	subprocess.call("cd /home/pi/Tool && sudo umount -f EmbeddedSystem 2> /dev/null", shell=True)
	subprocess.call("cd /home/pi/Tool && sudo rmdir EmbeddedSystem 2> /dev/null", shell=True)

	# Create folder in Tool repo with name EmbeddedSystem	
	print("Creating EmbeddedSystem root folder")
	subprocess.call("mkdir /home/pi/Tool/EmbeddedSystem 2> /dev/null", shell=True)

	# Mount sda1 folder in Tool/EmbeddedSystem folder
	print("Mounting EmbeddedSystem")
	subprocess.call("sudo mount /dev/sda1 /home/pi/Tool/EmbeddedSystem 2> /dev/null", shell=True)

	# Copy EmbeddedSystem folder to ARDUINOTEST folder
	print("Copying file into SD-Card")
	subprocess.call("sudo cp -r /home/pi/Tool/EmbeddedSystem /media/pi/ARDUINOTEST 2> /dev/null", shell=True)
	print("File has been copied...")
	
	# print("Unmounting EmbeddedSystem")
	# subprocess.call("cd /home/pi/Tool && sudo umount -f EmbeddedSystem 2> /dev/null", shell=True)
	# subprocess.call("cd /home/pi/Tool && sudo rmdir EmbeddedSystem 2> /dev/null", shell=True)
	# print("EmbeddedSystem is unmounted...")
	       

if __name__ == '__main__':
	print("Embedded tool is initiating...")
	# Delay for 2 seconds
	time.sleep(2)
	# Call copyData() function
	copyData()


