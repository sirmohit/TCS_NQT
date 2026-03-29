'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
A

AB

ABC

ABCD

ABCDE

3️⃣ Convert number → character

Use ASCII:

chr(65) = 'A'
chr(66) = 'B'
chr(67) = 'C'


'''

class Solution:
    def pattern14(self,n:int):
        for i in range(1,n+1):
            for j in range(i):
                print(chr(65 +j),end = "")
            print()


