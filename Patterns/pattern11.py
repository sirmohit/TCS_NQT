'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1 

0 1 

1 0 1 

0 1 0 1 

1 0 1 0 1

1️⃣ Row decides starting value

Look carefully:

Row (i)	Pattern Start
1	1
2	0
3	1
4	0
5	1


'''

class Solution:
    def pattern11(self, n:int):
        for i in range(1,n + 1):
            if i % 2 == 0:
                start = 0
            else:
                start = 1

            for j in range(i):
                print(start,end = "")
                start = 1 - start 
            print()