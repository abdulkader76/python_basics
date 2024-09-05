# Finding Index

# Python lists come with a variety of built-in methods that allow for common list manipulations. One such operation is determining the index of an item in the list.

#Given a list:
fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

# How would you determine the index of the fruit "cherry" in this list?

# Refer to the official Python documentation on lists to assist with your answer.

# python documentation:
# https://docs.python.org/3/tutorial/datastructures.html

#  list.index(x[, start[, end]])
#     Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

# use .index('item_name') method on fruits with the item you are looking for. If item is in the list, it will return a the index.
# if not, it will raise an error

print(fruits.index('cherry'))
# 2

print(fruits.index('grape'))
# ValueError: 'grape' is not in list