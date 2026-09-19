#Practice Questions:

#1. Two Sum – LeetCode 1: Two Sum

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

from symtable import Class


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []

#2. Contains Duplicate – LeetCode 217: Contains Duplicate
# Input: nums = [1,2,3,1]
# Output: true
# Explanation: The value 1 appears twice in the array.
nums = [1,2,3,1]
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
contains_duplicate = Solution().containsDuplicate(nums)
print("Contains Duplicate:", contains_duplicate)
#3. Valid Anagram – LeetCode 242: Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Explanation: Both strings contain the same characters with the same frequencies.

class AnagramSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        return len(char_count) == 0

#4. Move Zeroes – LeetCode 283: Move Zeroes
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Explanation: All zeros are moved to the end of the array.

class MoveSolution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
move_zeroes_result = MoveSolution().moveZeroes([0,1,0,3,12])
print("After moving zeroes:", move_zeroes_result)
#5. Remove Duplicates from Sorted Array – LeetCode 26: Remove Duplicates from Sorted Array
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: The function should return the new length of the array without duplicates.

class RemoveDuplicatesSolution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        return left + 1
remove_duplicates_result = RemoveDuplicatesSolution().removeDuplicates([1,1,2])
print("New length after removing duplicates:", remove_duplicates_result)
#6. Valid Palindrome – LeetCode 125: Valid Palindrome
# Input: s = "A man a plan a canal Panama"
# Output: true
# Explanation: The string is a palindrome when ignoring case and non-alphanumeric characters.

class PalindromeSolution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]
palindrome_result = PalindromeSolution().isPalindrome("A man a plan a canal Panama")
print("Is valid palindrome:", palindrome_result)

#7. Squares of a Sorted Array – LeetCode 977: Squares of a Sorted Array
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: The squares of the numbers are sorted in non-decreasing order.

class SquaresSolution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Optimization: use two pointers to fill the result array from the end
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result
sorted_squares_result = SquaresSolution().sortedSquares([-4,-1,0,3,10])
print("Sorted squares:", sorted_squares_result)

#8. Maximum Average Subarray I – LeetCode 643: Maximum Average Subarray

class MaxAverageSolution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        return max_sum / k
max_average_result = MaxAverageSolution().findMaxAverage([1,12,-5,-6,50,3], 4)
print("Maximum average subarray:", max_average_result)
#9. Minimum Size Subarray Sum – LeetCode 209: Minimum Size Subarray Sum

class MinSizeSubarraySolution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0
min_size_subarray_result = MinSizeSubarraySolution().minSubArrayLen(7, [2,3,1,2,4,3])
print("Minimum size subarray length:", min_size_subarray_result)    
#10. 3Sum – LeetCode 15: 3Sum
class ThreeSumSolution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
three_sum_result = ThreeSumSolution().threeSum([-1,0,1,2,-1,-4])
print("3Sum result:", three_sum_result)