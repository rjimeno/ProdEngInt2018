#!/usr/bin/env bash

: << 'END_OF_COMMENT'
The following command prints all the lines of the file input which contains a number

cat input | grep '[0-9]*'

Example:
Assume that the input has the following content:

axes12
w143th
qwer

Then the given command prints the following ouput:

axes12
w143th


Now change the command slighly so that it prints only the number part of the lines.


Example:
Assume that the input has the following content:

axes12
w143th
qwer

Then your new command should ouput the following content

12
143
END_OF_COMMENT

# Incase you have to take input, please take it from file named 'input' (without quotes) [e.g. cat input]
# Print your final output to console. Do not redirect to another file.
# E.g. Suppose the question is to print the content of a file.
#      Your solution should be 'cat input'(without quotes) instead of 'cat input > output'. That's it!
# Your code starts from here...

cat input | grep -o '[0-9]*'
