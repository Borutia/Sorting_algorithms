
def heapify(l, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and l[left_child] > l[largest]:
        largest = left_child

    if right_child < heap_size and l[right_child] > l[largest]:
        largest = right_child

    if largest != root_index:
        l[root_index], l[largest] = l[largest], l[root_index]
        heapify(l, heap_size, largest)


def heap_sort(l):
    n = len(l)

    for i in range(n, -1, -1):
        heapify(l, n, i)

    for i in range(n - 1, 0, -1):
        l[i], l[0] = l[0], l[i]
        heapify(l, i, 0)


def main():
    l = [2,4,5,2,3,6,6,3,4,6,7,5,3,2,4,6,7]
    heap_sort(l)
    print(l)


if __name__ == '__main__':
    main()
