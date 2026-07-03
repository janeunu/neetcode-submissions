class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 

        for s in strs:
            count = [0]*26 # 1 for each char a .. z

            for c in s:
                count[ord(c)-ord("a")]+= 1 # converts each char into index

            res[tuple(count)].append(s)
        
        return list(res.values())