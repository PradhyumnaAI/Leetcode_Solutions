class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num1 = "".join(map(str, digits))
        num2 = str(int(num1)+1)
        output = []

        for i in num2 :
            output.append(int(i))

        return output

