
# There are  jugs on a table and each jug has a capacity .

# Each jug will be filled with water such that the amount of water from Jug 1 to Jug N is in decreasing order. i.e. if Jug  has  amount of water in it then  for .

# What is the maximum amount of water in total the can be poured in all the jugs?

# Input Format

# The first line contains , number of test cases. For each test case,

# First line contains , number of Jugs.

# Second line contains  space seperated integers - .

# Constraints

# Output Format

# For each test case print the maximum amount of water that can be poured in the jugs in a new line.

# Sample Input 0

# 2
# 4
# 10 4 7 3
# 5
# 1 2 3 4 5
# Sample Output 0

# 21
# 5
# Explanation 0

# In the first test case, amount of water in each jug will be,

# 10 4 4 3

# In the second test case it will be,

# 1 1 1 1 1
T = int(input())

for _t in range(T):
    n = int(input())
    C = list(map(int , input().strip().split()))
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    sum1=0
    if len(C)<=1:
        print(C[0])
    maxl = C[0]
    sum1=C[0]
    for i in range(1,len(C)):
        if C[i]<maxl:
            maxl=C[i]
        sum1=sum1+maxl
    print(sum1)
