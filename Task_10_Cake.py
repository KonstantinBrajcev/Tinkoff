# Соня с Сашей купили торт в форме выпуклого многоугольника на n вершинах. Они хотят разделить этот торт на две равные части одним строго вертикальным разрезом. А, именно, линия разреза на торте должна быть параллельна координатной оси Oy
# Найдите x - координату, вдоль которой надо сделать искомый разрез.
# ------------------------------------
def area_of_polygon(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0


def calculate_area_split(vertices, x_cut):
    left_area = 0.0
    right_area = 0.0
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        if x1 > x_cut and x2 > x_cut:
            right_area += (x2 - x1) * (y2 + y1) / 2.0
        elif x1 < x_cut and x2 < x_cut:
            left_area += (x2 - x1) * (y2 + y1) / 2.0
        else:
            if x1 == x2:  # вертикальная линия
                continue
            k = (y2 - y1) / (x2 - x1)
            y_cut = k * (x_cut - x1) + y1

            if x1 < x_cut < x2:
                left_area += (x_cut - x1) * (y_cut + y1) / 2.0
                right_area += (x2 - x_cut) * (y2 + y_cut) / 2.0
            else:
                right_area += (x_cut - x1) * (y_cut + y1) / 2.0
                left_area += (x2 - x_cut) * (y2 + y_cut) / 2.0
    return left_area, right_area


def find_cut_x(vertices):
    min_x = min(x for x, y in vertices)
    max_x = max(x for x, y in vertices)
    total_area = area_of_polygon(vertices)
    target_area = total_area / 2.0
    # Бинарный поиск
    low, high = min_x, max_x
    precision = 1e-9

    while high - low > precision:
        mid = (low + high) / 2.0
        left_area, right_area = calculate_area_split(vertices, mid)
        if left_area < target_area:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0


n = int(input())
vertices = []
for _ in range(n):
    x, y = map(int, input().split())
    vertices.append((x, y))
cut_x = find_cut_x(vertices)
print(f"{cut_x:.9f}")
# ЧАСТИЧНОЕ РЕШЕНИЕ/ПРОЙДЕННЫЙ ТЕСТ - 1
