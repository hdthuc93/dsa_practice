def binary_search(lst, l, r, target):
    if l > r:
        return l

    m = (l + r) // 2

    if lst[m] == target:
        while m < len(lst) and lst[m] == target:
            m += 1
        return m - 1
    elif lst[m] > target:
        return binary_search(lst, l, m - 1, target)

    return binary_search(lst, m + 1, r, target)


lst = [1, 4, 8, 10]
lst = [1, 4, 8, 10, 15]
lst = [1, 15]
target = 1

print(binary_search(lst, 0, len(lst) - 1, target))
