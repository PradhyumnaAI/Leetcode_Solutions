class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        n1 = len(arr1)
        n2 = len(arr2)
        count=0
        flag = False 
        for i in range (n1):
            flag = False
            for j  in range(n2):
                if abs(arr1[i]-arr2[j])<= d:
                    flag = True
            if flag :
                count+=1

                    
                    
        return n1-count

        