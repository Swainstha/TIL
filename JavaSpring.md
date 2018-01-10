## JAVA, Spring Boot

#### January 10, 2018

* Nosuchmethod Error
		
		The error generates when there are two versions of the same dependency in the project.So while building the build process may use one of the versions but during running time, the project may try to use another version. So if there is a condition that a function exists in one version but not the other but the project tries to call the function from the version where that function is not anymore then it gives Nosuch error method
		
		Example:
			com.squareup.okhttp3
		This dependency was in the project dependencies with version 3.4.0 and in one of the dependencies of the project as well with version 3.7.0. So we excluded the depenency  with version 3.7.0. In pom.xml file
		<dependency>
            		<groupId>
            			com.squareup.okhttp3
            		</groupId>
            		<artifactId>
            			okhttp
            		</artifactId>
            		<version>
            			3.7.0
            		</version>
            		<scope>
            			provided
            			</scope>
        	</dependency>
        	

* Adding jar files to maven

		URL-https://devcenter.heroku.com/articles/local-maven-dependencies
		
	* Make a folder named repo inside the project directory
	* The run the following command
		
			mvn deploy:deploy-file -Durl=file:///path/to/yourproject/repo/ -Dfile=mylib-1.0.jar -DgroupId=com.example -DartifactId=mylib -Dpackaging=jar -Dversion=1.0
			
	* Update the pom file with exactly the same words
	
			<repositories>
       <repository>
        			<id>project.local</id>
        			<name>project</name>
        			<url>file:${project.basedir}/repo</url>
    			</repository>
			</repositories>
			
	* Then add this
	
			<dependency>
    <groupId>com.example</groupId>
    <artifactId>mylib</artifactId>
    <version>1.0</version>
</dependency>

	* The add the repo to the git, commit it and upload to heroku if needed.
	* Make sure the group, artifact and version are same as the one mentioned in the the pom file of the respective jar.

