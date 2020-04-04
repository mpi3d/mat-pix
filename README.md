# Mat Pix

Program in python to control a [8 leds neopixel](https://www.adafruit.com/product/1426).

[![Mat Pix](/mat_pix.jpg)](https://www.adafruit.com/product/1426)

# Install

``` sh
git clone https://github.com/MPi3D/Mat_Pix.git
cd Mat_Pix
chmod +x install.sh
sudo install.sh
```

# Program

+ [Program](/mat_pix.py)

# Usage

``` sh
sudo python mat_pix.py -S 255 255 255 # Set color of all leds to white.
sudo python mat_pix.py -c # Clear all leds.

sudo python mat_pix.py -s 0 255 0 0 # Set color of the first led to white.
sudo python mat_pix.py -b 50 # Set the brightness to 50%.
sudo python mat_pix.py -g 0 # Get color of the first led.

sudo python mat_pix.py -bl 5 10 0 255 0 # Blink 10 times to green with speed 5.
sudo python mat_pix.py -fa 10 5 0 0 255 # Fade 5 times to blue with speed 10.
sudo python mat_pix.py -ra 1 20 # Random 20 times with speed 1.
sudo python mat_pix.py -po 20 2 # Police twice with speed 20.

sudo python mat_pix.py -h # For more informations
```
