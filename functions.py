
def read_table(filename):
    table_data = []

    with open(filename, 'r') as file:
        rows, columns = map(int, file.readline().split())

        for _ in range(rows):
            row_data = list(map(int, file.readline().split()))
            table_data.append(row_data)

    return table_data
