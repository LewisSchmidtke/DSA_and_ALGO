class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped_chars = set()

        for idx, character in enumerate(s):
            if character not in mapping:
                mapping[character] = t[idx]
                if t[idx] in mapped_chars:
                    return False
                mapped_chars.add(t[idx])
            else:
                if t[idx] != mapping[character]:
                    return False

        return True