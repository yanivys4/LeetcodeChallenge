class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum = 0 # max length found
        last_repeat = -1 # index of last repeat
        found_letters = {}
        i = 0
        while i < len(s):
            last_repeat = found_letters.get(s[i])
            if last_repeat != None: # found repeat of char
                maximum = max(maximum,len(found_letters))
                found_letters.clear()
                i = last_repeat + 1
            else:
                found_letters[s[i]] = i
                i = i + 1
                 
        maximum = max(maximum,len(found_letters))
        
        return maximum
