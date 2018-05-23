### HTML

*  strong and b for bold
* em and i for italics
* ol for ordered list with numbers and ul for unordered list with bullets
* type tag name and hit tab and it will autocomplete

* The tag strong does not affect the headers h1-h6

* The header tags should be correct at the front but in the end it may be anything  like h1 ... h4 will give out the size of h1. Like wise h4....h1 will give out the tag of h4

* Typing lorem in head or body of html and pressing tab will give a test text.

* "div" is a block level element so it takes up its own line like "p". So to customize a specific content i.e. some words inside of a paragraph we use span because span is a inline container

* "a" tag is an inline element so it doesnot take up its own line after images.

* When specifying the href for "a" tag we must provide https/https before the url to direct it to the  specified url otherwise it will try to find it with the file protocol and search in the directory.

* In tables to distinguish between head and body we have "thead" and "tbody".Table starts with "table". Then there are th for headers, tr for rows and td for data.

* For inputs we have different types-text, password, radio, date,submit,file.

* In forms, we have action which is the location where the data is sent to and method is the type of request i.e. get or post. If we do not specify the action, the data is sent to the same page and the page gets refreshed. If we do not specify the method, the default is get request.

* In forms if we have assigned a name to the input fields and the method is get method, then on submit we can see the key value pair in the url.

		file:///home/swainstha/Documents/Web/inputs.html?username=asa&password=qwqw
		
* In forms we can add labels for inputs in two different ways. The second way can use the ame or the id of the inputs for "for" attribute.

		<label>
      		Username:
      		<input name="username" type="text" placeholder="username">
    	</label>
    	
    	<label for="password">Password:</label>
      		<input name="password" type="password" placeholder="password">
      		
* In forms if we have a button at the end of the form, it is used as a submit button.


### CSS
* In radios, checkboxes and dropdown menus, we ca use the value attribute for the elements to send to the server with the name as key value pair.
      		
* Checkbox can be selected or unselected. Eg: we can choose a set of skills. Radio cannot the unselected if otherwise another option is there. Eg: choosing gender


* Border style must be provided to see the border. If border color is not provided it will of the color of the text in which it is included in. If the width is not specified then default width will be used.

* The attributes of the border can be provided all in one go

      border: width style color

* Advanced Selectors
	* -Star selector-for all the elements of the file

     		 * {
     		 border: 1px solid lightgrey;
    		}

	* Descendant Selectors - for those that are inside something

    		li a {
      color: red;
    }
    
	* Adjacent Selectors - which come along with or after

    		h4 + ul {
      		border: 1px solid lightgrey;
    		}

	* Attribute Selectors which contains a specific value in an attribute of the elements

    		a[href="http://www.google.com"] {
      background: lightgrey;
    }

	* nth of type Selectors

	    	ul:nth-of-type(3) {
 	    	 background: red;
    		}

Specificity

    Type Selectors
    li{}, li a{}, li + a{}

    Class, attribute and pseudo class Selectors
    .hello{}, input[type="text"] {}

    ID Selectors
    #hello

    link-https://specificity.keegan.st/
    
 * Box Model
 
 	* Content
 	* Padding
 	* Border
 	* Margin
 
 * Margin
 
 		Margin: Top Right Bottom Left;
 		Margin: Top/Bottom Right/Left;
 		Margin: auto //To divide equally
 		
* There may be some spacing between the elements even if we have not specified any margins. So use float to get rid of the spacing.

* We can use max-width to some pixels and width to some percentage to make the page look good at different window sizes. At full screen size the element will remain at 700 px but when the window size it reduced it checks whether 700px is lesser than 80% of the window. If it is, it remains at 700 px or otherwise shrinks to 805 of the window.

		max-width: 700px;
  		width: 80%;
  		
 * In font sizes "em' relates to the parent which it is inside but "rem" relates to the root element.
 
 * We can use "hr" for underlines.


### Bootstrap

* containers have built in margins.

* The jquery cdn link should be written above the javascript cdn link otherwise the page wont be responsive.

* Nav bar collapse

	* Collapse button
	
			<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#hahaha" aria-expanded="false">

	* Elements to collapse
	
			<div class="collapse navbar-collapse" id="hahaha">
			
	* They are related by id="hahaha"
	
* Anytime we use a grid system, it must be inside a container.

* Grid system has 12 columns.

* Use of grid

		<div class="row">
        <div class="col-lg-1 col-md-2 col-sm-3 col-xs-6 pink">COL LG 4</div>
        <div class="col-lg-1 col-md-2 col-sm-3 col-xs-6 pink">COL LG 4</div>
        <div class="col-lg-1 col-md-2 col-sm-3 col-xs-6 pink">COL LG 4</div>
        <div class="col-lg-1 col-md-2 col-sm-3 col-xs-6 pink">COL LG 4</div>
        <div class="col-lg-1 col-md-2 col-sm-3 col-xs-6 pink">COL LG 4</div>
        <div class="col-lg-1 col-md-2 col-sm-3 col-xs-6 pink">COL LG 4</div>
        <div class="col-lg-1 col-md-2 col-sm-3 col-xs-6 pink">COL LG 4</div>
        <div class="col-lg-1 col-md-2 col-sm-3 col-xs-6 pink">COL LG 4</div>
        <div class="col-lg-1 col-md-2 col-sm-3 col-xs-6 pink">COL LG 4</div>
        <div class="col-lg-1 col-md-2 col-sm-3 col-xs-6 pink">COL LG 4</div>
        <div class="col-lg-1 col-md-2 col-sm-3 col-xs-6 pink">COL LG 4</div>
        <div class="col-lg-1 col-md-2 col-sm-3 col-xs-6 pink">COL LG 4</div>
      	</div>
      	
  * If we have the same length for the large and medium in grid system then we can specify only for medium and bootstrap will think it as the length for large as well.
  
* Even if we have setup the column size, but if the image is arge it will not be contained in the column specified, so we use a thumbnai class as well.

* In nav headers we should put the heading inside the "a" element inside of the "li" element.

* width of nav bar- 70px

* In nav bar, container-fluid does not have left and right paddings.

* Our css stylesheet links shoud be after the bootstrap css links so, ours can override it.

* Text Shadow- It can be applied one after another

		text-shadow: offset-x offset-y blur-radius color
		
* Bootstrap to be responsive in mobile devices, add following line above title in head.

		<meta name="viewport" content="width=device-width, initial-scale=1">
		
* If hr tag does not work in mobile devices then add

		max-width: 90%;
	
	to the hr element in css. 
	
	
### JavaScript

* 5 Primitive Data Types

	* Numbers - 4, 9.5, -10
	* Strings - "hello", "45"
	* Booleans- true or false
	* undefined
		* Variables that are declared but not initialized are undefined
			
				var name;
				var age;
				
	* null
		* null is explicitly nothing 
		
				var name = "Charlie";
				name = null;
	
* Escape Character - \

* "hello' and 'hello"

		SyntaxError: '' string literal contains an unescaped line break
		
Some useful built-in methods

	* clear();
	* alert("Hello");
	* console.log("Hello");
	* prompt("What is your name?");
	
* Two ways of defining functions

	function cap(str) {
	}
	
	var cap = function(str) {
	}
	
* Defining Arrays

		var friends = [];
		var friends = new Array();

* Arrays can hold any type of data

		var random = [ 49, "hello", true, null];
		
* Arrays have a length property

		nums.length;
		
* Some built in functions

	* To add data to the last of the array
	
			fruits.push("Banana");
			
	* To delete data from last of the array
	
			fruit.pop():
			
	* To add to the front of the array
	
			fruit.unshift("Apple");
			
	* To remove the first item in an array
	
			fruit.shift();
	
	* To find the index of an item in an array. Returns -1 if not  found
	
			fruit.indexOf("Grapes");
					
	* To copy a part of the array
	
			fruits.slice(1,3);
			
* In chrome browser, It doesn't display the HTML on the page until after the popup(prompt, alert) has been closed. So add

		    window.setTimeout(function() {
      		// put all of your JS code from the lecture here
   		 }, 500);
   		 
   	* This gives the HTML a half second to load before running the JS, which circumvents the issue of the prompt function blocking the HTML from loading right away.
   	
* For Rach loop

		arrayName.forEach(function(argument) {
		
		});
		
* When we pass a function as an argument in a function, we dont need to provide brackets.

* Object in Javascript

		var person = {
			name = "Yalisha",
			age = 23;
			city = "Dharan"
		};
		
* Advantage over Array

	* Unlike arrays, objects have no order
	* Objects are key-value pairs.
	
* Accessing objects

		object["name"];
		object.name;
		
	* We cannot use the dot notation if the name of the element of the object starts with a number.
	
	* We cannot use dot notation if the name of the elemen of the object are of two words separated by a space.
	
	* We can lookup a variable with bracket notation
	
			var str = "name"
			object[str]; 
			not object.str;
			
* Other ways of declaring objects

		var person ={}
		person.name = "Swain";
		
		var person = new Object();
		person.name = "Swain";
		
* Note

		JavaScript code at the bottom of the HTML document, right before the closing </body>  tag.
		
		The HTML will need to have loaded before the JavaScript is run, otherwise the JavaScript will throw an error because the HTML that it is trying to select and manipulate doesn't exist (yet).
		
* Select and manipulate

		var body = document.querySelector("body");
		body.style.background = "white";
		
		var tag = document.getElementbyId("high");
		
		var tags = document.getElementByClassName("bolded");
		
		var tags = document.getElementByTagName("p");
		
		var tag = document.querySelector("#highlight");  //returns the first element that matches a given CSS-style selector
		
		var tag = document.querySelector("h1");  //returns the first element that matches a given CSS-style selector
		
		var tags = document.querySelectorAll("h1");
		
		var tag = document.querySelector(".className"); //returns the first one
		
		var tag = document.querySelector("h1 + p"); 