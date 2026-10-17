class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(s: str, i: int) -> tuple[set[str], int]:
            # Each expression level maintains a list of product terms (union)
            terms = [set([""])]
            
            while i < len(s):
                if s[i] == '}':
                    i += 1
                    break
                elif s[i] == ',':
                    # Start a new union term
                    terms.append(set([""]))
                    i += 1
                elif s[i] == '{':
                    # Parse the nested expression inside the braces
                    sub_set, i = parse(s, i + 1)
                    # Concatenate the sub_set with the current active term
                    terms[-1] = {a + b for a in terms[-1] for b in sub_set}
                else:
                    # Parse a contiguous string of lowercase letters
                    j = i
                    while j < len(s) and s[j].isalpha():
                        j += 1
                    letter = s[i:j]
                    # Concatenate the letter with the current active term
                    terms[-1] = {a + letter for a in terms[-1]}
                    i = j
                    
            # Combine all comma-separated union terms
            return set().union(*terms), i

        result, _ = parse(expression, 0)
        return sorted(list(result))