def pascal_triangle(n):
    if n <= 0:
        return []
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            result.append([1] + [result[i-1][j] + result[i-1][j+1] for j in range(i-1)] + [1])
    return result
