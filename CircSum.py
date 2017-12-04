# Day 1 - The captcha requires you to review a sequence of digits (your puzzle input)
# and find the sum of all digits that match the next digit in the list. 
# The list is circular, so the digit after the last digit is the first digit in the list.

def getSum(nums):
	tot = 0
	nums = [int(n) for n in nums]
	length = len(nums)
	for i, n in enumerate(nums):
		if i <length-1:
			if nums[i]==nums[i+1]:
				tot+=nums[i]
		else:
			if nums[i]==nums[0]:
				tot+=nums[i]
	return tot

def getHalfSum(nums):
	tot = 0
	nums = [int(n) for n in nums]
	length = len(nums)
	dist = int(length/2)
	for i, n in enumerate(nums):
		if nums[i]==nums[(i+dist)%length]:
			tot+=nums[i]
	return tot