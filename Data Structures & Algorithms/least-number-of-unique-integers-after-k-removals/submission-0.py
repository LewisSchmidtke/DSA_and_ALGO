class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k == 0:
            return len(set(arr))

        count = 0

        freq = defaultdict(int)
        for x in arr:
            freq[x] += 1
        
        mapping = [(count, val) for val, count in freq.items()]
        heapq.heapify(mapping)

        while mapping and k >= 0:
            c, _ = heapq.heappop(mapping)
            if k - c < 0:
                return len(mapping) + 1
            
            k -= c
        
        return len(mapping)

