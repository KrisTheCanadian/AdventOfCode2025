def parse_input(filename: str) -> list[list[str]]:
    """Parse the input file and return the processed data."""
    with open(filename, "r") as f:
        lines = [[str(d) for d in line.strip()] for line in f]
    return lines


def part1(data: list[list[str]]) -> int:
    """Solve Part 1 of the puzzle."""
    accessible_paper_rolls = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            current_symbol = data[i][j]
            
            paper_roll_neighbours = 0

            if current_symbol != '@':
                continue

            # top (-i)
            if i > 0 and data[i -1][j] == '@':
                paper_roll_neighbours += 1

            # bottom (+i)
            if i < len(data) - 1 and data[i + 1][j] == '@':
                paper_roll_neighbours += 1
            
            # left (-j)
            if j > 0 and data[i][j - 1] == '@':
                paper_roll_neighbours += 1

            # right (+j)
            if j < len(data[i]) - 1 and data[i][j + 1] == '@':
                paper_roll_neighbours += 1

            # top left (-i, -j)
            if i > 0 and j > 0 and data[i -1][j - 1] == '@':
                paper_roll_neighbours += 1

            # top right (-i, +j)
            if i > 0 and j < len(data[i]) - 1 and data[i -1][j + 1] == '@':
                paper_roll_neighbours += 1

            # bottom left (+i, -j)
            if i < len(data) - 1 and j > 0 and data[i + 1][j - 1] == '@':
                paper_roll_neighbours += 1

            # bottom right (+i, +j)
            if i < len(data) - 1 and j < len(data[i]) - 1 and data[i + 1][j + 1] == '@':
                paper_roll_neighbours += 1

            if paper_roll_neighbours < 4:
                accessible_paper_rolls += 1

    return accessible_paper_rolls


def part2(data: list[list[str]]) -> int:
    """Solve Part 2 of the puzzle."""
    # TODO: Implement Part 2 solution logic
    count_rolls_removed = 0
    removed_last_pass = True
    to_be_removed: list[tuple[int, int]] = []
    while removed_last_pass:
        # reset flag
        removed_last_pass = False

        for i in range(len(data)):
            for j in range(len(data[i])):
                current_symbol = data[i][j]
                
                paper_roll_neighbours = 0

                if current_symbol != '@':
                    continue

                # top (-i)
                if i > 0 and data[i -1][j] == '@':
                    paper_roll_neighbours += 1

                # bottom (+i)
                if i < len(data) - 1 and data[i + 1][j] == '@':
                    paper_roll_neighbours += 1
                
                # left (-j)
                if j > 0 and data[i][j - 1] == '@':
                    paper_roll_neighbours += 1

                # right (+j)
                if j < len(data[i]) - 1 and data[i][j + 1] == '@':
                    paper_roll_neighbours += 1

                # top left (-i, -j)
                if i > 0 and j > 0 and data[i -1][j - 1] == '@':
                    paper_roll_neighbours += 1

                # top right (-i, +j)
                if i > 0 and j < len(data[i]) - 1 and data[i -1][j + 1] == '@':
                    paper_roll_neighbours += 1

                # bottom left (+i, -j)
                if i < len(data) - 1 and j > 0 and data[i + 1][j - 1] == '@':
                    paper_roll_neighbours += 1

                # bottom right (+i, +j)
                if i < len(data) - 1 and j < len(data[i]) - 1 and data[i + 1][j + 1] == '@':
                    paper_roll_neighbours += 1

                if paper_roll_neighbours < 4:
                    # we need to remove the paper rolls 
                    to_be_removed.append((i, j))
        
        # we need to remove everything in the to_be_removed
        for i in range(len(to_be_removed)):
            x = to_be_removed[i][0]
            y = to_be_removed[i][1]

            data[x][y] = "X"

            removed_last_pass = True

        count_rolls_removed += len(to_be_removed)
        to_be_removed = []

    return count_rolls_removed


if __name__ == "__main__":
    input_file = "04/input1.txt"
    data = parse_input(input_file)
    # print("Part 1:", part1(data))
    print("Part 2:", part2(data))
