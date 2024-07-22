# def find_target(nums, target):
#     sums=[]
#     for i in range(0,len(nums)-1):
#         if nums[i] + nums[i+1] == target:
#             sums = [i,i+1]

#     return sums


def find_target(nums, target):
    hash= {}
    for index,num in enumerate(nums):
        cur = target-num
        if cur in hash:
            return [hash[cur], index]
        hash[num] = index
        
nums = list(map(int,input().split()))
target = int(input())
print(find_target(nums, target))
