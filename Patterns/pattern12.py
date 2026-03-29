'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1        1
12      21
123    321
1234  4321
1234554321
'''
class Solution:
    def pattern10(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end = "")
            for k in range(1):
                print(" " * (2*(n-i)),end = "")
                
            for l in range(i,0,-1):
                print(l,end = "")
            print()
n = 5
            
a= Solution()
a.pattern10(5)

#------------------------------------------------

# optimize code

class Solution:
    def pattern10(self, n):
        for i in range(1, n+1):
            print(
                "".join(map(str, range(1, i+1))) +
                " " * (2*(n-i)) +
                "".join(map(str, range(i, 0, -1)))
            )