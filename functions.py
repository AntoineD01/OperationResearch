
def read_table(filename):
    table_data = []

    with open(filename, 'r') as file:
        rows, columns = map(int, file.readline().split())

        for _ in range(rows):
            row_data = list(map(int, file.readline().split()))
            table_data.append(row_data)
        
        orders_data = list(map(int, file.readline().split()))
        table_data.append(orders_data)

    return table_data

def display_table(table_data):
    max_rows = min(len(table_data), 21)  # Include the last row (Orders)
    max_columns = min(len(table_data[0]), 13)

    # Display column headers
    print('\n\n          ', end='')  
    for col in range(1, max_columns):
        print(f'C{col:<4}', end='')  # Updated column headers
    print('P')

    # Display table data
    for i in range(max_rows - 1):  # Exclude the last row (Orders)
        print('    ', end='')  
        print(f'P{i + 1:2}', end='')
        for j in range(max_columns):
            print(f'{table_data[i][j]:5}', end='')
        print()

    # Display capacities
    print('Orders:', end='')
    for j in range(max_columns - 1):  # Exclude the last capacity
        print(f'{table_data[-1][j]:5}', end='')
    print()  # Add a new line for formatting

def north_west_corner_method(table_data):
    max_rows = min(len(table_data) - 1, 20)  # Exclude the last row (Orders)
    max_columns = min(len(table_data[0]) - 1, 12)  # Exclude the last column (Orders)

    # Initialize the indices for the northwest corner of the matrix
    row_index = 0
    col_index = 0

    # Iterate until we reach the last row or column
    while row_index < max_rows and col_index < max_columns:
        # Find the minimum between supply and demand
        min_value = min(table_data[row_index][-1], table_data[-1][col_index])

        # Allocate the minimum value to the current cell
        table_data[row_index][col_index] = min_value

        # Update supply and demand
        table_data[row_index][-1] -= min_value
        table_data[-1][col_index] -= min_value

        # Move to the next row or column if supply or demand becomes zero
        if table_data[row_index][-1] == 0:
            row_index += 1
        else:
            col_index += 1

        # Display the updated table
        display_table(table_data)
