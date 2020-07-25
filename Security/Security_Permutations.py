#!/bin/python
#Javier Garcia

n = int(raw_input())
x = map(int,raw_input().split())
for i in range(n):
    print x[x[i]-1]
