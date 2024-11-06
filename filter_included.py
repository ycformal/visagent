import copy

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
        if percentage_i > 0.85:
            deleted[i] = True
        elif percentage_j > 0.85:
            deleted[j] = True
result = []
for i in range(len(boxes)):
    if not deleted[i]:
        result.append(boxes[i])

changed = True
expanded_boxes = copy.deepcopy(result)
for i in range(len(expanded_boxes)):
    center_x = (expanded_boxes[i][0] + expanded_boxes[i][2]) / 2
    center_y = (expanded_boxes[i][1] + expanded_boxes[i][3]) / 2
    # expanded width and height to 1.5x
    width = expanded_boxes[i][2] - expanded_boxes[i][0]
    height = expanded_boxes[i][3] - expanded_boxes[i][1]
    expanded_boxes[i][0] = center_x - width * 0.75
    expanded_boxes[i][2] = center_x + width * 0.75
    expanded_boxes[i][1] = center_y - height * 0.75
    expanded_boxes[i][3] = center_y + height * 0.75
while changed:
    changed = False
    for i in range(len(result) - 1):
        for j in range(i + 1, len(result)):
            overlap_area = None
            x_distance = min(expanded_boxes[i][2], expanded_boxes[j][2]) - max(expanded_boxes[i][0], expanded_boxes[j][0])
            y_distance = min(expanded_boxes[i][3], expanded_boxes[j][3]) - max(expanded_boxes[i][1], expanded_boxes[j][1])
            if x_distance > 0 and y_distance > 0:
                overlap_area = x_distance * y_distance
            else:
                overlap_area = 0
            percentage_i = overlap_area / ((expanded_boxes[i][2] - expanded_boxes[i][0]) * (expanded_boxes[i][3] - expanded_boxes[i][1]))
            percentage_j = overlap_area / ((expanded_boxes[j][2] - expanded_boxes[j][0]) * (expanded_boxes[j][3] - expanded_boxes[j][1]))
            if percentage_i > 0.6 or percentage_j > 0.6:
                merged_box = [min(result[i][0], result[j][0]), min(result[i][1], result[j][1]), max(result[i][2], result[j][2]), max(result[i][3], result[j][3])]
                result.append(merged_box)
                result.pop(i)
                result.pop(j - 1)
                changed = True
                break
        if changed:
            break

print(result)