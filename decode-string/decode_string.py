def decodeString(s: str) -> str:
    # Each stack frame saves the string built before the "[" and the repeat count
    # so we can resume the outer context after closing "]".
    stack = []
    curr_str = ""
    curr_num = 0

    for c in s:
        if c.isdigit():
            # Accumulate digits to support multi-digit multipliers (e.g., "12[a]")
            curr_num = curr_num * 10 + int(c)
        elif c == "[":
            # Freeze the current context and start a fresh one inside the brackets
            stack.append((curr_str, curr_num))
            curr_str = ""
            curr_num = 0
        elif c == "]":
            # Restore the outer context, appending the repeated inner string
            prev_str, num = stack.pop()
            curr_str = prev_str + num * curr_str
        else:
            curr_str += c

    return curr_str


res = decodeString("3[a]2[bc]")
print(res)  # aaabcbc
