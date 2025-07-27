# Runtime: 17 ms, faster than 63% of Python3 submissions
# Memory Usage: 18 MB, beats 13% of Python3 submissions

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_of_longest_substring = 0 #final required result
        #len_of_s = len(s)
        index_of_dup_char = 0
        char = 0
        dic = {}
        while char in range(0,len(s)):
            if s[char] not in dic or dic[s[char]]<index_of_dup_char:
                if (char+1)-index_of_dup_char>len_of_longest_substring:
                    len_of_longest_substring = (char+1)-index_of_dup_char
                dic[s[char]]=char
            else:
                index_of_dup_char = dic[s[char]]+1
                dic[s[char]]=char
                temp_len = 0
            #print(s[char],temp_len,len_of_longest_substring,index_of_dup_char)
            #print(dic)
            char+=1
        return len_of_longest_substring
