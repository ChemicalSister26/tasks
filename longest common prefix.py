# task from leetcode = longest common prefix.
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""

a = input().split(',')
b = []
for i in range(len(a)):
    m = len(a[i])
    b.append(m)
l = min(b)
for i in range(len(a)):
    if len(a[i]) == l:
        s=a[i]
exit = False
for i in range(len(a)):
    for j in range(len(s)):
        if a[i][j] != s[j]:
            exit = True
            break
    if (exit):
        break
print(s[0:j])