boxes = eval(input())
deleted = [False] * len(boxes)
for i in range(len(boxes) - 1):
    for j in range(i + 1, len(boxes)):
        overlap_area = None
        x_distance = min(boxes[i][2], boxes[j][2]) - max(boxes[i][0], boxes[j][0])
        y_distance = min(boxes[i][3], boxes[j][3]) - max(boxes[i][1], boxes[j][1])
        if x_distance > 0 and y_distance > 0:
            overlap_area = x_distance * y_distance
        else:
            overlap_area = 0
        percentage_i = overlap_area / ((boxes[i][2] - boxes[i][0]) * (boxes[i][3] - boxes[i][1]))
        percentage_j = overlap_area / ((boxes[j][2] - boxes[j][0]) * (boxes[j][3] - boxes[j][1]))
        print(i, j, percentage_i, percentage_j)
        if percentage_i > 0.85:
            deleted[i] = True
        elif percentage_j > 0.85:
            deleted[j] = True
result = []
for i in range(len(boxes)):
    if not deleted[i]:
        result.append(boxes[i])

print(result)