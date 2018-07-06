#### February 21, 2018

  * Install openssh-server and openssh-client to use ssh
  
  * For using real vnc server and disabling the encryption
  
        gsettings set org.gnome.Vino require-encryption false
        
#### March 7, 2018

* making a link so that it can be run from the terminal directly 

		Run "sudo ln -s /usr/local/android-studio/bin/studio.sh androidStudio" in /usr/local/bin
		
		androidStudio is the name of the link

#### 7zip

* Installing

		sudo apt-get install p7zip-full

* Running

		7z x PACKAGE.7z 
				
* DTRX

		sudo apt-get install dtrx
		dtrx archive.tar.XX

#### Starting VNC server

                systemctl start vncserver-x11-serviced.service #systemd
                /etc/init.d/vncserver-x11-serviced start #initd
                
#### Installing ubuntu 16.04 in Alienware Aurora R7

* https://medium.com/@FloodSung/tutorial-how-to-install-ubuntu-16-04-windows10-on-alienware-15-r3-91cd1dc7eb3c
                
* https://askubuntu.com/questions/832163/black-screen-when-loading-ubuntu-live-usb
                
* https://askubuntu.com/questions/716957/what-do-the-nomodeset-quiet-and-splash-kernel-parameters-mean

* https://medium.com/yanda/building-your-own-deep-learning-dream-machine-4f02ccdb0460
                
* sudo apt-get update not working
                
                sudo apt-get remove libappstream3
                
*

#### Starting vnc server in boot time

* https://stackoverflow.com/questions/7221757/run-automatically-program-on-startup-under-linux-ubuntu

* create a script named vnc.sh in /etc/init/d

		#!/bin/bash
		systemctl start vncserver-x11-serviced.service

* Then execute following commands

		sudo chmod +x /etc/init.d/filename 
		sudo update-rc.d filename defaults 
		
* There will be warning signs of insserv but they donot effect the script running

* another option - search for startup applications and add

		systemctl start vncserver-x11-serviced.service

* In /etc/rc.local add

		systemctl start vncserver-x11-serviced.service
		
* Using wifi before login,these are unprivileged actions. So login and go to wifi, select edit connections and select the ssid and edit it. Go to general and tick "All users may connect to this network"

#### No count down in grub for ubuntu

* https://askubuntu.com/questions/483729/how-to-remove-countdown-in-grub-menu-disable-countdown

* To get grub file in /etc/default/grub

		sudo apt-get install grub2 grub-pc
* Then run 

		sudo update-grub
		
* Now open /etc/default/grub using your favourite editor.
* And set this field to -1 to wait indefinitely!

		GRUB_TIMEOUT=-1
		
* comment out the following two lines to

		# GRUB_HIDDEN_TIMEOUT=0 
		# GRUB_HIDDEN_TIMEOUT_QUIET=true 
		
* Now again run 
		
		sudo update-grub

#### grub and dpkg error

		sudo dpkg-reconfigure grub-pc
		
* select the hard disk not the partition and click ok

#### The system doesnot login and it goes in a loop in login.

		Due to the dependency on third party drivers without disabling uefi secure boot
		
		So uefi secure boot should be disabled on boot up time. It comes it self at first time.

* Displaying the specifications of the computer in ubuntu

		sudo apt-get install lshw

		sudo lshw -html > mySpecs.html
