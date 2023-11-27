from statistics import mean


def pearson_correlation(x, y):
    n = len(x)

    mean_x = mean(x)
    mean_y = mean(y)

    cov = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    var_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    var_y = sum((y[i] - mean_y) ** 2 for i in range(n))

    correlation = cov / (var_x ** 0.5 * var_y ** 0.5)

    return correlation


array1 = [1, 2, 3, 4, 10]
array2 = [5, 4, 3, 2, 1]

corr = pearson_correlation(array1, array2)
print(f'Корреляция Пирсона между массивами: {corr}')

# При написании кода использованы :
# - процедурная парадигма, т.к. создана функция def pearson_correlation
# - структурная парадигма - использование цикла for
# - функциональная парадигма - использование математических функций и генертора
