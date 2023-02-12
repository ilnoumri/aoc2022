from lib import open_file

data = open_file("8/input.txt")

def visible_left_right(idx, row):
    visible_left = [0, True]
    visible_right = [0, True]
    if idx == 0 or idx == len(data[0])-1:
        return (visible_left, visible_right)
    value = data[row][idx]
    curr = idx
    while curr > 0:
        curr -= 1
        visible_left[0] += 1
        if data[row][curr] >= value:
            visible_left[1] = False
            break
    curr = idx
    while curr < len(data[0]) - 1:
        curr += 1
        visible_right[0] += 1
        if data[row][curr] >= value:
            visible_right[1] = False
            break
    return (visible_left,visible_right)

def visible_up_down(idx, row):
    visible_up = [0, True]
    visible_down = [0, True]
    if row == 0 or row == len(data) -1:
        return visible_up, visible_down
    value = data[row][idx]
    curr = row
    while curr > 0:
        curr -= 1
        visible_up[0] += 1
        if data[curr][idx] >= value:
            visible_up[1] = False
            break
    curr = row
    while curr < len(data) - 1:
        curr += 1
        visible_down[0] += 1
        if data[curr][idx] >= value:
            visible_down[1] = False
            break
    return (visible_up, visible_down)

res = 0
scenic_score = []
for i in range(len(data)):
    for j in range(len(data[0])):
        visible_left, visible_right = visible_left_right(j, i)
        visibile_up, visible_down = visible_up_down(j, i)
        visibility = [visibile_up, visible_down, visible_left, visible_right]
        score = 1
        for vis in visibility:
            score *= vis[0]
        scenic_score.append(score)
        for vis in visibility:
            if vis[1] == True:
                res += 1
                break
print(res)
res2 = max(scenic_score)
print(res2)