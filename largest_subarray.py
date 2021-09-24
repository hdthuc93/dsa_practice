
def find_largestsubarray_topdown(arr, ifrom, ito, current_max, cache):
    if cache.get("{}_{}".format(ifrom, ito)):
        return cache.get("{}_{}".format(ifrom, ito))
    if ito - ifrom == 1:
        return max(arr[ifrom], current_max)

    current_max = max(current_max, sum(arr[ifrom:ito]))
    cache["{}_{}".format(ifrom, ito)] = current_max

    current_max = max(current_max, find_largestsubarray_topdown(arr, ifrom+1, ito, current_max, cache))
    return max(current_max, find_largestsubarray_topdown(arr, ifrom, ito-1, current_max, cache))


def find_largestsubarray_bottomup(arr):
    max_sum = -1e10
    continuous_sum = 0
    for val in arr:
        continuous_sum = continuous_sum + val if continuous_sum > 0 else val
        max_sum = max(continuous_sum, max_sum)

    return max_sum


if __name__ == '__main__':
    arr = [-3, 1, -8, 4, -1, 2, 1, -5, 5]
    cache = {}
    print('find_largestsubarray_topdown', find_largestsubarray_topdown(arr, 0, len(arr), -1e10, cache))
    print('find_largestsubarray_bottomup', find_largestsubarray_bottomup(arr))
