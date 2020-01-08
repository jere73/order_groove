# order_groove
Python practical exercise.

Standard Libraries Used

* HTMLParser
* urllib2
* Counter from collections


Success Case

* Run the main module
* First, Request class make a request to an URL and retrieves HTML from web page.
* This HTML is passed to Reader class, where is parsed and calculate the number of elements and the top five tags.
* There is a method called getMetrics that return a dictionary with the calculated values.
* Then, the DictOutputFormatter class handles output formats. 
* There are two outputs, to console and to JSON. Both are in the success case.

Test Cases

* RequestTest
* ReaderTest


Note

* http://ordergroove.com/company is not working or not allowed to web scrapping.