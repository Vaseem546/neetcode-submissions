class Solution:
    def isValid(self, s: str) -> bool:
        valid_string=[]
        if len(s)<2:
            return False
        else:
            for i in s:
                if i == ("[") or i==("{") or i==("(") :
                    valid_string.append(i)
                else:
                    if not valid_string:
                        return False
                    last_item = valid_string.pop()
                    if (i == ")" and last_item != "(") or  (i == "]" and last_item != "[") or  (i == "}" and last_item != "{"):
                        return False
                    
        return len(valid_string) ==0

        