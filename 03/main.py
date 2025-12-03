def parse_input(filename: str) -> list[list[int]]:
    """Parse the input file and return the processed data."""
    with open(filename, "r") as f:
        lines = [[int(d) for d in str(line.strip())] for line in f]
    print(lines)
    return lines


def part1(banks: list[list[int]]) -> int:
    """Solve Part 1 of the puzzle."""
    solution = 0

    for i in range(len(banks)):
        biggest_number = 0
        for j in range(len(banks[i])):
            
            current_first_number = banks[i][j]
            
            for k in range(j + 1 ,len(banks[i])):
                current_second_number = banks[i][k]
                # compare this number with all other numbers
                paired_number = int(str(current_first_number) + str(current_second_number))

                if paired_number > biggest_number:
                    biggest_number = paired_number
        
        print(f"Found {biggest_number} in {banks[i]}")
        solution += biggest_number
            
    return solution

def part2(banks: list[list[int]]) -> int:
    """Solve Part 2 of the puzzle."""
    solution = 0
    # we can turn on 12 batteries instead of 2 (RIP solution 1)
    # 818181911112111

    # we can start with the first 12 digits

    target_length = 12

    # if we have 12 digits or less, we will activate all of them
    for bank in banks:
        if len(bank) <= target_length:
            solution += int("".join(str(d) for d in bank))

        stack = []
        number_of_removals = len(bank) - target_length

        # we want Monotonic Decreasing stack
        for digit in bank:
            # check to see if current digit is larger than top of stack
            while stack and number_of_removals > 0 and stack[-1] < digit:
                stack.pop()
                number_of_removals -= 1
            
            stack.append(digit)
        
        biggest_number = int("".join(str(d) for d in stack[:target_length]))
        print(f"Found {biggest_number} in {bank}")
        solution += biggest_number

    return solution


if __name__ == "__main__":
    input_file = "03/input1.txt"
    data = parse_input(input_file)
    # print("Part 1:", part1(data))
    print("Part 2:", part2(data))
