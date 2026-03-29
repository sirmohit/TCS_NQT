'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



A

BB

CCC

DDDD

EEEEE
'''

class Solution:
    def pattern16(self,n:int):
        for i in range(1,n+1):
            print(chr(64 + i) * i,end = "\n")