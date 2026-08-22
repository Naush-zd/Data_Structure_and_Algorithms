class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapp={}
        for i in s:
            mapp[i]= mapp.get(i,0)+1
        for i in t:
            mapp[i]= mapp.get(i,0)-1
        return all(value==0 for value in mapp.values())
        
