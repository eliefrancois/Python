import os
import sys
import operator
import re

def Count(l):
    word_dict = {}
# creaing empty list
    word_list = []
    for line in l.split():
# appening to list
        if line in word_dict:
            word_dict[line] += 1
        else:
            word_dict[line] = 1
# now we are sorting to dictonary based on count value
# sorted needs 3 aruguments
    return (sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True))

def main():
# taking inputs from user in form of string
    l = str(input("Please enter integers separated by spaces: "))
#print(f)
# passing list to function
    Integer_list = Count(l)
# printing output to screen
    for w in list(Integer_list[:]):
            print (w[0],'Occures -->',w[1],' times',end ="\n")

# runing main function
if __name__=="__main__":
    main()
