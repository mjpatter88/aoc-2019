
def fuel_cost(mass):
    fuel = (mass // 3) - 2
    if fuel <= 0:
        return 0
    return fuel + fuel_cost(fuel)

with open("input.txt") as f:
    nums = [int(line) for line in f.readlines()]

total = 0
for num in nums:
    total += (num // 3) -2
print(f"Part 1: {total}")

part2_total = 0
for num in nums:
    part2_total += fuel_cost(num)
print(f"Part 2: {part2_total}")