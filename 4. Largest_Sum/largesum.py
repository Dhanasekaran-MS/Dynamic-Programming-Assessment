# Function to find subarray the longest sum
def largest_sum(arr):
    cur_max = glob_max = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        num = arr[i]
        # checking whether the current number itself is greater than cur max + number
        if num > cur_max + num:
            # if number is greater we arr replacing the cur max value to number
            #  storing its index
            cur_max = num
            s = i
        
        else:
            # increasing the cur_max with number
            cur_max += num

        # checking whether current maximum sum is greater than global maximum
        if cur_max > glob_max:
            glob_max = cur_max
        # Recording their starting and ending points
            start = s
            end = i

    return glob_max, arr[start:end+1]


# input Handling
inp = list(map(int,input().split(', ')))
# print(inp)
# Storing the sum and sub arr in two variables
maximum, subarr = largest_sum(inp)
# printing longest subarray and its sum
print(f"Longest subarray : {subarr}\nSum : {maximum}")