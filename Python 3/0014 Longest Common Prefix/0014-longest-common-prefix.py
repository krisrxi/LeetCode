class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return("")
        if len(strs) == 1:
            return(str[0])
        
        prefix = strs[0]
        prefixlen = len(pref)

        for string in strs[1:]:
            while prefix != string[0:prefixlen]:
                prefix = prefix[0:(prefixlen - 1)]
                prefixlen -= 1

                if prefixlen == 0:
                    return("")
                
        return(prefix)