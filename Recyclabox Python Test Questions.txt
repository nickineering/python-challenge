A Bag of Pythons
-----------------

1. 
Your Django application is built for paranoids who want a complete audit trail of any changes made to the data.
The audit should contain any modification made to any attribute of the model and include the time of change and by which user.
How would you approach this?


2. 
Create a function that receives one argument of any type and always returns a list of strings.
If the argument is a dict, return a list of the keys. If it's a number, return a string representation of it as a list, etc.
Bonus points if it can be done without explictly checking the argument type inside the function body.

Sample output:

> to_list([1, 2, 3])
> ['1', '2', '3']
> to_list({'one': 1, 'two': 2})
> ['one', 'two']
> to_list('value')
> ['value']

3. 
Given two lists (of same length):
	l1 = ['a', 'b', 'c', 'd']
	l2 = [1, 2, 3, 4]
Create a function that returns a dict where each element of l1 is the key and it's value is the corresponding element from l2.
Bonus points if you can explain how you'd deal with lists of different lengths.

4. 
Write a small self contained python command line tool that receives a list of URLs as command line arguments, and returns a structured JSON data containing all the links and image urls within the document. The tool should be generic enough to work with any URL.
Don't spend more than an hour or two on this.
The result should include everything to make it usable (requirements file, etc.), and tests to ensure it works as expected.

It should be executed as:

>> ./mytool http://example.com http://bbc.co.uk 

And return:

{
	"http://example.com": {
		"links": [
			"https://example.link1.com",
			"https://example.link2.com"
		],
		"images": [
			"https://example.link.com/image/one.jpg",
			"https://example.link.com/images/two.png"
		]
	},
	"http://bbc.co.uk": {
		.....
	}
}
