class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for i in strs:
            r=tuple(sorted(i))
            if r in result:
                result[r].append(i)
            else:
                result[r]=[i]
        return list(result.values())