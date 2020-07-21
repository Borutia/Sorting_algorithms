
def bubble_sort(l):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True


def main():
    l = [2,4,5,2,3,6,6,3,4,6,7,5,3,2,4,6,7]
    bubble_sort(l)
    print(l)


if __name__ == '__main__':
    main()
