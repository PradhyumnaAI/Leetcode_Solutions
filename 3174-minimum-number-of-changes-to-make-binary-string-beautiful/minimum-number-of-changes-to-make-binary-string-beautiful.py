class Solution:
    def minChanges(self, s: str) -> int:
        
        count = 0
        for i in range (0,len(s),2):
            string = s[i:i+2]
            if string == "01" or string =="10":
                count+=1
            
            
            

        
        return count



        

        