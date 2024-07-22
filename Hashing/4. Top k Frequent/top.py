def frequent(nums, k):
    hash = {}
    for i in nums:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    
    # Sort the dictionary items by their frequency in descending order
    sorted_hash = sorted(hash.items(), key=lambda x: x[1], reverse=True)
    
    # Extract the top k frequent elements
    res = [i[0] for i in sorted_hash[:k]]
    return res

# Input Handling
nums = list(map(int, input().split()))
k = int(input())

print(frequent(nums, k))