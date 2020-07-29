
def partition(l, low, high):
    pivot = l[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while l[i] < pivot:
            i += 1

        j -= 1
        while l[j] > pivot:
            j -= 1

        if i >= j:
            return j

        l[i], l[j] = l[j], l[i]


def quick_sort(l):
    def _quick_sort(items, low, high):
        if low < high:
            part = partition(items, low, high)
            _quick_sort(items, low, part)
            _quick_sort(items, part + 1, high)

    _quick_sort(l, 0, len(l) - 1)


def main():
    l = [2,4,5,2,3,6,6,3,4,6,7,5,3,2,4,6,7]
    quick_sort(l)
    print(l)


if __name__ == '__main__':
    main()
