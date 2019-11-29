# Double array for quick lookup.
def minimumSwaps(arr):
    # array of all indexes for each value
    # indexes is 0 based.
    indexes = [0] * len(arr)
    for pos, val in enumerate(arr):
        indexes[val - 1] = pos

    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i + 1:
            tmp = arr[i]

            # sets the current index to the array.
            arr[i] = i + 1
            # find the previous value index from indexes
            # and set the tmp value to where the index was.
            arr[indexes[i]] = tmp

            # modify the indexes array accordingly
            indexes[tmp - 1] = indexes[i]
            indexes[i] = i

            swaps += 1

    return swaps


minimumSwaps([5, 3, 2, 1])
