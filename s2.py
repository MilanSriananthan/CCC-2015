jerseys = int(input())
players = int(input())
jseq = []
pseq = []
for i in range(jerseys):
    hold = input()
    jseq.append(hold)
for x in range(players):
    hold = input()
    hold = hold.split(' ')
    pseq.append(hold)
roster = []
def convert(seq):
    for i in range(len(seq)):
        if seq[i] == 'S':
            seq[i] = 10
        elif seq[i] == "M":
            seq[i] = 100
        elif seq[i] == "L":
            seq[i] = 1000
    return seq
jseq = convert(jseq)
for i in pseq:
    roster.append(convert(i))

def check(info, current):
    if current[int(info[1])-1] >= info[0]:
        current[int(info[1])-1] = 0
        return True
    return False
total = 0
for i in roster:
    if check(i, jseq) == True:
        total = total + 1

print(total)