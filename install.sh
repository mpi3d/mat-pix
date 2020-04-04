# !/bin/bash
clear
cd
sudo apt-get update -y
sudo apt-get upgrade -y
sudo pip install rpi_ws281x adafruit-circuitpython-neopixel
sudo bash -c 'echo "blacklist snd_bcm2835" >> /etc/modprobe.d/snd-blacklist.conf'
sudo reboot
