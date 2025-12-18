from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = defaultdict(int)

        for num in nums:
            topk[num] += 1


        num_ = sorted(topk.items(), key=lambda x:x[1], reverse=True)
        return [k[0] for k in num_[:k]]
