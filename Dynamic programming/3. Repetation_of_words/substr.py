def repetation(string, word):
    counts = 0
    k = 1
    while True:
        # Checking Whether k times word repetation(continuous)
        # 'substring' present in string (sequence) 
        if word * k in string:
            counts = k
            k += 1
        else:
            break
    return counts

# Handling input
s = input()
w = input()
print(repetation(s,w))
