class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the cleaned string is equal to its reverse
        return cleaned == cleaned[::-1]