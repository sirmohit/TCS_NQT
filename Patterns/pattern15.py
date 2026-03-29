'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



ABCDE

ABCD

ABC

AB

A

'''
class Solution:
    def pattern15(self,n:int):
        for i in range(n,0,-1):
            for j in range(i):
                print(chr(65 + j),end = "")
            print()
            