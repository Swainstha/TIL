* echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
	* sudo sysctl -p

* To not display the redux actions in production mode we edit the line in index.js file as

		const composeEnhancers = process.env.NODE_ENV==='development'? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__:null || compose;
		
	* The process is a global variable and we can access the environmental variable  NODE_ENV in config/env.js