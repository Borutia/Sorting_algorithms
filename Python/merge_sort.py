def merge(left_l, right_l):
    temp_list = []
    left_index = 0
    right_index = 0
    for i in range(len(left_l) + len(right_l)):
        if left_index < len(left_l) and right_index < len(right_l):
            if left_l[left_index] < right_l[right_index]:
                temp_list.append(left_l[left_index])
                left_index += 1
            elif left_l[left_index] > right_l[right_index]:
                temp_list.append(right_l[right_index])
                right_index += 1
            elif left_l[left_index] == right_l[right_index]:
                temp_list.append(right_l[right_index])
                right_index += 1
        elif left_index == len(left_l):
            temp_list.append(right_l[right_index])
            right_index += 1
        elif right_index == len(right_l):
            temp_list.append(left_l[left_index])
            left_index += 1

    return temp_list


def merge_sort(l):
    if len(l) <= 1:
        return l

    mid = len(l) // 2

    left_l = merge_sort(l[:mid])
    right_l = merge_sort(l[mid:])

    return merge(left_l, right_l)


def main():
    l = [2,4,5,2,3,6,6,3,4,6,7,5,3,2,4,6,7]
    l = merge_sort(l)
    print(l)


if __name__ == '__main__':
    main()
