class Solution:
    def isValid(self, s: str) -> bool:


        # brute force approach

        # while (
        #     "()" in s
        #     or "[]" in s
        #     or "{}" in s
        # ):
        #     s = s.replace("()", "")
        #     s = s.replace("[]", "")
        #     s = s.replace("{}", "")

        # return s == ""

        stack = []

        matching_brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for current_bracket in s:

            # Opening bracket
            if current_bracket not in matching_brackets:
                stack.append(current_bracket)

            # Closing bracket
            else:

                # No opening bracket available
                if not stack:
                    return False

                # Top opening bracket does not match
                if stack[-1] != matching_brackets[current_bracket]:
                    return False

                # Matching pair found
                stack.pop()

        return len(stack) == 0