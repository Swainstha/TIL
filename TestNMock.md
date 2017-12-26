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
  <p><img src="TDD.png " width="300" height="300" hspace="20"/></p>

		
