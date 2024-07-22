def anagrams(strs):
    hash={}
    for i in strs:
        x = list(i)
        x.sort()
        x= ''.join(x)
        if x not in hash:
            hash[x] = []
        hash[x] += [i]
    return list(hash.values())

st = input().split()
print(anagrams(st))