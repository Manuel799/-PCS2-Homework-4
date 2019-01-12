def MergeSort(arr):
    l = len(arr)
    if l <= 1:
        return arr

    s = []
    d = []
    for i in range(0, l):
        if i < l // 2:
            s.append(arr[i])
        else:
            d.append(arr[i])

    left = MergeSort(s)
    right = MergeSort(d)

    return merge(left, right)

def merge(a, b):
    a_l = len(a)
    b_le = len(b)
    result = []

    while a or b:
        if not a:
            result.extend(b)
            b.clear()
        elif not b:
            result.extend(a)
            a.clear()
        elif a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))

    return result

with open('rosalind_ms.txt') as f:
    lines = f.read().splitlines()
    arr = [int(x) for x in lines[1].split(' ')]

    print(' '.join(str(x) for x in MergeSort(arr)))
