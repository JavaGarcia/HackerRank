#!/bin/python
#Javier Garcia
n = int(raw_input())
x = map(int, raw_input().split())
for i in range(n):
    if i+1 != x[x[i]-1]:
        print "NO"
        exit()
print "YES"
