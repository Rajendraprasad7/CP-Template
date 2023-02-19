# fast IO
import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

#list of numbers
def ilst():
    return list(map(int,input().split()))

#list of strings
def islst():
    return list(map(str,input().split()))
    
#multiple numbers from single line
def inum():
    return map(int,input().split())

#input a matrix
n = int(input())
l = [list(map(int,input().split())) for i in range(n)]

# Adjacency List [space O(V+E) might reduce to O(V^2) if vC2 edges]
l = [[] for i in range(v+1)]
for i in range(e):
    x,y = list(map(int,input().split()))
    l[x].append(y)
    l[y].append(x)

# Adjacency matrix [space O(V^2)]
l = [[0 for i in range(v+1)] for i in range(v+1)]
for i in range(e):
    x,y = list(map(int,input().split()))
    l[x][y] = 1 
    l[y][x] = 1

# Fast IO
import os
from io import BytesIO, IOBase
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b'\n') + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda: self.buffer.read().decode('ascii')
        self.readline = lambda: self.buffer.readline().decode('ascii')
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
