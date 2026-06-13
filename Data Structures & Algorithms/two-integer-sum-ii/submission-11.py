class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0 
        end = len(numbers) - 1
        while start < end:
            print(numbers[start])
            print(numbers[end])
            if (target - numbers[start]) == numbers[end]:
                return [start + 1, end + 1]
            else:
                if (target - numbers[start]) > numbers[end]:
                    start += 1
                    continue
                if (target - numbers[start]) < numbers[end]:
                    end -= 1
                    continue
                
            
                

        

