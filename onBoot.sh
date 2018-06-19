#!/bin/sh

# Go to nano /etc/profile and change the path and if permission denied then change the mode of profile to 777

sleep 5
cd /home/pi/Data_Transfer_Function
sudo python data.py 1> /dev/null &
exit 0
cd /
