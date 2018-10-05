#!/usr/bin/env python3

def maxset0(A):
    largestArray = []
    largestSum = 0
    for i in range(0, len(A)):
        for j in range(i+1, len(A)+1):
            if A[j] > 0:
                if (sum(A[i:j]) > largestSum):
                    largestArray = A[i:j]
                    largestSum = sum(largestArray)
                    print("sum(A[{},{}])=={}".format(i, j, largestSum))
                elif (sum(A[i:j]) == largestSum): # There is a tie with sum.
                    if len(A[i:j]) > len(largestArray):
                        largestArray = A[i:j]
                        largestSum = sum(largestArray)
                    elif len(A[i:j]) < len(largestArray):
                        pass # Largest is still the same
                    else: # There is a tie with length.
                        if A[i] < largestArray[0]:
                            largestArray = A[i:j]
                            largestSum = sum(largestArray)
                        else:
                            pass
                else:
                    pass
            else:
                break
    return(largestArray)

def maxset(A):
    max = [A[0]]
    i = 0
    while i < len(A):
        j = i
        while j < len(A)+1:
            j += 1
            if A[j] > 0:
                curr=A[i:j]
                if sum(max) < sum(curr):  # We just found a new maximum
                    max = curr
                elif sum(max) == sum(curr):
                    if len(max) < len(curr):
                        max = curr
                    elif max[i] > curr[i]:
                        max = curr
            else:
                break
        i += 1



A = [1, 2, 5, -71, 2, 2, 2, 2]
B = maxset(A)
print(B)
