import heapq

def findGreater(num):
    """
    findGreater takes a number and outputs the next greatest number that is a
    permutation of the input number.

    """
    digits = [int(i) for i in str(num)]
    n = len(digits)

    # use heap to track minimum digits seen so far
    heap = []

    for i in reversed(range(n)):

        curr_val = digits[i]
        next_val = digits[i-1]
        heapq.heappush(heap, (curr_val, i))

        if curr_val > next_val:
            (ele, idx) = heapq.heappop(heap)
            while ele < next_val:
                (ele, idx) = heapq.heappop(heap)
            digits[i-1], digits[idx] = digits[idx], digits[i-1]
            digits[i:] = sorted(digits[i:])
            break

    result = int("".join(map(str, digits)))
    return result
