### Problems

* java.lang.RuntimeException: Can't create handler inside thread that has not called Looper.prepare()

	* This problem came when running toast messaging in worker thread i.e. async task.
	
	* You need to call Toast.makeText() (and most other functions dealing with the UI) from within the main thread
	
	* You could also use Activity.runOnUiThread().
	
	* Using handlers
	
		* Handler is part of the Android system's framework for managing threads.
		
*  Error inflating class android.support.design.widget.BottomNavigationView

		Caused by: android.content.res.Resources$NotFoundException: Resource ID
		
		Some of the resources were in drawable-v24 only. Copy those resources to drawable folder also.
