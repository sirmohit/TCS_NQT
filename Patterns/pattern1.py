'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*****

*****

*****

*****

*****
Constraints

1 <= n <= 100
'''

class Pattern1:
    def patterns1(self,n):
        for i in range(n):
            for j in range(n):
                print('*',end='')
            print()