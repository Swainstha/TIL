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

		
