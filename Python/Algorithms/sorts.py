"""sorts.py - Python implementations of merge and bubble sort.
by Giovanni Prinzivalli"""

def bubble_sort(arr):
    """Python bubble sort for a list of comparables."""
    idx = len(arr)
    while idx > 0:
        print arr
        temp_idx = 0
        for i in range(1, idx):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i-1]
                temp_idx = i
        idx = temp_idx

def merge_sort(arr):
    """Python merge sort for a list of comparables."""
    if len(arr) <= 1:
        return arr

    middle = int(len(arr) / 2)

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

def merge(left, right):
    """Merge helper function that preforms the actual sort."""
    print "Unmerged: ", left, ", ", right
    arr = []
    while len(left) and len(right):
        if left[0] < right[0]:
            arr.append(left.pop(0))
        else:
            arr.append(right.pop(0))
    for val in left:
        arr.append(val)
    for val in right:
        arr.append(val)

    print "Merged: ", arr
    return arr

if __name__ == "__main__":
    import random
    bub_arr = random.sample(xrange(200), 25)
    print "Running Bubble Sort..."
    bubble_sort(bub_arr)
    print "Bubble Sort output:"
    print bub_arr

    mer_arr = random.sample(xrange(200), 25)
    print "Running Merge Sort..."
    merged = merge_sort(mer_arr)
    print "Merge Sort output:"
    print merged

