'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



    *
   ***
  *****
 *******
*********
'''
class Solution:
    def pattern7(self,n):
        for i in range(1,n+1):
            for j in range(1):
                print(" " * (n - i),"*" * (2*i -1),end = "")
            print()
a = Solution()
a.pattern7(5)

