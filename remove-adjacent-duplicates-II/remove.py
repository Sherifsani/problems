def removeDuplicates(s: str, k: int):
    stack = []
    
    for i in range(len(s)):
        if stack and stack[-1][0] == s[i]:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([s[i], 1])
        print(stack)
    
    res = ''
    for char, count in stack:
        res += char * count
    return res


print(removeDuplicates("abcd", 2))