class Solution:
    def reverseVowels(self, s: str) -> str:
        s=[i for i in s]
        i,j=0,len(s)-1
        v='aeiouAEIOU'
        while i<j:
            if s[i] in v and s[j] in v:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            if s[i] in v and s[j] not in v or s[j] not in v:
                j-=1
            if s[i] not in v and s[j] in v or s[i] not in v:
                i+=1
        return ''.join(s)
                        