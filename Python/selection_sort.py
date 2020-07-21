
def selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]

def main():
    l = [2,4,5,2,3,6]
    selection_sort(l)
    print(l)


if __name__ == '__main__':
    main()
