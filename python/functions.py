def SieveOfEratosthenes(n):
    prim = [False] * (n + 1)
    ret = []
    for i in range(2, n + 1):
        if not prim[i]:
            ret.append(i)
            for j in range(i, n + 1, i):
                prim[j] = 1
    return ret

def upper_bound(low,high,val): #Finding first F
    while low < high:
        mid = low + (high-low)//2 
        if l[mid] <= val:
            low = mid+1
        else:
            high = mid 
    return low 

def lower_bound(low,high,val): #Finding first T
    while low < high:
        mid = low + (high-low)//2
        if l[mid] >= val:
            high = mid
        else:
            low = mid+1
    return low 

def powerOf2(n):
    return n > 0 and n & (n-1) == 0

def freq(l):
    d = {}
    for i in l:
        d[i] = d.get(i,0)+1
    return d

def pre(l):
    p = [l[0]]
    for i in range(1,len(l)):
        p.append(p[-1]+l[i])
    return p 

def suf(l):
    p = [l[-1]]*(len(l))
    for i in range(len(l)-2,-1,-1):
        suf[i] = p[i+1]+l[i]
    return p 

def prefix_sum_2d(l): 
    n = len(l)
    m = len(l[0])
    p = [[0 for i in range(m+1)] for j in range(n+1)]
 
    for i in range(1,n+1):
        for j in range(1,m+1):
            p[i][j] = p[i-1][j]+p[i][j-1]+l[i-1][j-1]-p[i-1][j-1]
    return p 

from math import gcd
def lgcd(l): 
    a = 0
    for i in l:
        a = gcd(a,i)
    return a

def bin_sqrt(x): # Returns floor of sqrt // O(logx) //
    if x == 0 or x == 1:
        return x
    l = 1
    r = x
    while l<=r:
        mid = (l+r)/2
        y = mid*mid
        if y>x:
            r = mid-1
        elif y == x:
            return mid
        else:
            if ((mid+1)*(mid+1))>x:
                return mid
            else:
                l = mid+1

def lcs(a, b): # Returns the longest common subsequence of two strings in //O(n^2)//
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    i,j = len(a),len(b)
    l = []
    while i!=0 and j!=0:
        if dp[i][j] == dp[i][j-1]:
            j-=1
        elif dp[i][j] == dp[i-1][j]:
            i-=1
        else:
            i-=1
            j-=1
            l.append(a[i])
    s = ''.join(l)
    return s[::-1]

from bisect import bisect_left
def lis(arr): #O(nlogn)
    l = []
    for i in arr:
        pos = bisect_left(l,i)
        if pos == len(l): 
            l.append(i) 
        else:
            l[pos] = i
    return len(l)