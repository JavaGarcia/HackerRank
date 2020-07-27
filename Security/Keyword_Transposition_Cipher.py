#!/bin/python
#Javier Garcia Prada

lines = int(raw_input())
for i in range(lines):
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = raw_input()
    key = ''.join(sorted(set(key),key=key.index))
    newabc = key+abc
    newabc = ''.join(sorted(set(newabc),key=newabc.index))

    arr = []
    for j in range(26/len(key)):
        arr.append(list(newabc[j*len(key):(j+1)*len(key)]))

    if 26%len(key)>0:
        plus = []
        plus =list('_'*(len(key)-(26%len(key))))
        arr.append(list(newabc[(26/len(key))*len(key)::])+plus)


    for i in range(1,len(arr[0])):
        for j in range(0,len(arr[0])-i):
            if(ord(arr[0][j+1]) < ord(arr[0][j])):
                for k in range(len(arr)):
                    #print k
                    aux=arr[k][j]
                    arr[k][j]=arr[k][j+1]
                    arr[k][j+1]=aux

    encryptedabc = ''
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            if arr[j][i] != '_':
                encryptedabc+=arr[j][i]

    abc+=' '
    encryptedabc+='_'
    encrytext=raw_input()
    out=''
    for i in encrytext:
        out+=abc[encryptedabc.find(i)]

    print out
