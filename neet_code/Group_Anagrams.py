from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_list = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            group_list[key].append(s)
        
        return list(group_list.values())

