# 1st Dec

My instant thought for this question was "modular arithmetic!".

I started by using the example given for testing...
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82

example solution = 3

I then proceeded to convert these values into positive/negative values, so they can be used with modular arithmetic more easily.
e.g. L60 becomes -60, R80 becomes 80

These could then be used like... (50 + (-60)) % 100 >>> 90

Then I coded this to extract and transform the instructions to this format, and kept track of the result, counting 0s.

And it worked!