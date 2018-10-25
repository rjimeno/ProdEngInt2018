#!/usr/bin/env bash

: << END_OF_COMMENT


Write a bash script to replace all the occurrences of / with \ and \ with / in a text file named input.

For simplicity sake, you may assume:

    input contains only either forward slash / or backward slash \

Example:

Assume that input has the following content:

\\//

Your script should output the following:

//\\

END_OF_COMMENT

# Incase you have to take input, please take it from file named 'input' (without quotes) [e.g. cat input]
# Print your final output to console. Do not redirect to another file.
# E.g. Suppose the question is to print the content of a file.
#      Your solution should be 'cat input'(without quotes) instead of 'cat input > output'. That's it!
# Your code starts from here...

tr "\\\/" "/\\" < input
