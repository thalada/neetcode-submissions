class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_cntr = Counter(s)
        print(s_cntr)

        t_cntr = Counter(t)
        print(t_cntr)

        for s in s_cntr:
            if s in t_cntr and s_cntr[s] == t_cntr[s]:
                continue
            else:
                return False
        for t in t_cntr:
            if t in s_cntr and t_cntr[t] == s_cntr[t]:
                continue
            else:
                return False

        return True
        