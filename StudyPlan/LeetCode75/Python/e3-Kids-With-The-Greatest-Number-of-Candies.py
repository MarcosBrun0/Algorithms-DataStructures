class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        array = []
        for n in range(0, len(candies)):
            array.append(True)
        
        for i in range(0,len(candies)):
            for j in range(0,len(candies)):
                if candies[i]+extraCandies < candies[j]:
                    array[i] = False

        return array
