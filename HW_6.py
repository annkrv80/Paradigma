# Функция для бинарного поиска
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 11, 13]
    target = 5

    result = binary_search(array, target)
    print("Индекс искомого элемента:", result)


# При написании кода использованы процедурная, структурная парадигмы.
# Процедурная парадигма основана на вызове процедур.
# В моем коде создана процедура binary_search()
# Внутри процедуры использована структурная парадигма, код структурирован, имеет конструкции while и if
# не используется "goto".