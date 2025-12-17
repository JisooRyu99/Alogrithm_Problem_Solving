class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec_a = int(a, 2)
        dec_b = int(b, 2)
        
        return bin(dec_a + dec_b)[2:]



"""
숫자를 int로 변환한 후 더하고 다시 binary로 return
"""

        
