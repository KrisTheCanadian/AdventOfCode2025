from typing import Any

def parse_input(filename: str) -> list[tuple[int, int]]:
    """Parse the input file and return the processed data."""
    ranges: list[tuple[int, int]] = []
    with open(filename, "r") as f:
        for line in f:
            raw_ranges = line.strip().split(',')
            for r in raw_ranges:
                parts = r.split('-')

                # sanity check
                assert len(parts) == 2

                start, end = map(int, parts)
                ranges.append((start, end))
            
    print(ranges)
    return ranges


def isValidPart1(number: int) -> bool:
    number_str = str(number)
    number_arr = list(number_str)
    
    # odd digits are always valid
    if len(number_arr) % 2 == 1:
        return True
    
    # check the string with 2 pointers, one starting at 0 and one starting at the midpoint
    midpoint = int(len(number_arr) / 2)
    ptr1 = 0
    ptr2 = midpoint

    for _ in range(midpoint):
        if number_arr[ptr1] != number_arr[ptr2]:
            return True
        ptr1 += 1
        ptr2 += 1

    return False


def part1(data: list[tuple[int, int]]) -> int:
    """Solve Part 1 of the puzzle."""
    # Any ID with sequence of digits repeated twice is a invalid
    solution = 0
    # We need to figure out all invalid IDs in the ranges
    for r in data:
        start = r[0]
        end = r[1]

        for i in range(start, end + 1):
            if not isValidPart1(i):
                print(f"{i} was found to be valid in the range: {start}:{end}")
                solution += i

    return solution

def isValidPart2(number: int) -> bool:
    number_str = str(number)
    number_arr = list(number_str)

    # single digits cannot repeat
    if len(number_arr) == 0:
        return True
    
    n = len(number_str)
    # Try every possible split size from 1 up to half the length of the string
    for size in range(1, n // 2 + 1):
        # Only consider sizes that divide the string evenly
        if n % size == 0:
            # Split the string into chunks of length 'size'
            parts = [number_str[i:i+size] for i in range(0, n, size)]
            # Check if all chunks are identical
            # If so, the string is made of repeated sequences
            if all(part == parts[0] for part in parts):
                # Found a repeated sequence, so return False
                return False
    # If no repeated sequence is found, return True
    return True


def part2(data: Any) -> int:
    """Solve Part 2 of the puzzle."""
    # Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice.
    solution = 0
    for r in data:
        start = r[0]
        end = r[1]

        for i in range(start, end + 1):
            if not isValidPart2(i):
                print(f"{i} was found to be valid in the range: {start}:{end}")
                solution += i

    return solution


if __name__ == "__main__":
    input_file = "02/input1.txt"
    data = parse_input(input_file)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
