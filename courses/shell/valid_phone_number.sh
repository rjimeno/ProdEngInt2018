#!/usr/bin/env bash

# In case you have to take input, please take it from file named 'input' (without quotes) [e.g. cat input]
# Print your final output to console. Do not redirect to another file.
# E.g. Suppose the question is to print the content of a file.
#      Your solution should be 'cat input'(without quotes) instead of 'cat input > output'. That's it!
# Your code starts from here...

grep '^[(]\{0,1\}[0-9]\{3\}[)]\{0,1\}[ -]\{1\}[[0-9]\{3\}-[0-9]\{4\}$' input
