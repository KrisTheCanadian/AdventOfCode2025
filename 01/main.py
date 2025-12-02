class Rotation:
    def __init__(self, direction: str, amount: int):
        self.direction = direction
        self.amount = amount
    
    def show(self):
        print(f"{self.direction}{self.amount}")

def part1(rotations: list[Rotation]):
    START = 50
    current_index = START
    number_of_zeros = 0
    for rotation in rotations:
        print(f"current index: {current_index}")
        rotation.show()
        if current_index == 0:
            number_of_zeros = number_of_zeros + 1
        if rotation.direction == "R":
            current_index = (current_index + rotation.amount) % 100
        else:
            current_index = (current_index - rotation.amount) % 100
        
    return number_of_zeros

def part2(rotations: list[Rotation]):
    START = 50
    current_index = START
    number_of_zeros = 0

    for rotation in rotations:
        rotation.show()

        # going right
        if rotation.direction == "R":
            for _ in range(rotation.amount):
                current_index = current_index + 1

                if current_index == 100: ## 99 + 1 means we passed 0 and we should count it
                    number_of_zeros = number_of_zeros + 1
                    current_index = 0
                    print(f"Number of zeros increased to {number_of_zeros}")

        # going left
        else:
            for _ in range(rotation.amount):
                if current_index == 0: # if we are at 0 and we need to go left, we should not count the 0 so let's put it at 100
                    current_index = 100

                current_index = current_index - 1

                if current_index == 0:
                    number_of_zeros = number_of_zeros + 1
                    print(f"Number of zeros increased to {number_of_zeros}")
                    current_index = 100
            
        current_index = current_index % 100

        print(f"current index: {current_index}")
        print("=============================")
        
    return number_of_zeros

def parse(filename: str) -> list[Rotation]:
    rotations: list[Rotation] = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            amount = int(line[1:])
            rotations.append(Rotation(direction, amount))
    return rotations


if __name__ == "__main__":
    data = parse("input1.txt")
    print(part1(data))
    print(part2(data))
