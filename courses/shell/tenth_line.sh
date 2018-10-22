#!/usr/bin/env bash

: << 'END_OF_COMMENT'


The following command prints the top 10 lines of file named input

cat input | head -n 10

The following command prints the bottom 10 lines of file named input

cat input | tail -n 10

Can you somehow use the above information to print the 10th line of the file named input ?

Example:

Assume that the input contains the following:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Line 11
Line 12
Line 13
Line 14
Line 15

Your bash script should output the following:

Line 10

END_OF_COMMENT

# Incase you have to take input, please take it from file named 'input' (without quotes) [e.g. cat input]
# Print your final output to console. Do not redirect to another file.
# E.g. Suppose the question is to print the content of a file.
#      Your solution should be 'cat input'(without quotes) instead of 'cat input > output'. That's it!
# Your code starts from here...

cat input | head -n 10 | tail -n 1
