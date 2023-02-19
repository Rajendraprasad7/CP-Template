class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1
    


import bisect
import math
class SortedList():
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def __init__(self,buckets):
        buckets = list(buckets)
        buckets = sorted(buckets)
        self._build(buckets)

    def __iter__(self):
        for i in self.buckets:
            for j in i: yield j

    def __reversed__(self):
        for i in reversed(self.buckets):
            for j in reversed(i): yield j

    def __len__(self):
        return self.size

    def __contains__(self,x):
        if self.size == 0: return False
        bucket = self._find_bucket(x)
        i = bisect.bisect_left(bucket,x)
        return i != len(bucket) and bucket[i] == x

    def __getitem__(self,x):
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for i in self.buckets:
            if x < len(i): return i[x]
            x -= len(i)
        raise IndexError

    def _build(self,buckets=None):
        if buckets is None: buckets = list(self)
        self.size = len(buckets)
        bucket_size = int(math.ceil(math.sqrt(self.size/self.BUCKET_RATIO)))
        tmp = []
        for i in range(bucket_size):
            t = buckets[(self.size*i)//bucket_size:(self.size*(i+1))//bucket_size]
            tmp.append(t)
        self.buckets = tmp

    def _find_bucket(self,x):
        for i in self.buckets:
            if x <= i[-1]:
                return i
        return i

    def add(self,x):
        # O(√N)
        if self.size == 0:
            self.buckets = [[x]]
            self.size = 1
            return True

        bucket = self._find_bucket(x)
        bisect.insort(bucket,x)
        self.size += 1
        if len(bucket) > len(self.buckets) * self.REBUILD_RATIO:
            self._build()
        return True

    def remove(self,x):
        # O(√N)
        if self.size == 0: return False
        bucket = self._find_bucket(x)
        i = bisect.bisect_left(bucket,x)
        if i == len(bucket) or bucket[i] != x: return False
        bucket.pop(i)
        self.size -= 1
        if len(bucket) == 0: self._build()
        return True

    def lt(self,x):
        # less than < x
        for i in reversed(self.buckets):
            if i[0] < x:
                return i[bisect.bisect_left(i,x) - 1]

    def le(self,x):
        # less than or equal to <= x
        for i in reversed(self.buckets):
            if i[0] <= x:
                return i[bisect.bisect_right(i,x) - 1]

    def gt(self,x):
        # greater than > x
        for i in self.buckets:
            if i[-1] > x:
                return i[bisect.bisect_right(i,x)]

    def ge(self,x):
        # greater than or equal to >= x
        for i in self.buckets:
            if i[-1] >= x:
                return i[bisect.bisect_left(i,x)]
    def index(self,x):
        # the number of elements < x
        ans = 0
        for i in self.buckets:
            if i[-1] >= x:
                return ans + bisect.bisect_left(i,x)
            ans += len(i)
        return ans

    def index_right(self,x):
        # the number of elements < x
        ans = 0
        for i in self.buckets:
            if i[-1] > x:
                return ans + bisect.bisect_right(i,x)
            ans += len(i)
        return ans
    
class SegmentTree: # //O(logn) for operations and O(n) for building//
    def init(arr): # n shld be a power of 2...hence add extra zeros before itself if needed //O(n)//
        n = len(arr)
        tree = [0]*(2*n) 
        for i in range(n):
            tree[n+i] = arr[i] # The actual array is between indices n to 2*n-1 the first nodes store sums
 
        for i in range(n-1,-1,-1):
            tree[i] = tree[i<<1]+tree[(i<<1) | 1] # parent node value  = child node's sum i<<1 = 2*i, i<<1 |1 = 2*i+1
        return tree
        
    def add(tree,i,v): # Sets vertex i to value v (i shld be 0 based indexing) //O(logn)//
        i += len(tree)//2 # As the actual array is between n and 2*n-1, we add n to i (n = len(tree)//2)
        tree[i] += v
        while i>1:
            tree[i>>1] = tree[i]+tree[i^1] 
            i >>=1
            # Calculating the values of prev nodes. (eg if node 9 is changed 9>>1 = 4 takes values of node i(9) and node i^1(8))
 
    def range_sum(tree,l, r): # calculates the sum of values in the range [l,r-1] (l and r take 0 based indexing) //O(logn)//
        l += len(tree)//2
        r += len(tree)//2
        sum = 0
        while l<r: 
            if l&1:
                sum += tree[l] # If the index is odd, add its value to sum. if the index is even it means there would be a parent 
                l += 1         # of this with odd index
            if r&1:
                r -= 1
                sum += tree[r]
            l >>= 1
            r >>= 1
        return sum