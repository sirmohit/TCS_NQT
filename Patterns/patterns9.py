'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''

class Solution:
    def pattern9(self,n):
        for i in range(1,n+1):
            for j in range(1):
                print(" " * (n-i),"*" * (2*i -1),end= "")
            print()
        for i in range(n,0,-1):
            for j in range(1):
                print(" " * (n-i),"*"*(2*i - 1),end= "")
            print()
a = Solution()
a.pattern9(5)

#----------------------------------------------------------------------------------

# optimized code

class Solution:
    def pattern9(self, n):
        # Upper half (including middle row)
        for i in range(1, n+1):
            print(" " * (n - i) + "*" * (2*i - 1))
        
        # Lower half (starting again from n → to repeat middle row)
        for i in range(n, 0, -1):
            print(" " * (n - i) + "*" * (2*i - 1))