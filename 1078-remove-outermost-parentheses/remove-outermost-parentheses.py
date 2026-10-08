class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0 
        string1 = []
        output = []
        n = len(s)
        if n==2:
            return ""
        for i in s:
            if i == '(':
                depth +=1
                string1.append(i)
            else :
                depth-=1
                string1.append(i)
                if depth == 0 :
                    string2 = "".join(string1)
                    string3 = string2[1:-1]
                    output.append (string3)

                    string1 = []
        output1 = "".join(output)
        return output1
        





        
        
        