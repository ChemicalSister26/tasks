# task from leetcode = two sum.
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


exit = False
a = list(map(float, input().split(',')))
b = float(input())
for i in range(len(a)-1):
    for k in range(len(a)-1):
        if a[i]+a[k+1] == b:
            print([i, k+1])
            exit = True
            break
    if (exit):
        break