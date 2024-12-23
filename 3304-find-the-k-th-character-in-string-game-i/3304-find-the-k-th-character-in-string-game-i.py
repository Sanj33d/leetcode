class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        def helper(k, w):
            if len(w) >= k: # bc
                return w[k-1]

            else:
                g = "" ## operation
                for x in range(len(w)):
                    g += chr(ord(w[x])+1)
                w += g ##
                
                return helper(k, w) # rc
        ans = helper(k, word)
        return ans
        
        # word = "a"
        # while len(word) < k: #MMI: won't work with for loop
        #     generated = ""
        #     for i in range(len(word)):
        #         generated += chr(ord(word[i])+1)
        #     word += generated
        # return word[k-1]

