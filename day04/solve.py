MIN = 353096
MAX = 843212

def is_valid(num):
    digits = str(num)
    repeated = False
    for index, digit in enumerate(digits):
        if index != 0:
            if digits[index-1] > digit:
                return False
            if digits[index-1] == digit:
                repeated = True
    return repeated

def is_valid_2(num):
    digits = str(num)
    repeated = False
    for index, digit in enumerate(digits):
        if index != 0:
            if digits[index-1] > digit:
                return False
            # Ugly coniditional. Basically, look for the second occurrence of a number.
            # Make sure the number after it is different if it exists.
            # Make sure the number two left of it is different if it exists
            if digits[index-1] == digit and (index==len(digits)-1 or digits[index+1] != digit) and (index == 1 or digits[index-2] != digit):
                repeated = True
    return repeated

count = 0
for x in range(MIN, MAX):
    if is_valid(x):
        count+=1

print(f"Part 1: {count}")

count = 0
for x in range(MIN, MAX):
    if is_valid_2(x):
        count+=1

print(f"Part 2: {count}")