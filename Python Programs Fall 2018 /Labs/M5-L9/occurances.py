def occurances(s, c) :  
	res = 0
	for i in range(len(s)) : 
		if (s[i] == c): 
			res = res + 1
	return res 
def main():		
    str= input('Enter word: ')
    c = input('Enter character: ')
    print(occurances(str, c)) 

main()	
