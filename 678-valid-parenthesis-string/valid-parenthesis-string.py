class Solution:
    def checkValidString(self, s: str) -> bool:
        bracket = list(s)
        balance= 0
        for char in s :
            if char == '(' or char == '*':
                balance +=1
            else:
                balance -=1
            if balance<0:
                return False

        balance= 0
        for char in reversed(s) :
            if char == ')' or char == '*':
                balance +=1
            else:
                balance -=1
            if balance<0:
                return False
        return True

