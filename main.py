import sys

def checkMapping(s1, s2):
	print("Received Command Line Arguments, s1:  "+str(s1)+", s2: "+str(s2))
	if len(s1) != len(s2):
                return False    #One to One mapping is not possible when length are different.

try:
        print(checkMapping(sys.argv[1],sys.argv[2]))
except IndexError:
        print("Add Two Inputs")
