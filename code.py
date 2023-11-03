s = input()
k = int(input())
n = len(s)
count = 0
ans = 0
r = 0
l = 0
while(r < n):
    if(s[r] == '0'):
        count = count + 1
    while(count > k):
        if(s[l] == '0'):
            count = count - 1
        l = l + 1
    ans = max(ans, r - l + 1)
    r = r + 1

print("length = ", ans);