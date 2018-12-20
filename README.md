# How to install and configure screenly on a Raspberry Pi

1. Download the Screenly OSE disk image from github:

  https://github.com/Screenly/screenly-ose/releases/download/0.16/image_2018-11-23-Screenly-OSE-lite.zip

1. Unzip the disk image

1. Write the disk image to the SD card.  An easy way to do that is with Etcher:

  https://www.balena.io/etcher/

1. Create an empty file named 'ssh' at the top-level of the boot partition (the smallest partition on the SD card)

1. Connect the Pi to a TV or computer monitor and power on the Pi

1. An SSID and password will be displayed on the screen.  Connect to it.

1. Open a browser and go to the web page displayed on the screen to configure wifi.  Configure it to connect to your network.

1. The Pi reboots and displays its ip address on the screen

1. SSH into the Pi using its ip address (user: pi, pw: raspberry).  If you're on Windows and don't have an SSH client installed, putty is available here:

  https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

1. Change the password for the pi account

  $ passwd

1. Switch to the root account

  $ sudo su root

1. Change the password for the root account

  # passwd

1. Install the python 'requests' module

  # pip install requests

1. [Optional] Configure the locale

  # raspi-config

1. Exit 

  # exit
  $ exit

1. Add content to screenly using a web browser, using the ip address that is displayed when the Pi boots

# Using physical buttons with the Pi

1. ssh into the Pi

1. Clone Kevin's python scripts

  $ git clone git@github.com:frankdeath/screenly-python.git

1. Manually run the button script

  $ cd screenly-python
  $ ./buttons.py


