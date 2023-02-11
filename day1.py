from lib import open_file

data = open_file("1/input.txt")

cals = [] 
curr_cal = 0
for elt in data:
    if elt == "":
        cals.append(curr_cal)
        curr_cal = 0
    else:
        curr_cal += int(elt)

if curr_cal != 0:
    cals.append(curr_cal)

cals = sorted(cals, reverse=True)
print(cals[0])
print(sum(cals[:3]))