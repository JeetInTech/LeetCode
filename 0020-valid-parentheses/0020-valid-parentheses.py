class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        
        return dp[len(s)][len(p)]
    
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            max_water = max(max_water, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
    
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_numeral = ""
        
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                roman_numeral += symbols[i]
        
        return roman_numeral
    
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            current_value = roman_dict[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        
        return total
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
    
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current: str, open_count: int, close_count: int):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        result = []
        backtrack("", 0, 0)
        return result
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = second = dummy
        
        for _ in range(n + 1):
            first = first.next
        
        while first:
            first, second = first.next, second.next
        
        second.next = second.next.next
        return dummy.next
    
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack