from lib import open_file

data = open_file("10/input.txt")

instr = None
cycle_x = {}

cycle = 1
x = 1
for cmd in data:
    if instr:
        x += instr
        instr = None
    if cmd != "noop":
        val = int(cmd.split()[1])
        instr = val
        cycle += 2
    else:
        cycle += 1 
    if cycle not in cycle_x:
        cycle_x[cycle] = x

def find_closest(strength):
    start = strength
    while True:
        start += 1
        if start in cycle_x:
            return cycle_x[start]
    

strength_to_check = (20, 60, 100, 140, 180, 220)
res = 0
for strength in strength_to_check:
    val = find_closest(strength)
    res += strength * val
print(res)