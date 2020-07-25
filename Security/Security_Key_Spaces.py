#!/bin/python
#Javier Garcia
message = raw_input()
key = int(raw_input())
out = ''
for i in message[0::]:
    out+=str((int(i)+key)%10)
print out
