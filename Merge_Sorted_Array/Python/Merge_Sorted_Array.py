class Solution:A
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m):
            nums2.append(nums1[i])

        vetor = nums2
        vetortemp = []
        for a in range(0, len(vetor)):
            for b in range(0, len(vetor)):
                if vetor[a] <= vetor[b]:
                    temp = vetor[a]
                    vetor[a] = vetor[b]
                    vetor[b] = temp

        for b in range(m+n):
            nums1[b] = vetor[b]

#there` a lot to improve but for the first leetcode that I solved it`s okay
