* Process to install google cloud sdk in your computer

	* install python2
	* Install pip
	
			sudo apt-get install pip2
			
	* Install virtualenv(It doesn't matter if you install it with Python 2 or Python 3)
	
			pip install --upgrade virtualenv
			
			virtualenv --python [python_version=python2/python3] [name of env]
			
			source [name of env]/bin/activate
			
	* Install google-cloud-storage
	
			pip install google-cloud-storage
			
	* Install Google cloud SDK
	
		* Download latest googe cloud sdk or use command
		
				curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-235.0.0-linux-x86_64.tar.gz
		
		* Extract the archive to any location
		
				tar zxvf [ARCHIVE_FILE] google-cloud-sdk
				
		* Setting the $PATH for the sdk
		
				./google-cloud-sdk/install.sh
				
		* Restart your terminal for the changes to take effect
		
		* Initialize sdk
		
			* Run the command
				
				
					gcloud init
						
	* Gcloud commands
	
		* To list accounts whose credentials are stored on the local system
					
				gcloud auth list
				
	
		* To list the properties in your active SDK configuration
		
				gcloud config list
				
		* To view information about your Cloud SDK installation and the active SDK configuration
		
				gcloud info
				
		* To view information about gcloud commands and other topics from the command line
		
				gcloud help
				
	* install the gcloud component that includes the App Engine extension for Python
	
			gcloud components install app-engine-python
			
	*  install the Extra Libraries component for Python, which includes the graphy and Django libraries
	
			gcloud components install app-engine-python-extras
			
	* Run the following command to update all the installed Google Cloud SDK components, including the App Engine extension for Python
	
			gcloud components update
			
	* To install the original local development server and the appcfg tooling, you can install the original App Engine SDK for Python
	
		* Download it
		
		* Unzip it
		
				unzip google_appengine_1.9.83.zip
				
		* Add the google_appengine directory to your PATH
		
				export PATH=$PATH:DIRECTORY_PATH/google_appengine/		
				
		* If the appcfg tool is not recognized then, run
		
				[SDK_INSTALL_PATH]/google-cloud-sdk/platform/google_appengine/appcfg.py -A [YOUR_PROJECT_ID] -V [YOUR_VERSION_ID] download_app [OUTPUT_DIR]
				
		* Only the authenticated user who deployed the version of the application as well as the users with the project Owner role have the privileges to download files. Other users who attempt to download the application will receive an error message
	
	* To list the project deployed in GCP
	
			gcloud projects list

	* To describe the project
	
			gcloud projects describe [project-id]