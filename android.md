### Problems

* java.lang.RuntimeException: Can't create handler inside thread that has not called Looper.prepare()

	* This problem came when running toast messaging in worker thread i.e. async task.
	
	* You need to call Toast.makeText() (and most other functions dealing with the UI) from within the main thread
	
	* You could also use Activity.runOnUiThread().
	
	* Using handlers
	
		* Handler is part of the Android system's framework for managing threads.