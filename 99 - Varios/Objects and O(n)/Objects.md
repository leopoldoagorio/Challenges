## Objects

Thank you for agreeing to tackle this code challenge! The purpose of the program is to
compute some basic statistics about a collection of some relatively small positive integers
(you can assume all values will be lower than 1000). We will give you a sample main
program, and you need to create the necessary classes to make it work. This is the main
program:
```python
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4) # should return 2 (only two values 3,3 are less than 4)
stats.between(3, 6) # should return 4 (3,3,4 and 6 are between 3 and 6)
stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)
```

The DataCapure object has the responsibility of collecting numbers and then return an object so
that we can easily obtain stats about how many numbers are less than a value, greater than a
value or between a range of numbers.
These are the restrictions of the challenge:
* You cannot add any import statements (neither python imports nor third party libraries -
testing utilities are allowed though)
* The methods add() less() greater() and between() should have constant time O(1)
* The method build_stats() can be at most linear O(n)
* Appropriate Errors should be thrown upon invalid inputs to methods.

We encourage you to follow all the best practices you know regarding good programming.
Please zip all the python files and send us the response back. We will evaluate your solution
and discuss it with you.