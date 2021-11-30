class Solution:
    def isValid(self, s: str) -> bool:
        Bracket1 = ["(", ")"]
        Bracket1 = ["[", "]"]
        Bracket1 = ["{", "}"]
        result = True
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == "[":
                stack.append(s[i])
            elif s[i] == "{":
                stack.append(s[i])

            if s[i] == ")":
                if len(stack):
                    tmp = stack.pop()
                    if tmp != "(":
                        result = False
                else:
                    result = False

            if s[i] == "]":
                if len(stack):
                    tmp = stack.pop()
                    if tmp != "[":
                        result = False
                else:
                    result = False

            if s[i] == "}":
                if len(stack):
                    tmp = stack.pop()
                    if tmp != "{":
                        result = False
                else:
                    result = False
        if len(stack):
            result = False
        return result


s = "(]"
solution = Solution()
print(solution.isValid(s))
