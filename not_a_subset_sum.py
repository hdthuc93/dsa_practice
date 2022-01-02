# https://practice.geeksforgeeks.org/problems/smallest-number-subset1220/1


class Solution:
    def findSmallest(self, arr, n):
        m = 1
        for i in range(n):
            if m >= arr[i]:
                m += arr[i]

        return m


if __name__ == '__main__':
    arr = [1,2,3,7]
    # arr = [1, 2, 3]
    # arr = [3, 6, 9, 10, 20, 28]
    # arr = [1, 1, 9, 15, 30, 76, 99]
    # arr = [1]*1000000
    print(Solution().findSmallest(arr, len(arr)))
