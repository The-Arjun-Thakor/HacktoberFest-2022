class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split()
        
        answer = []
        
        for i in range(len(split_s)):
            reverse_str = list(reversed(split_s[i]))
            answer.append(''.join(reverse_str))
        return ' '.join(answer)
