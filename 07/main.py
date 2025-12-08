def parse_input(filename: str) -> list[list[str]]:
    """Parse the input file and return the processed data."""
    with open(filename, "r") as f:
        lines = [[str(d) for d in line.strip()] for line in f]
    # TODO: Process lines as needed for your puzzle
    return lines


def find_starting_point(m: list[list[str]]) -> tuple[int, int]:
    for i in range(len(m)):
        for j in range(len(m[i])):
            token = m[i][j]
            if token == "S":
                return (i, j)
            
    # we did not find the starting point
    assert False

def down(coordinates: tuple[int, int]) -> tuple[int, int]:
    return (coordinates[0] + 1, coordinates[1])

def print_map(matrix: list[list[str]]): 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")

        print("\n")

def part1(matrix: list[list[str]]) -> int:
    """Solve Part 1 of the puzzle."""
    starting_coordinates = find_starting_point(matrix)
    current_beams = [starting_coordinates]
    next_beams = []

    splits = 0

    for row in range(len(matrix) - 1):
        
        for beam in current_beams:
            i, j = down(beam)
            token = matrix[i][j]

            if token == ".":
                # modify map
                matrix[i][j] = "|"
                next_beams.append((i, j))

            elif token == "^":
                splits += 1
                # we need to split the beam
                left_side_coordinates = (i, j - 1)
                right_side_coordinates = (i, j + 1)

                left_side = matrix[left_side_coordinates[0]][left_side_coordinates[1]]
                right_side = matrix[right_side_coordinates[0]][right_side_coordinates[1]]

                if left_side == ".":
                    matrix[left_side_coordinates[0]][left_side_coordinates[1]] = "|"
                    next_beams.append(left_side_coordinates)
                    
                
                if right_side == ".":
                    matrix[right_side_coordinates[0]][right_side_coordinates[1]] = "|"
                    next_beams.append(right_side_coordinates)
        
        current_beams = next_beams
        next_beams = []

        # print(f"Row: {row}")

        # print_map(matrix)


    return splits

def part2(matrix: list[list[str]]) -> int:
    """Solve Part 2 of the puzzle."""
    start_r, start_c = find_starting_point(matrix)
    
    # Map of col -> count of timelines
    current_counts = {start_c: 1}
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    for r in range(start_r, rows - 1):
        next_counts = {}
        
        for c, count in current_counts.items():
            # Look at the cell below
            next_r = r + 1
            
            # Check bounds just in case
            if next_r >= rows:
                continue
                
            target_char = matrix[next_r][c]
            
            if target_char == '^':
                # Split
                # Left
                if c - 1 >= 0:
                    next_counts[c - 1] = next_counts.get(c - 1, 0) + count
                # Right
                if c + 1 < cols:
                    next_counts[c + 1] = next_counts.get(c + 1, 0) + count
            else:
                # Continue straight
                next_counts[c] = next_counts.get(c, 0) + count
                
        current_counts = next_counts
        
    return sum(current_counts.values())


if __name__ == "__main__":
    input_file = "07/example1.txt"
    data = parse_input(input_file)
    # print("Part 1:", part1(data))
    print("Part 2:", part2(data))
