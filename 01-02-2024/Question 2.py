Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 
Example 1:
Input: s = "anagram", t = "nagaram" Output: true 
Example 2:
Input: s = "rat", t = "car" Output: false
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        left_products, right_products, result = [1] * n, [1] * n, [1] * n

        left_product, right_product = 1, 1

        for i in range(n):

            left_products[i] = left_product

            right_products[n - 1 - i] = right_product

            left_product *= nums[i]

            right_product *= nums[n - 1 - i]

        for i in range(n):

            result[i] = left_products[i] * right_products[i]

        return result

# Example usage:

nums = [1, 2, 3, 4]

solution = Solution()

result = solution.productExceptSelf(nums)

print(result)
