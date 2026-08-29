class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        left = 0
        max_length = 0
        max_freq = 0
        
        for right in range(len(s)):
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1
            max_freq = max(max_freq, hash_map[s[right]])
            window_size = right - left + 1
            if window_size - max_freq > k:
                hash_map[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            
        return max_length