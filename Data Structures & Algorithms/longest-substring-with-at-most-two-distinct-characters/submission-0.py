class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_length = 0
        count = 0
        right = 0
        left = 0
        char_map = {}

        while right < len(s):
            if s[right] not in char_map:
                char_map[s[right]] = 1
            else:
                char_map[s[right]] += 1
            count += 1
            while len(char_map) > 2:
                char_map[s[left]] -= 1
                count -= 1
                if char_map[s[left]] == 0:
                    char_map.pop(s[left])
                left += 1
            
            max_length = max(max_length, count)
            right += 1
        
        max_length = max(max_length, count)

        return max_length     