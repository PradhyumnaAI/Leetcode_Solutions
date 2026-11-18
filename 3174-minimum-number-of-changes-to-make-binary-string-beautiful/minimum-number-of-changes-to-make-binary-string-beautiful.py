class Solution:
    def minChanges(self, s: str) -> int:
        string = []
        count = 0
        for i in range (0,len(s),2):
            
            string.append(s[i:i+2])

        for i in string :
            if i == "01":
                count+=1
            elif i =="10":
                count+=1
        return count



        

        