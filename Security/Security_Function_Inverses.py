#!/bin/python

#Security Function Inverses
#Javier Garcia

n = int(raw_input())
fx = map(int, raw_input().split())

for i in range(n):
    print fx.index(i+1)+1
