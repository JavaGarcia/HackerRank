#!/bin/python
#Javier Garcia
message = raw_input()
out = ''
for i in message[0::]:
    out+=str((int(i)+1)%10)
print out
