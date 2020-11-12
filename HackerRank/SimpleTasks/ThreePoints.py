a_point = [float(i) for i in input().split(" ")]
b_point = [float(i) for i in input().split(" ")]
c_point = [float(i) for i in input().split(" ")]

x_a, y_a = a_point[0], a_point[1]
x_b, y_b = b_point[0], b_point[1]
x_c, y_c = c_point[0], c_point[1]

if x_a == x_b and y_a == y_b:
    print(True)
elif x_a == x_b or x_c == x_b or x_a == x_c:
    print(x_a == x_c == x_b)
else:
    a_b_slope = ((y_b-y_a)/(x_b-x_a))
    a_c_slope = ((y_c-y_a)/(x_c-x_a))
    b_c_slope = ((y_b-y_c)/(x_b-x_c))
    print(a_b_slope == b_c_slope == a_c_slope)

