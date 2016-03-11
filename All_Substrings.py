##Generate all substrings of a given string.Empty string should NOT be included and all strings should
#be sorted alphabetically.The final list should have the substring ordered alphanetically

import unittest

def  build_subsequences( s):
    #List to generate a set of all substrings
    substr_list=list()
    #List to contain strings sorted in their own place alphabetically
    substr_sorted_list=list()

    #variable to hold length of substrings being generated
    substr_len=1
    
    while(substr_len<=len(s)):

        for each_pos,item in enumerate(s):
            #With the given substring length,getting the endpoint for substring starting at item character
            final_pos=each_pos+substr_len
            # not going too far
            if final_pos>(2*len(s))-1:
                continue
            #to loop back to the string for getting substrings eg: abc should also yield ca    
            elif final_pos>=len(s) and final_pos<(2*len(s))-1 and (final_pos-len(s))!=each_pos:
                #all full length strings whatever order they appear in should not be considered as different
            	if len((s[each_pos:(len(s))]+s[0:(final_pos-len(s)+1)]))==len(s):
            		continue
                #Generating the substring by taken end of string first and then looping back to beginning    
            	else:
                	substr_list.append(s[each_pos:(len(s))]+s[0:(final_pos-len(s)+1)])
            # just moving forward in the string and getting the substring starting at item
            else:
                substr_list.append(s[each_pos:final_pos])
        substr_len=substr_len+1

    #sorting each substring
    for substr in substr_list:
     	substr_sorted_list.append(''.join(sorted(substr)))

    #final sorting    
    return sorted(substr_sorted_list)
    
#Test cases
class Test(unittest.TestCase):

    def test_buildSubsequence(self):
        self.assertEqual(build_subsequences('abc'),['a','ab','abc','ac','b','bc','c'])
        
    def test_empty_input(self):
        self.assertEqual(build_subsequences(''),[])

    def test_single_char_input(self):
        self.assertEqual(build_subsequences('b'),['b'])

    def test_double_char_input(self):
        self.assertEqual(build_subsequences('ea'),['a','ae','e'])


if __name__ == '__main__':
    unittest.main()