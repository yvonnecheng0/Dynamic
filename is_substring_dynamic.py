""""
Module will determine whether something is a substring using dynamic programming
Yvonne Cheng 
csci 112
Winter, 2023
"""

def is_substring(str1, str2):
    # initialize table of zeros with dimensions m × n
    table = [[0] * (len(str2) + 1) for x in range(len(str1) + 1)]
    
    #iterate through the table to fill in row by row
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            #empty string always substring of any string
            if i == 0:
                table[i][j] = 1
            #s1[i-1] == s2[j-1], substring prefix of string up to j
            elif str1[i-1] == str2[j-1]:
                table[i][j] = table[i-1][j-1]
            #s1[i-1] != s2[j-1], substring match string up to j-1
            else:
                table[i][j] = table[i][j-1]
    
    #substring is a substring of whole string when the last row in the table has a 1
    return 1 in table[-1]

if __name__ == "__main__":
    print(is_substring("geoff", "xxgxxeoxxfxxxf"))
    print(is_substring("yvonne", "cheng"))  
    print(is_substring("i", "hi"))  
    print(is_substring("", "meow")) 
    print(is_substring("abc", "xabbxc"))   