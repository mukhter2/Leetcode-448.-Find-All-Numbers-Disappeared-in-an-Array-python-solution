# Leetcode 448. Find All Numbers Disappeared in an Array Python Solution
## Problem Statement 
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
## Examples
Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:
Input: nums = [1,1]
Output: [2]
## Constraints
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
## Methodology
Step 1: Create a counting array with length of n+1, where n is the size of the nums
Step 2: Loop through the counting array to check if any index has no count ad store them into another list
Step 3: Return the list
