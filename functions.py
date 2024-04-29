
def read_table(filename):
    table_data = []

    with open(filename, 'r') as file:
        rows, columns = map(int, file.readline().split())

        for _ in range(rows):
            row_data = list(map(int, file.readline().split()))
            table_data.append(row_data)

    return table_data

def display_table(table_data):
    max_rows = min(len(table_data) - 1, 20)  # Exclude the last row (Orders)
    max_columns = min(len(table_data[0]), 12)

    # Display column headers
    print('          ', end='')  
    for col in range(1, max_columns + 1):
        print(f'C{col:<4}', end='')  # Updated column headers
    print()

    # Display table data
    for i in range(max_rows):
        print('    ', end='')  
        print(f'P{i + 1:2}', end='')
        for j in range(max_columns):
            print(f'{table_data[i][j]:5}', end='')
        print()

    # Display capacities
    print('Orders:', end='')
    for j in range(max_columns):
        print(f'{table_data[-1][j]:5}', end='')
