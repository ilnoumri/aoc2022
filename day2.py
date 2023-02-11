from lib import open_file

data = open_file("2/input.txt")
rps = {"A": ("X","Y", "Z"), "B": ("Y","Z","X"), "C": ("Z","X","Y")}

def shape_point(shape):
    return 1 + ord(shape) - ord("X") 
res = 0
for elt in data:
    opp, me = elt.split()
    sim, winning, _ = rps[opp]
    sp = shape_point(me)
    if me == winning:
        res += 6 + sp
    elif me == sim:
        res += 3 + sp
    else:
        res += sp

print(res)

res2 = 0
for elt in data:
    opp, conclusion = elt.split()
    sim, winning, losing =  rps[opp]
    if conclusion == "X":
        res2 += shape_point(losing)
    elif conclusion == "Y":
        res2 += 3 + shape_point(sim)
    elif conclusion == "Z":
        res2 += 6 + shape_point(winning)

print(res2)

