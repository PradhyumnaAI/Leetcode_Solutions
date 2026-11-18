class Solution:
    def minChanges(self, s: str) -> int:
        string = []
        count = 0
        for i in range (0,len(s),2):
            string = s[i:i+2]
            if string == "01":
                count+=1
            elif string =="10":
                count+=1
            
            

        
        return count



        

        