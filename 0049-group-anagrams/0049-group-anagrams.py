class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct={}
        lst=[]
        for r in strs:
            tup=tuple(sorted(r))
            if tup in dct:
                dct[tup].append(r)
            else:
                dct[tup]=[r] 
        for d in dct:
            lst.append(dct[d])             
        return lst   