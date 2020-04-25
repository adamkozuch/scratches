def get_longest_sequence(arr):
    if len(arr) < 3:
        return len(arr)
    first = 0
    second = None
    length = 0
    for i in range(1, len(arr)):
        if arr[first] == arr[i] or (second and arr[second]== arr[i]):
            continue
        if not second:
            second = i
            continue
        if i - first > length:
            length = i - first
        first = second
        second = i

    if len(arr) - first > length:
        length = len(arr) - first

    return length


print(get_longest_sequence([1]))
print(get_longest_sequence([5,1,2,1,2,5]))
