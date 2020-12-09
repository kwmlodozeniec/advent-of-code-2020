def solution(input_data):
    with open(input_data, "r") as f:
        data = [line.strip() for line in f.readlines()]

    matrix = []
    for line in data:
        matrix.append(list(line.strip()))

    trees_1 = 0
    trees_2 = 0
    trees_3 = 0
    trees_4 = 0
    trees_5 = 0

    def count_trees(right, down, matrix):
        position = 0
        trees = 0
        for line in range(down, len(matrix), int(down / 1)):
            position += right
            char = matrix[line][position % len(matrix[line])]
            if char == "#":
                trees += 1
        return trees

    trees_1 = count_trees(1, 1, matrix)
    trees_2 = count_trees(3, 1, matrix)
    trees_3 = count_trees(5, 1, matrix)
    trees_4 = count_trees(7, 1, matrix)
    trees_5 = count_trees(1, 2, matrix)

    print(f"Part 1: {trees_2}")
    print(f"Part 2: {trees_1 * trees_2 * trees_3 * trees_4 * trees_5}")


if __name__ == "__main__":
    solution("input.txt")
