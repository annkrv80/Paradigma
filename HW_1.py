def sort_list_imperativa(array):
    for i in range(len(array)):
        max_index = i
        for j in range(i+1, len(array)):
            if array[j] > array[max_index]:
                max_index = j
        array[i], array[max_index] = array[max_index], array[i]
    return array


def sort_list_declarative(array):
    return sorted(array, reverse=True)


if __name__ == '__main__':
    numbers = [2, 4, 8, 101, 55, -16]
    sort_number = sort_list_imperativa(numbers)
    sort_num = sort_list_declarative(numbers)
    print(sort_number)
    print(sort_num)
