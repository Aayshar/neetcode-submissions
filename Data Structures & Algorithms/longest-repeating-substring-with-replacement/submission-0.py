class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        left = 0
        max_frequency = 0
        longest = 0

        for right in range(len(s)):

            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1

            max_frequency = max(
                max_frequency,
                count[s[right]]
            )

            window_length = right - left + 1

            replacements_needed = window_length - max_frequency

            if replacements_needed > k:
                count[s[left]] -= 1
                left += 1

            current_window_length = right - left + 1

            longest = max(
                longest,
                current_window_length
            )

        return longest