#!/usr/bin/python

mystr = str("My test string")
rev=reversed(mystr)

def check_palindrome(str1):
    if list(mystr) == list(rev):
       return "This string is palindrome"
    else:
       return "This string isn't a palindrome"

print check_palindrome(mystr)