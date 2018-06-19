# RPi-Data-Transfer
This program provides Data transfer feature from embedded device to sd card attached with raspberry pi
  
# Development Environment
  * OS: Raspbian for Raspberry Pi
  * Libraries required: 
        Subprocess library of Python
        Time library

# How to use
  1. install the Python libraries.
  2. connect embedded device and SD card with RPI
  3. Make sure, device should under /home/pi/Tool and sd card under /media/pi/ARDUINOTEST
  3. change the current directory to where the file located.
  4. run the code with: 
     sudo python data.py