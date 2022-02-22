from itertools import count
from typing import List, Optional
from utils.converter import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i*j % k == 0:
                    pairs.append((i, j))

        return len(pairs)


    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0: return []

        res = []

        def recursive(remain, even_num):
            if remain == 0:
                return True

            while remain - even_num >= 0:
                res.append(even_num)
                if recursive(remain-even_num, even_num + 2):
                    return True
                res.pop()
                even_num += 2

            return False

        recursive(finalSum, 2)
        return res

    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        list_indexes = [0] * (n + 1)
        for i in range(n):
            list_indexes[nums2[i]] = i

        res = 0
        for i in range(n):
            before = min(i, list_indexes[nums1[i]])
            after = min(n-1-i, n-1-list_indexes[nums1[i]])
            if before != 0 and after != 0:
                res += before * after
        return res

    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num+1):
            i_lst = list(str(i))
            if sum(list(map(int, i_lst))) % 2 == 0:
                count += 1

        return count

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        head = ListNode()
        head.next = node
        prev_node = head
        zero_node = None
        cur_sum = 0

        while node:
            if node.val == 0:
                if zero_node:
                    new_node = ListNode(cur_sum)
                    prev_node.next = new_node
                    new_node.next = node
                    prev_node = new_node
                    cur_sum = 0
                zero_node = node
                if not node.next:
                    new_node.next = None
            else:
                cur_sum += node.val

            node = node.next
        return head.next

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        from string import ascii_lowercase
        alphabet = ascii_lowercase[::-1]
        d_chars = {}
        for c in s:
            d_chars.setdefault(c, 0)
            d_chars[c] += 1

        new_str = ''
        r = repeatLimit
        is_added = True
        while is_added:
            is_added = False
            for c in alphabet:
                if d_chars.get(c, 0) > 0:
                    if not len(new_str) or c == new_str[-1]:
                        if r > 0:
                            new_str += c
                            r -= 1
                            is_added = True
                            d_chars[c] -= 1
                        else:
                            continue
                    else:
                        new_str += c
                        r = repeatLimit - 1
                        is_added = True
                        d_chars[c] -= 1
                    break
        return new_str

    def coutPairs(self, nums: List[int], k: int) -> int:
        def calc_gcd(n1, n2):
            while n1 != 0 and n2 != 0:
                if n1 > n2:
                    n1 -= n2
                else:
                    n2 -= n1
            return max(n1, n2)

        d_gcd = {}
        res = 0
        for n in nums:
            gcd = calc_gcd(n, k)
            for gcd_j, v in d_gcd.items():
                if gcd * gcd_j % k == 0:
                    res += v
            d_gcd.setdefault(gcd, 0)
            d_gcd[gcd] += 1

        return res


if __name__ == '__main__':
    # finalSum = 8
    # print(Solution().maximumEvenSplit(finalSum))
    nums1 = [4,0,1,3,2]
    nums2 = [4,1,0,2,3]

    nums1 = [2,0,1,3]
    nums2 = [0,1,2,3]

    num = 1000

    # head = [0,3,1,0,4,5,2,0]
    # head = [0,1,0,3,0,2,2,0]
    # head = list_to_linked_list(head)
    # res = Solution().mergeNodes(head)
    # print(linked_list_to_list(res))

    s = 'cczazcc'
    repeatLimit = 3
    s = 'abc'
    repeatLimit = 3

    nums = [1,2,3,4,5]
    k = 2
    nums = [1,2,3,4]
    k = 5
    # nums = [3,2,6,1,8,4,1]
    # k = 3
    # nums = [8,10,2,5,9,6,3,8,2]
    # k = 6
    # nums = [7,4,4,4,6,4]
    # k = 2
    print(Solution().coutPairs(nums, k))
