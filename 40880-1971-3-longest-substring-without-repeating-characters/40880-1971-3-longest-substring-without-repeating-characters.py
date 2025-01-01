class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # approach1: hardcode: O(n^3)
        # approach2: sliding window: O(n): need to learn
        # ap2: 
        sett = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            lenn = (r - l) + 1
            longest = max(longest, lenn)
            sett.add(s[r])

        return longest
        
        # ap1
        # checker = ''
        # l = []
        # lenn = 0
        # l.append(lenn)
        
        # i = 0
        # while i<len(s):
        #     j = i
        #     while j<len(s):
        #         if s[j] not in checker:
        #             checker += s[j]
        #             lenn += 1

        #             j += 1
        #         else:
        #             checker = ''
        #             l.append(lenn)
        #             lenn = 0

        #             i += 1
        #             break ## mmi, breaks the inner loop
        #     ## and comes to this line, checks whether i < len(s)
        #     ### and if true then outer loop continues 
        # return max(max(l), lenn)
                

        