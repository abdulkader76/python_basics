# Reverse

# Is there a method to reverse a string, for example turning 'hello' into 'olleh'?

# Simple answer: There's no method to reverse a string.

# I have 2 ways to reverse a string

# Method 1
# use index slicing to reverse the string
greeting = 'hello'
print(greeting[::-1])      # olleh

# Method 2
# use the reversed methods for sequences and using join
text = 'helloworld'
text_reversed = reversed(text)
text = ''.join(text_reversed)
print(text)          # dlrowolleh