class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {"I":1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000
                        }
        d = len(s)
        total = 0

        for i in range(d):
            value = symbol_value[s[i]]
            if i+1<d and value<symbol_value[s[i+1]]:
                total = total - value
            else:
                total = total + value
        return total

        




        
