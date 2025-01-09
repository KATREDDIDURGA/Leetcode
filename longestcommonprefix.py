class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 1000
        for i in range(len(strs)):
            if len(strs[i])<min_len:
                min_len = len(strs[i])
        p = []
        for letters in range(min_len):
            char = strs[0][letters]
            for words in range(1, len(strs)):
                if strs[words][letters] != char:
                    return ''.join(p)
            p.append(char)

        return ''.join(p)


