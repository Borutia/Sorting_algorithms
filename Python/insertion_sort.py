
def insertion_sort(l):
    for i in range(1, len(l)):
        val_insert = l[i]
        j = i - 1
        while 0 <= j and val_insert <= l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = val_insert


def main():
    l = [2,4,5,2,3,6,6,3,4,6,7,5,3,2,4,6,7]
    insertion_sort(l)
    print(l)


if __name__ == '__main__':
    main()
