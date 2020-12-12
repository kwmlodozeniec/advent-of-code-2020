data = []
with open("5.data", "r") as f:
    data = [x.strip() for x in f.readlines()]


def get_row(input):
    start = 0
    end = 127
    for indicator in input:
        print("Before: ", indicator, start, end)
        if indicator == "F":
            end -= int((end - start) / 2)
        else:
            start += int((end - start) / 2)
        #     if indicator == "F":
        #         end = int((end - start) + 1) / 2
        #     elif indicator == "B":
        #         start = int((start + end + 1) / 2) - 1
        print("After: ", indicator, start, end)
    if input[-1] == "F":
        return start
    else:
        return end


def get_column(input):
    start = 0
    end = 7
    for indicator in input:
        # print("Before: ", indicator, start, end)
        if indicator == "L":
            end -= int((end - start) / 2)
        elif indicator == "R":
            start += int((end - start) / 2)
        # print("After: ", indicator, start, end)
    return start


seat_ids = []

for line in data:
    row_data = list(line)[:7]
    column_data = list(line)[7:]
    row = get_row(row_data)
    column = get_column(column_data)
    seat_id = (row * 8) + column
    # print(row, column, seat_id)
    seat_ids.append(seat_id)
    break

print(f"Max seat ID: {max(seat_ids)}")

seats = [
    (int("".join(map(lambda x: "1" if x in "BR" else "0", s.rstrip())), 2)) for s in open("5.data")
]
print(seats[0])
print(
    f"Highest: {max(seats)}\tYour seat: {next(filter(lambda x: x not in seats, range(min(seats), max(seats))))}"
)
