
## Brute Force Approach

# def non_repeat(s):
#     mx = 0
#     cur=[]
#     for i in s:
#         if i not in cur:
#             cur.append(i)
#         else:
#             mx =  max(mx,len(cur))
#             cur=[]
#     return max(mx,len(cur))

def non_repeat(s):
    mx = 0
    cur = []
    for i in s:
        if i not in cur:
            cur.append(i)
        else:
            mx = max(mx, len(cur))
            cur = cur[cur.index(i) + 1:]  # To Remove Repeated character (upto)
            cur.append(i)
    return max(mx, len(cur))

s = input()
print(non_repeat(s))