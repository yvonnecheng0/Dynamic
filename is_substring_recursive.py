""""
Module will determine whether something is a substring using recursion
Yvonne Cheng 
csci 112
Winter, 2023
"""

def is_substring(str1, str2):
    #str1 empty, always a substring of str2
    if not str1:
        return True
    #str1 not empty, but str2 empty, str1 not substring of str2
    elif not str2:
        return False
    #first char of str1 != first char of str2, attempt to match str1 with rest of str2
    elif str1[0] != str2[0]:
        return is_substring(str1, str2[1:])
    #first char of str1 == the first char of str2, attempt to match str1 with rest of str2 with and without first char of str1
    else:
        return is_substring(str1[1:], str2[1:]) or is_substring(str1, str2[1:])

if __name__ == "__main__":
    print(is_substring("geoff", "xxgxxeoxxfxxxf"))
    print(is_substring("yvonne", "cheng"))  
    print(is_substring("i", "hi"))  
    print(is_substring("", "meow")) 
    print(is_substring("abc", "xabbxc"))   
     


