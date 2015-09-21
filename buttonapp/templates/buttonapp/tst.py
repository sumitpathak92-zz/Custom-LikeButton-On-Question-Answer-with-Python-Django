'''
Created on 21-Sep-2015

@author: sumit
'''
def fib(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

t = int(raw_input())
while(t):
    t-=1
    l = []
    L, R = map(int, raw_input().split())
    l1 = fib(100)
    for i in xrange (L, R):
        l.append(l1[i])   
    print(sum(l))