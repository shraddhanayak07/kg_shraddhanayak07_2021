import sys
  
def checkMapping(s1, s2):
    if len(s1) != len(s2):
        return False                    #One to One mapping is not possible when length are different
    dic = {}                            #Created a dictonary to store character mappings
    for i in range(0,len(s1)):
        if s1[i] in dic.keys():         #check if a character is present in dictionary
            if dic[s1[i]] != s2[i]:     #if yes, then check if its value is not equal to the character in s2
                return False            #if yes, then return False, since two characters cannot be mapped
        dic[s1[i]] = s2[i]              #if character in s1 is not present in dictionary, then add it to 
    return True

try:
    print(checkMapping(sys.argv[1],sys.argv[2]))
except IndexError:
    print("Add Two Inputs")
