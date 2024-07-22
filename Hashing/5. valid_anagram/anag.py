# approach BRUTE FORCE
# def anag(s,t):
#     if sorted(s) == sorted(t):
#         return 'true'
#     else:
#         return 'false'
    
def anag(s,t):
    h1={}
    h2={}
    for i in s:
        if i not in h1:
            h1[i]=1
        else:
            h1[i] += 1
    for i in t:
        if i not in h2:
            h2[i]=1
        else:
            h2[i] += 1
    if h1==h2:
        return 'true'
    else:
        return 'false'

s = input()
t = input()
print(anag(s,t))