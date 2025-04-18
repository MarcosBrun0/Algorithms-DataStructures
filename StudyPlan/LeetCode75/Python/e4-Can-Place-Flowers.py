
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        

        plot = 0
        while plot < len(flowerbed):
            empty_left = ( plot == 0 or flowerbed[plot -1] == 0 )
            empty_right = ( plot == len(flowerbed)-1 or flowerbed[plot + 1 ] == 0 )

            if empty_left and empty_right and flowerbed[plot]==0:
                flowerbed[plot] = 1
                plot += 1
                n -= 1
            if n <= 0:
                return True
            plot += 1
        return False
