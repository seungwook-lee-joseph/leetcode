class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1 :
            return False
        else :
            stack = []
            for i in range(0, len(s)):
                if s[i] in ('(','[','{'):
                    stack.append(s[i])
                else:
                    if len(stack) == 0:
                        return False
                    poped = stack.pop()
                    if (poped == '(') and (s[i] == ')'):
                        pass
                    elif (poped == '[') and (s[i] == ']'):
                        pass
                    elif (poped == '{') and (s[i] == '}'):
                        pass
                    else:
                        return False
            if len(stack) == 0:
                return True
            else:
                return False
