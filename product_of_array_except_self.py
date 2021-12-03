# https://leetcode.com/problems/product-of-array-except-self/


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products1 = [nums[0]]
        products2 = [nums[-1]]

        for i in range(1, len(nums)):
            products1.append(products1[-1]*nums[i])
        for i in range(len(nums)-2, -1, -1):
            products2.append(products2[-1]*nums[i])
        products2.reverse()

        ans = []
        for i in range(len(nums)):
            left = products1[i-1] if i-1 >= 0 else 1
            right = products2[i+1] if i + 1 < len(products2) else 1
            ans.append(left*right)

        return ans

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        ans = [1]
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            ans.append(product)

        product = 1
        for i in range(len(nums)-2, -1, -1):
            product *= nums[i+1]
            ans[i] *= product

        return ans


if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf2(nums))
