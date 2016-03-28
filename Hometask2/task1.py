#!/usr/bin/python

list1 = ['one','two','three','four','five','six','seven']
list2 = [1,2,3,4,5]

def dict(list1,list2):
    if len(list1)>len(list2):
        while len(list1)>len(list2):
            list2.append(None)
    else:
        list2=list2[0:len(list1)]
    return {key:value for key,value in zip(list1, list2)}

print dict(list1,list2)
