class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Append the length of the string, a '#', and then the string itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            # Find the position of the next '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # The number before the '#' tells us the length of the word
            length = int(s[i:j])
            
            # Extract the actual word using the length
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Move the pointer to the start of the next encoded string
            i = j + 1 + length
            
        return res