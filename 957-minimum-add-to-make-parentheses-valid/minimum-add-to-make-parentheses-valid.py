class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        openBracket  = 0
        unmatched = 0
        for i in range (n):
            if s[i] == '(':
                openBracket +=1
            elif s[i] == ')':
                if openBracket >0 :
                    openBracket -=1
                elif openBracket == 0:
                    unmatched +=1
        total = unmatched + openBracket
        return total 

        


            

        