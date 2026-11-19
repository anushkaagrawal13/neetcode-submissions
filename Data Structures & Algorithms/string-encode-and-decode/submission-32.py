class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            ret += f",{len(word)}"
            print(len(word))
        ret += "#"
        for word in strs:
            ret += word
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        if not s:
            return([])
        strs = []
        split = s.split("#", maxsplit=1)
        lens = split[0].split(",")[1:]
        words = "".join(split[1:])
        start_idx = 0
        for str_len in lens:
            int_len = int(str_len)
            end_idx = start_idx + int_len
            strs.append(words[start_idx:end_idx])
            start_idx += int_len
        return strs