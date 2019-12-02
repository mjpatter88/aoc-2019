import operator
import sys

opcodes = {
    1: operator.add,
    2: operator.mul,
    99: lambda a, b: StopIteration()
}
with open("input.txt") as f:
    original_data = [int(d) for d in f.read().split(',')]

def execute(pos1_val, pos2_val):
    data = original_data.copy()

    data[1] = pos1_val
    data[2] = pos2_val
    pc = 0

    while pc <= len(data):
        op = opcodes[data[pc]]
        index1 = data[pc+1]
        index2 = data[pc+2]
        dest = data[pc+3]
        result = op(data[index1], data[index2])
        # Ugly, but it works
        if type(result) == StopIteration:
            break
        data[dest] = result
        pc += 4
    
    return data[0]

print(f"Part 1: {execute(12, 2)}")


for noun in range(100):
    for verb in range(100):
        if execute(noun, verb) == 19690720:
            print(f"Part 2: {100*noun + verb}")
            sys.exit(0)