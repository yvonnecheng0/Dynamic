""""
Module will test functionality of functions in is_substring_recursive and is_substring_dynamic
Yvonne Cheng 
csci 112
Winter, 2023
"""

import random
import unittest
import is_substring_recursive
import is_substring_dynamic

class TestIsSubstring(unittest.TestCase):
    def test_recursive(self):
        #generate random strings 
        for i in range(10): # run 10 random tests
            str1 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 10)))
            str2 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 15)))
            #set result by checking if str1 is substring of str2
            result = str1 in str2
            #call is_substring function and compare with result
            self.assertEqual(is_substring_recursive.is_substring(str1, str2), result)
    def test_dynamic(self):
        #generate random strings 
        for i in range(10): # run 10 random tests
            str1 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 10)))
            str2 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 20)))
            #set result by checking if str1 is substring of str2
            result = str1 in str2
            #call is_substring function and compare with result
            self.assertEqual(is_substring_dynamic.is_substring(str1, str2), result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)