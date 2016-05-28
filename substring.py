#!/usr/bin/python
testVar = raw_input("Enter a string :")
str1 = int(input("Enter a source range: "))
str2 = int(input("Enter a destination range: "))
#for n in range(str1, str2+1):
 #       print(testVar[n])
final = testVar[str1:str1+str2-1]
print final


