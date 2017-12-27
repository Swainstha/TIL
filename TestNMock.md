## December  26, 2017


#### Test Driven Development


**Naming Convention**

> * Have two source directories. Implementation code should be located in src/main/java and test code in src/test/java.

 > * Place test classes in the same package as implementation but in different source directories.
 
 > * Name test classes in a similar fashion as classes they test. Eg: StringCalculatorTest for StringCalculator.
 
 > * Use descriptive names for test methods using the Given/When/Then syntax.
	* Eg:whenSemicolonDelimiterIsSpecifiedThenItIsUsedToSeparateNumbers()
 
 
**Processes**


> * Write test before writing the implementation code. Be focused on requirements before starting to work on a code.

>  * Only write code when test is failing.

>  * Rerun all tests every time implementation cide changes.

>  * All test should pass before new test is written. 

>  * Refactor (improved code readability and reduced complexity) only after all tests are passing.

		
**Development Practices**


> * Write the simplest code to pass the test.

> * Write assertions first and act later.

> * Minimize assertions in each test.

> * Donot introduce dependencies between tests. Each test should be independent from others.

> * Tests should run fast.

> * Use mocks. Mocks are prerequisites for fast execution of tests and ability to concentrate on a single unit of functionality.

> * Use setup(@BeforeClass and @Before : Setting up test data in database) and tear-down(@After and @ AfterClass : Destroy data oe state created during the setup phase) methods. 

>  * Do not use base classes. Tests clarity should more important than avoiding code duplication.


		
**Tools**


> * Code Coverage: Assurance that everything is tested.

> * Use Behaviour Driven Development along with TDD.  
	* TDD is fast to develop, helps the design process and gives confidence through fast feedback. 
	* On the other hand, BDD is more suitable for integration and functional testing, provide better process for requirements gathering through narratives and is the better way of communication with clients through scenarios.
		
		
	
**Different Phases of TDD**	

		
 >
  <p><img src="Images/TDD.png " width="300" height="300"/></p>
  
  
  **Adding junit test**
  

  
 * Create and setup a "tests" folder
 	* In the Project sidebar on the left, right-click your project and do New > Directory. Name it "test" or whatever you like.
	* Right-click the folder and choose "Mark Directory As > Test Source Root".
* Adding JUnit library
	* Right-click your project and choose "Open Module Settings" or hit F4. (Alternatively, File > Project Structure, Ctrl-Alt-Shift-S is probably the "right" way to do this.
	* Go to the "Libraries" group, click the little green plus (look up), and choose "From Maven...".
	* Search for "junit" -- you're looking for something like **`junit:junit:4.11`**.
	* Check whichever boxes you want (Sources, JavaDocs) then hit OK.
	* Keep hitting OK until you're back to the code.

* Write your first unit test
	* Right-click on your test folder, "New > Java Class", call it whatever, e.g. MyFirstTest.
```

        import org.junit.Assert;
        import org.junit.Test;

        public class MyFirstTest {
            @Test
            public void firstTest() {
                Assert.assertTrue(true);
            }
        }
```
* Run your tests
	* Right-click on your test folder and choose "Run 'All Tests'". Presto, testo.
	* To run again, you can either hit the green "Play"-style button that appeared in the new section that popped on the bottom of your window, or you can hit the green "Play"-style button in the top bar.


### December 27, 2017

* The @Test,@Before and @After methods should be public and void.

		initializationError(Practice1.EmpBusinessLogicTest): Method calculateAppraisalTest() should be public
		
		initializationError(Practice1.EmpBusinessLogicTest): Method calculateAppraisalTest() should be void
		
* The @BeforeClass and @AfterClass should be public static void.

* The order in which the annotations are executed is 
		
		@BeforClass	- executes only once
		@Before	- exceutes before each test method
		@Test
		@After	- executes after each test method
		@AfterClass	executes only once

* assertEquals(if expected= int, if actual= double, delta=0.0)
		
		For compatibility add delta = 0.0
		
* Result from failure.toString()

		calculateAppraisalTest(Practice1.EmpBusinessLogicTest): expected:<5000.0> but was:<500.0>
		
		function_name_in_test(package_name.class_name): error

* Assert methods
	* Only failed assertions are recorded.

		void assertEquals(boolean expected, boolean actual);
		void assertTrue(boolean condition);
		void assertFalse(boolean condition);
		void assertNotNull(Object object);
		void assertNull(Object object);
		void assertSame(boolean condition);
		void assertNotSame(boolean condition);
		void assertArrayEquals(expectedArray, resultArray);
		
* Run multiple test classes

	* Without creating a suite class

			Result result = JUnitCore.runClasses(TestClass1.class, TestClass2.class);
			
	* Creating a suite class
	
			import org.junit.runner.RunWith;
			import org.junit.runners.Suite;

			@RunWith(Suite.class)

			@Suite.SuiteClasses({
				TestClass1.class,
				TestClass2.class
			})
			public class TestSuite {
			}
			
		* In main Test class
			
				Result result = JUnitCore.runClasses(TestSuite.class);
		
		
* Using timeout

	* Using timeout
	
			@Test(timeout = 1000)
    			public void checkForInitialization() {}
    			
	* Error
    	
    			checkForInitialization(Practice2ForSuiteCase.TestClass1): test timed out after 1000 milliseconds
    			
    			
* Test whether the code throws a desired exception or not

	* Introduce the following code
			
			int a = 0;
        	int b = 1 / a;
        		
        * if @Test(timeout = 1000,expected = ArithmeticException.class)
        
        		result.wasSuccessful() = true
        		
        * if not
        
        		exception : checkForInitialization(Practice2ForSuiteCase.TestClass1): / by zero
        		result.wasSuccessful() = false
        
* Parameterized Test

	* Allow a developer to run the same test over and over again using different values
	* Steps
		
		 * Annotate test class with @RunWith(Parameterized.class).
		 
		 * Create a public static method annotated with @Parameters that returns a Collection of Objects (as Array) as test data set.
		 
		 * Create a public constructor that takes in what is equivalent to one "row" of test data.
		 
		 * Create an instance variable for each "column" of test data.
		 
		 * Create your test case(s) using the instance variables as the source of the test data.
		 

* Creating a TestNg test class

	* Disable plugin for junit.
	
	* Click Alt+Enter in the class for which you want to create the test class.
	
	* Choose TestNg
	
	* Click Alt+Enter in @Test and import the required libraries.
	
	
###  TESTNG

* The order of execution is

		@BeforeSuite
		@BeforeTest
		@BeforeClass
		@BeforeMethod
		@Test case 1
		@AfterMethod
		@BeforeMethod
		@Test case 2
		@AfterMethod
		@AfterClass
		@AfterTest
		@AfterSuite
		
		 

    		

    		

    		

    		
	
	
   
		

  

		
