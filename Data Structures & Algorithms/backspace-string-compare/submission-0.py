class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_new = []
        for c in s:
            if c == '#':
                if s_new:
                    s_new.pop()
                continue
            s_new.append(c)

        t_new = []
        for c in t:
            if c == '#':
                if t_new:
                    t_new.pop()
                continue
            t_new.append(c)

        return "".join(s_new) == "".join(t_new)
