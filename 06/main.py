def parse_input(filename: str) -> list[list[str]]:
    """Parse the input file and return the processed data."""
    with open(filename, "r") as f:
        lines = [line.strip().split() for line in f]

    return lines

def part1(data: list[list[str]]) -> int:
    """Solve Part 1 of the puzzle."""
    # TODO: Implement Part 1 solution logic
    
    total = 0

    for i in range(len(data[0])):
        column_solution = 0
        operation = data[-1][i]
        
        if operation == "*":
            column_solution = 1
        
        for j in range(len(data)):

            token = data[j][i]

            if token == "*" or token == "+":
                continue

            if operation == "*":
                column_solution *= int(token)
            else:
                column_solution += int(token)
        
        total += column_solution
                
            
    return total


def part2(filename) -> int:
    """Solve Part 2 of the puzzle."""
    # TODO: Implement Part 2 solution logic
    data = []
    with open(filename, "r") as f:
        data = [line.split('\n')[0] for line in f]

    operator = ""
    column_solution = 0
    total = 0

    length_of_longest_string = len(max(data, key=len))

    for i in range(length_of_longest_string):
        s = ""
        

        for j in range(len(data)):

            if i >= len(data[j]):
                s += " "
                continue

            token = data[j][i]
            
            if token == "*" or token == "+":
                operator = token

                if operator == "*":
                    column_solution = 1

                continue
            
            s += token
        
        # check for space column
        if len(s.strip()) == 0:
            print(column_solution)
            total += column_solution
            column_solution = 0

        elif operator == "*":
            column_solution *= int(s.strip())
        else:
            column_solution += int(s.strip())
        

        if i == length_of_longest_string - 1:
            print(column_solution)
            total += column_solution
            column_solution = 0
    
    return total


if __name__ == "__main__":
    input_file = "06/input1.txt"
    data = parse_input(input_file)
    # print("Part 1:", part1(data))
    print("Part 2:", part2(input_file))
