def parse_input(filename: str) -> tuple[list[tuple[int, int]], list[int]]:
    """Parse the input file and return the processed data."""

    is_ingredients = False

    ranges: list[tuple[int, int]] = []
    ingredients: list[int] = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            if line == "":
                is_ingredients = True
                continue
            
            if is_ingredients:
                ingredients.append(int(line))
            else:
                # range
                s = line.split('-')
                start = int(s[0])
                end = int(s[1])
                ranges.append((start, end))
    return (ranges, ingredients)


def part1(data: tuple[list[tuple[int, int]], list[int]]) -> int:
    """Solve Part 1 of the puzzle."""
    ranges = data[0]
    ingredients = data[1]

    fresh_count = 0

    for ingredient in ingredients:
        
        for r in ranges:
            start = r[0]
            end = r[1]

            if ingredient >= start and ingredient <= end:
                fresh_count += 1
                break
    

    return fresh_count


# 3 - 5
# 10 - 14
# 16 - 20
# 12 - 18

# order the ranges
# 3 - 5
# 10 - 14
# 12 - 18
# 16 - 20

# step 1, find overlapping ranges
# 3 - 5 can be combined with nothing...
# 10 - 14 can be combined with 12 - 18 by making 10 - 18
# 10, 11, [12, 13, 14]
# [12, 13, 14], 15, 16, 17, 18
# if my starting or ending number is part of another range, we can combine ranges
# we use the smallest starting number, and the biggest ending number

# step 2, combine those ranges

# 10 - 20

def canBeSimplified(ranges: list[tuple[int, int]]) -> bool:
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            s1, e1 = ranges[i]
            s2, e2 = ranges[j]

            # Ranges overlap if: max(start) <= min(end)
            # Or they're adjacent (e1 + 1 == s2 or e2 + 1 == s1)
            if max(s1, s2) <= min(e1, e2) or e1 + 1 == s2 or e2 + 1 == s1:
                return True
    
    return False

def simplify(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    while canBeSimplified(ranges):
        merged = False
        for i in range(len(ranges)):
            if merged:
                break
            for j in range(i + 1, len(ranges)):
                s1, e1 = ranges[i]
                s2, e2 = ranges[j]

                # Check if ranges overlap or are adjacent
                if max(s1, s2) <= min(e1, e2) or e1 + 1 == s2 or e2 + 1 == s1:
                    # Merge: take minimum start and maximum end
                    new_ranges = [r for idx, r in enumerate(ranges) if idx != i and idx != j]
                    new_ranges.append((min(s1, s2), max(e1, e2)))
                    ranges = new_ranges
                    merged = True
                    break
    
    return ranges


def part2(ranges: list[tuple[int, int]]) -> int:
    """Solve Part 2 of the puzzle."""
    solution = 0
    simplified_ranges = simplify(ranges)
    # now the ranges should have no overlap
    for r in simplified_ranges:
        solution += r[1] - r[0] + 1
    return solution


if __name__ == "__main__":
    input_file = "05/input1.txt"
    data = parse_input(input_file)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data[0]))
