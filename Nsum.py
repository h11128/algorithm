def fourSum(nums, target, N):
    def findNsum(nums, target, N, result, results):
        nums.sort()
        if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N: return
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l = l +1
                elif s < target:
                    l = l + 1
                else: r = r - 1
        else:
            for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result + [nums[i]], results)

    results = []
    findNsum(sorted(nums), target, N, [], results)
    return results
nums = [1, 0, -1, 0, -2, 2]
target = 0
results = fourSum(nums, target, 4)
print(results)
