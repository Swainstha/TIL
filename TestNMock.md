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


  

		
