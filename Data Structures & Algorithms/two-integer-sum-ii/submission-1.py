class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        outputlist = []
        for i in range(len(numbers)):
            j = i + 1
            while j < len(numbers):
                if (numbers[j] + numbers[i]) == target:
                    outputlist.append(i + 1)
                    outputlist.append(j + 1)
                    return outputlist
                else:
                    j += 1
        

