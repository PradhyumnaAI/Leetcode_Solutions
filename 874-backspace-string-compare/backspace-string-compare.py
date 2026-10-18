class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        output = []
        for i in s: 
            if i !='#':
                stack1.append(i)

            if i =='#':
                if len(stack1)==0:
                    continue 
                else :
                    stack1.pop()
        for j in t:
            if j !='#':
                stack2.append(j)
                
            if j =='#':
                if len(stack2)==0:
                    continue 
                else :
                    stack2.pop()
        
        if len(stack1)==len(stack2):
            for i in range(len(stack1)):
                if stack1[i]==stack2[i]:
                    output.append (True)
                else:
                    output.append(False)
        else:
            return False

        if not all(output): 
            return False
        return True






        
        
            
        