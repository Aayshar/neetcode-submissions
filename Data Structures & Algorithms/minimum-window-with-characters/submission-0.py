class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        count_t = {}

        for char in t:
            if char not in count_t:
                count_t[char] = 1
            else:
                count_t[char] += 1

        left = 0
        right = 0

        need = len(count_t)
        have = 0

        window = {}

        min_length = float("inf")
        result = ""

        while right < len(s):

            current_char = s[right]

            if current_char not in window:
                window[current_char] = 1
            else:
                window[current_char] += 1

            if current_char in count_t:
                if window[current_char] == count_t[current_char]:
                    have += 1

            while have == need:

                window_length = right - left + 1

                if window_length < min_length:
                    min_length = window_length
                    result = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in count_t:
                    if window[left_char] < count_t[left_char]:
                        have -= 1

                left += 1

            right += 1

        return result