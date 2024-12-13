class Solution:
    def isValid(self, s: str) -> bool:
        
        stackk = []
        brackets_open = ['(','{','[',]

        for i in range(len(s)):
            if s[i] in brackets_open:
                stackk.append(s[i])
            else:
                if len(stackk) == 0 or \
                (s[i] == ')' and stackk[-1] != '(') or \
                (s[i] == '}' and stackk[-1] != '{') or \
                (s[i] == ']' and stackk[-1] != '['):
                    return False
                else:
                    stackk.pop()
        
        if len(stackk) == 0:
            return True
        else:
            return False

