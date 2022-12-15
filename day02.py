f = open('input/day02.txt')
lines = [line.rstrip() for line in f.readlines()]

program = [int(i) for i in lines[0].split(',')]

def run(program, noun, verb):
    tmp = program[:]
    tmp[1] = noun; tmp[2] = verb
    i = 0
    while True:
        try: op, a, b, to = tmp[i:i + 4]
        except: op = tmp[i]
        if op == 99:
            break
        elif op == 1:
            tmp[to] = tmp[a] + tmp[b]
        elif op == 2:
            tmp[to] = tmp[a] * tmp[b]
        i += 4
    return tmp[0]

part1 = run(program, 12, 2)

for n in range(99 + 1):
    for v in range(99 + 1):
        if run(program, n, v) == 19690720: part2 = 100 * n + v; break

print(f'part 1: {part1}')
print(f'part 2: {part2}')
