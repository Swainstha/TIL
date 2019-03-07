* echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
	* sudo sysctl -p

* To not display the redux actions in production mode we edit the line in index.js file as

		const composeEnhancers = process.env.NODE_ENV==='development'? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__:null || compose;
		
	* The process is a global variable and we can access the environmental variable  ```NODE_ENV``` in ```config/env.js```
	
* We can use webpack to  manually build a react app on our own.

	* First we should use ```npm init``` in terminal. It will make a package.json and package-lock.json file. We should input our data or leave as it is accepting everything. Package.json indicates the entry or main file of the whole react app probably ```index.js```
	
	* Then we should use ```npm install``` to install all the node modules.
	
	* Then we should install ```react, react-dom and react-router-dom```.
	
			npm install --save react react-dom react-router-dom
			
		* if used ```npm install ---save-dev``` then it is a development only dependency, otherwise production dependency 
			
	* The we need to make a webpack file named as ```webpack.config.js``` and make a edit in ```package.json``` file as
	
			"scripts": {
    				"test": "test",
    				"start": "webpack-dev-server"
  			}
  			
  	* If we want to manage our extensions like a name with no extension is probably a js or jsx file then we should add  following in ```webpack.config.js```
  	
  			resolve: {
        			extensions: ['.js', '.jsx']
   			 }
   			 
   	* For handling different types of file types correctly, we should add ```module``` loaders in ```webpack.config.js```.
   	
   			module: {
        			rules:[{
                			test: /\.js$/,
                			loader: 'babel-loader',
                			exclude: /node_modules/
            			}]
    				}
    				
    	* If we need multiple loaders we use ```use``` instead of ```loader```.
    				
    	* The rules are in array.
    	* The test is the type of file with a regular expression. The ```.``` needs a escape character ```\```.
    	* The exclude contains the files or patterns to be excluded. it shouldn't try to transform anything in ```node_modules``` because they are already optimized and are third party libraries.
    	
    	* We can use the ```babel``` loader for javascript. It is the defacto standard for transpiling next generation javascript to current gen javascript.
    	
    			npm install --save-dev babel-loader babel-core babel-preset-react babel-preset-env
    			npm install --save-dev webpack-cli
    		
    		* The recent Babel upgrade to version 7 changed the namings of the node packages.For instance, now you have to install ```npm install --save-dev @babel/core @babel/preset-env``` and ```npm install --save-dev @babel/preset-react ```
    		to get it working with React. 
    			
    		* After install, the babel is not ready to use, we need to configure babel because the presets doesn't make Babel use them, it doesnot analyze all packages we installed and then see if there is a preset inside of them. So we make a file ```.babelrc`` which ```babel``` will automatically read if its in root folder.
    		
    		* Inside ```.babelrc``` we define the targets like which generation of browsers should support our app.
    		
    				{
    					"presets": [
       						 ["@babel/env", {
          						  "targets": {
                						"browsers": [
                   							 "> 1%",
                    							"last 2 versions"
                						]
            					}
        				}],
        				"@babel/react"
   					 ]
   					 "plugins": [
            "@babel/plugin-syntax-dynamic-import",
            "@babel/plugin-proposal-class-properties"   
        ]
   					 }
   					 
   		* For handling css files, we download
   		
   				npm install --save-dev css-loader style-loader
   				
   			* ```css-loader``` tells webpack what to do with these ```.css imports``` and ```style-loader``` which will then extract the css code from the css files and inject at the top of our html file hence reducing the amount of file downloads we have to make.
   			
   			* css loaders
   			
   						{
                			test: /\.css$/,
                			exclude: /node_modules/,
                			use: [
                    				{loader: 'style-loader'},
                    				{
                    					loader: 'css-loader',
                        				options: {
                        					importLoaders: 1,
                           			 		modules: true,
                           					localIdentName: '[name]__[local]__[hash:base64:5]'
                        				}
                        			}

                			]
            			}

			* The loader loads from bottom to top, so first the css-loader is loaded then only the style-loader. ```importLoaders: 1``` tells that there is one loader that is ```postcss-loader``` to be loaded before it.
			
			* Now install postcss loaders
			
					npm install --save-dev postcss-loader
					
					npm install --save-dev autoprefixer
					
			* ```postcss-loader``` actually runs before ```css-loader``` and dives into the css file and adjust our code before ```css-loader``` pulls it out and adjusts the classnames
			
					{
                		test: /\.css$/,
                		exclude: /node_modules/,
                		use: [
                    			{ loader: 'style-loader' },
                    			{
                       				 loader: 'css-loader',
                        			options: {
                           				importLoaders: 1,
                            			modules: true,
                            			localIdentName: '[name]__[local]__[hash:base64:5]'
                        			}
                    			}, 
                    			{
                       				 loader: 'postcss-loader',
                        			options: {
                            				ident: 'postcss',
                            				plugins: () => [
                                				autoprefixer({
                                   					 browsers: [
                                        					"> 1%",
                                        					"last 2 versions"
                                    					]
                                				})
                            				]
                       				 }
                    			}
                		]
            		}
  
 		* For handling image types
 		
 				 npm install --save-dev url-loader
 				 
 			* For file types which copies the image in a particular folder and gives a link to it.
 			
 					npm install --save-dev file-loader
 					
 			* The url loader checks the size of the image if it below a certain limit. If it is, then it will convert them into data64 urls which it can inline in our documents, so we dont have to download that extra file. For biggers files that would be inefficent so if the files exceed the limit the ```file-loader``` copies the images into a output folder and provides the links for them and put that into the imports in our components.
 			
 					{
               			test: /\.(png|jpe?g|gif)$/,
                		loader: 'url-loader?limit=8000&name=images/[name].[ext]'
           			 }
           			 
           		* Limit is in bytes and name is the output folder t store the bigger images.
           
 	* Some additions 
 	
 			npm install --save-dev  @babel/plugin-proposal-class-properties
 			npm install --save-dev @babel/plugin-syntax-dynamic-import
 			npm install --save-dev @babel/preset-stage-2 this is unsupported by babel now
 			
 			
 	* To connect index.html,we install
 	
 			npm install --save-dev html-webpack-plugin
 			
 	* Add plugins in ```webpack.conf.js```
 	
 			plugins :  [
        		new HtmlWebpackPlugin({
            		template: __dirname + '/src/index.html',
            		filename: 'index.html',
           			inject: 'body'
        		}),
        		new webpack.optimize.UglifyJsPlugin()  to optimize the bundle.js file after build but  has been changed.
    		]
    		
    	* For production workflow make a new file named ```webpack.prod.config.js  ``` and copy everything from ```webpack.config.js``` and add ```"build": "webpack --config webpack.prod.config.js --progress -profile --color"``` in scripts of package.json.
    	
    	* Also install  the following to delete any component in the project folder
    	
    			npm install --save-de rimraf
    			
    	* so we delete the dist folder before building our app using ```npm run build``` by 
    	```"build": " rimraf dist && webpack --config webpack.prod.config.js --progress -profile --color"```
    	
    	* webpack-optimize was depreciated . instead use
    	
    			npm install uglifyjs-webpack-plugin --save-dev
    			
    	* In ```webpack.prod.config.js``` file, add in plugins the following thing.
    	
    			new UglifyJsPlugin({
					uglifyOptions: {
						warnings: false,
						ie8: false,
						output: {
							comments: false
						}
					}
				})	