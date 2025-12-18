class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j + 1 + length
        return result


"""
시행착오: 일반적으로 Encode에서 "".join / decoder에서 split()을 했을 경우
빈 공백이 들어오면 처리를 못함. 확실한 구분자를 사용해야함
"""
        
        
