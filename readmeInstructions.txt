Set the Pi Up as a USB OTG Gadget

Open a terminal on the Pi and follow this procedure:

Set the USB driver to dwc2
echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
1
echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
Enable the dwc2 driver
echo "dwc2" | sudo tee -a /etc/modules
1
echo "dwc2" | sudo tee -a /etc/modules
Enable the libcomposite driver
echo "libcomposite" | sudo tee -a /etc/modules
1
echo "libcomposite" | sudo tee -a /etc/modules
Enable the MIDI gadget
echo "g_midi" | sudo tee -a /etc/modules
1
echo "g_midi" | sudo tee -a /etc/modules
Create the configuration script:

Create the file
sudo touch /usr/bin/midi_over_usb
1
sudo touch /usr/bin/midi_over_usb
Make it executable
sudo chmod +x /usr/bin/midi_over_usb
1
sudo chmod +x /usr/bin/midi_over_usb
Edit it with Nano 
sudo nano /usr/bin/midi_over_usb
1
sudo nano /usr/bin/midi_over_usb

paste the following into the file, making edits to the product and manufacturer strings as required


############################# file starts here #######
cd /sys/kernel/config/usb_gadget/ 
mkdir -p midi_over_usb 
cd midi_over_usb 
echo 0x1d6b &gt; idVendor # Linux Foundation 
echo 0x0104 &gt; idProduct # Multifunction Composite Gadget 
echo 0x0100 &gt; bcdDevice # v1.0.0 
echo 0x0200 &gt; bcdUSB # USB2 
mkdir -p strings/0x409 
echo "fedcba9876543210" &gt; strings/0x409/serialnumber 
echo "Casio" &gt; strings/0x409/manufacturer 
echo "CASIO USB-MIDI" &gt; strings/0x409/product 
ls /sys/class/udc &gt; UDC

################## file ends here ########




download below packages:

mido
python-rtmidi
pygame

pip install mido
sudo apt-get install libasound2-dev
sudo apt-get install libjack-dev
pip install python-rtmidi

The following packages will be REMOVED:
  jackd jackd2 libjack-jackd2-0 qjackctl sc3-plugins-server sonic-pi
  sonic-pi-server supercollider-server
The following NEW packages will be installed:
  jackd1 libjack0 libzita-alsa-pcmi0 libzita-resampler1
0 upgraded, 4 newly installed, 8 to remove and 105 not upgraded.


-------------------------------------------------------
neopixel  led - WS2812B libraries installation:
Note - below library requires python to be set as default python on pi

sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka


-----------------------------------------------------------
Updating/setting default python on pi:
1. first list them

sudo update-alternatives --list python

2. Update the alternatives table to include both Python 2.7.x and Python 3.5.x. Make sure to substitute the versions of Python in the command below with the versions of your system, which you have noted in the first step. Notice we use only the first 2 digits of the version (i.e. we ignore the 3rd version number part)

sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2

The --install option take multiple arguments from which it will be able to create a symbolic link. The last argument specified is priority. That means, if no manual alternative selection is made the alternative with the highest priority number will be set.

3.Check the result. Type the following:
python --version

4. Similarly to above, you can also list the priorities table to confirm:

update-alternatives --list python

5. Switching default Python versions
If you have followed the guide above, you can from now on switch preferred Python versions anytime. Just invoke the command below and make your choice.
sudo update-alternatives --config python

6. Cleanup
One day, your Python version(s) will change. To remove an entry from the alternatives table, simply type something like this (we will remove the table entry for Python 3.5 in this example):

sudo update-alternatives --remove python /usr/bin/python3.5
----------------------------------------------------------------
Note : if you get ModuleNotFoundError while executing in sudo, then reinstall the module with sudo command




