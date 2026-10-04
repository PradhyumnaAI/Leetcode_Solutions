class Solution:
    def checkValidString(self, s: str) -> bool:
        bracket = list(s)
        
        # Pass 1: Left to Right
        # Check if there are too many ')'
        balance = 0
        for char in bracket:
            if char in ('(', '*'):
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        # Pass 2: Right to Left
        # Check if there are too many '('
        balance = 0
        for char in reversed(bracket):
            if char in (')', '*'):
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        return True