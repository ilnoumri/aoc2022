from lib import open_file

s = open_file("6/input.txt")[0]
def get_marker(nb):
    for i in range(len(s)-nb-1):
        seq = f"{s[i]}"
        for j in range(1, nb):
            seq += f"{s[i+j]}"
        if len(set(seq)) == nb:
            return i +nb

res = get_marker(4)
res2 = get_marker(14)
print(res)
print(res2)