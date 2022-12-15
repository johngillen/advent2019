f = open('input/day01.txt')
lines = [line.rstrip() for line in f.readlines()]

def fuel(mass):
    x = mass // 3 - 2
    if x <= 0: return 0
    return fuel(x) + x

part1 = sum([int(line) // 3 - 2 for line in lines])
part2 = sum([fuel(int(line)) for line in lines])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
