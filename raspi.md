### February 20, 2018

##### Setting up raspi zero

  * Flash the raspbian image on a formatted sd card using etcher
  * In config.txt add dtoverlay=dwc2
  * In cmdline.txt add modules-load=dwc2,g_ether after rootwait.
  * Raspberry Pi Foundation is disabling SSH by default in Raspbian Pixel as a security precaution. So make a file named ssh without any extension
  * run ssh pi@raspberrypi.local 
  * pwd = raspberry

##### Solving new MAC address and new connection on every raspi boot

  * The host end of the link-local connection appears to get a random MAC each time, making a new Network Manager connection entry each time. 
  * Switching the Device in the Ethernet settings for the connection to just the device name, ejp0s26f7u1, stopped new ones from appearing.
  
##### Solving wifi connections

  * The ethernet with raspi zero doesnot connect
* In network, in edit connections, in the wired connection, in ipv4 settings change method to Shared to other computers.

##### Seeing devices connected to the router

 * USe nutty
 
       sudo apt-add-repository ppa:bablu-boy/nutty.0.1
       
       sudo apt-add-repository ppa:elementary-os/stable
     
       sudo apt-get update
     
       sudo apt-get install nutty
       
 * Remove nutty
 
       sudo apt-get remove nutty
       
       sudo apt-add-repository --remove ppa:bablu-boy/nutty.0.1 
       
#### Installin Real VNC

       sudo apt-get install realvnc-vnc-server
       run the command sudo raspi-config, navigate to Advanced Options > VNC and select Yes
     
#### Adding wifi to raspi

* Check for connections
       
       sudo iwlist wlan0 scan
       
* edit the file wpa

       sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
       
* Add ssid and password

       network={
        ssid="testing"
        psk="testingPassword"
       }
       
* Add ssid with no password

       network={
        ssid="testing"
        key_mgmt=NONE
       }
       
 * Adding hidden networks
 
       network={
        ssid="yourHiddenSSID"
        scan_ssid=1
        psk="Your_wifi_password"
       }
       
 * Add priority
 
       priority = 1
       
 * reconfigure wlan
 
        wpa_cli -i wlan0 reconfigure
        
 * Check if successful
 
        ifconfig wlan0
        
#### Installing realvnc

		sudo apt-get update
		sudo apt-get install realvnc-vnc-server
		sudo apt-get install realvnc-vnc-viewer
 
#### Problems
 
 * Adding
 		
 		iface default inet dhcp
 		
 	ethernet didnot show up
 
