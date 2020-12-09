def solution(input_data):
    with open(input_data, "r") as f:
        data = [line.strip() for line in f.readlines()]

    p1_good_passwords = 0
    p2_good_passwords = 0

    for line in data:
        chunks = line.strip().split(" ")
        min_count = int(chunks[0].split("-")[0])
        max_count = int(chunks[0].split("-")[1])
        target_letter = chunks[1].replace(":", "")
        password = chunks[-1]
        letter_count = password.count(target_letter)
        if letter_count >= min_count and letter_count <= max_count:
            p1_good_passwords += 1

        pass_letters = list(password)
        p1_letter = pass_letters[min_count - 1]
        p2_letter = pass_letters[max_count - 1]

        if (
            target_letter in [p1_letter, p2_letter]
            and [p1_letter, p2_letter].count(target_letter) == 1
        ):
            p2_good_passwords += 1

    print(f"Part 1: {p1_good_passwords}")
    print(f"Part 2: {p2_good_passwords}")


if __name__ == "__main__":
    solution("input.txt")
