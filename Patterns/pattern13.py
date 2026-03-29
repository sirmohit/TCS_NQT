'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1 

2 3 

4 5 6 

7 8 9 10 

11 12 13 14 15
'''

class Solution:
    def pattern13(self,n):
        num = 1
        for j in range(1,n + 1):
            for i in range(j):
                print(num, end= " ")
                num += 1
            print()
n = 5
            
a= Solution()
a.pattern13(5)