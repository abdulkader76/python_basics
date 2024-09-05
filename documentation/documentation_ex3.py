# Right Justifying Strings

# Use the Python documentation for the str class to determine which method can be used to right justify a str object.

# Python Documentation:

# str.rjust(width[, fillchar])

# Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).

text = 'Hello World!'
# rjust() returns the str 'text' right justified
# with padding done be default white space or specific
# character
result = text.rjust(15, '*')
print(result)
# output: ***Hello World!