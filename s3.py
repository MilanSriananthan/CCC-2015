gates = int(input())
planes = int(input())
nums = []
docks = []
for i in range(planes):
    hold = int(input())
    nums.append(hold)

for i in range(1, gates+1):
    docks.append(i)

def lowestDock(seq, plane):
    x = plane
    while x > 0:
        if x in seq:
            seq.remove(x)
            return [1, seq]
        x = x -1
    return False
count = 0
for i in nums:
    look = lowestDock(docks, i)
    if look == False:
        break
    else:
        count = count + look[0]
        docks = look[1]
print(count)

'''
4
6
2
2
3
3
4
4


'''