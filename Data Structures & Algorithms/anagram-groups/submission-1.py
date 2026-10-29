class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        res = []

        for s in strs:
            c_vector = [0] * 26
            for c in s:
                index = ord(c) - ord("a")
                c_vector[index] += 1

            c_vector = tuple(c_vector)

            if c_vector in anagrams:
                anagrams[c_vector].append(s)

            else:
                anagrams[c_vector] = [s]

        for key, value in anagrams.items():
            res.append(value)
            
        
        return res