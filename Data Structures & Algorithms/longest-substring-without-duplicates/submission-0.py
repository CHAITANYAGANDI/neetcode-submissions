class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        max_value = 0

        freq = dict()

        while right < len(s):
            
            
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            while freq[s[right]] > 1:
            
                freq[s[left]] = freq[s[left]] - 1
                
                if freq[s[left]] == 0:
                    
                    freq.pop(s[left])
                    
                left+=1
                
            current_value = right - left + 1
            
            max_value = max(max_value,current_value)
                    
            
            right+=1
    
    
        return max_value
        