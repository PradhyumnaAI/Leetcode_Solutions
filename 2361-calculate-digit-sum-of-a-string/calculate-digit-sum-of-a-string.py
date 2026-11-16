class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        flag = True
        if len(s)<=k:
            return s
        while (True):
            output = []
            for i in range (0,len(s),k):
                out = s[i:i+k]
                output.append(out)
            
            new_output = []
            for j in output:
                summ = 0
                for char in j:
                    summ += int(char)
                new_output.append(str(summ))

            string = ''.join(new_output)
            s = string
            
            if len(string)>k:
                flag = True 
            else :
                flag = False
                break
        return string     





        