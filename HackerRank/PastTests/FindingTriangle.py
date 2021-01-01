def largest_triangle_area(points):
    maximum = 0
    minimum = 0
    N = len(points)
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(i + 2, N):
                (x1, y1), (x2, y2), (x3, y3) = points[i], points[j], points[k]
                triangle_area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                maximum = max(maximum, triangle_area)
                if i == 0 and k == i + 2:
                    minimum = triangle_area
                if triangle_area != 0:
                    minimum = min(minimum, triangle_area)
    print(minimum, maximum)
    return maximum, minimum


amount_of_points = int(input())

matrix = [[0 for x in range(2)] for y in range(amount_of_points)]

for i in range(amount_of_points):
    point = input().split()
    matrix[i][0] = int(point[0])
    matrix[i][1] = int(point[1])

largest_triangle_area(matrix)
