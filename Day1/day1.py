from itertools import combinations


def solution(input_data):
    target_sum = 2020
    expense_report = []

    with open(input_data, "r") as f:
        expense_report = [int(amount) for amount in f.readlines()]

    combs = combinations(expense_report, 2)

    for c in combs:
        if sum(c) == target_sum:
            print(f"Part 1: {c[0] * c[1]}")

    combs = combinations(expense_report, 3)

    for c in combs:
        if sum(c) == target_sum:
            print(f"Part 2: {c[0] * c[1] * c[2]}")


if __name__ == "__main__":
    solution("input.txt")
