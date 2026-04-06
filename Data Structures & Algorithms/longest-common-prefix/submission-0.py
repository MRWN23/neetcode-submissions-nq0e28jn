class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lgp = strs[0]
        for word in strs[1:]:
            while not word.startswith(lgp):
                lgp = lgp[:-1]
                if not lgp:
                    return ""
                

                
        return lgp