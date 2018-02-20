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
