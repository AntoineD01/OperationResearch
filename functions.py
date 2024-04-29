
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
    max_rows = min(len(table_data) - 1, 21)  # Exclude the last row (Orders)
    max_columns = min(len(table_data[0]) - 1, 13)  # Exclude the last column (Orders)

    # Initialize the indices for the northwest corner of the matrix
    row_index = 0
    col_index = 0

    new_matrice = table_data
    
    # Change each value to 0 except the last line and last column
    for i in range(max_rows):
        for j in range(max_columns):
            new_matrice[i][j] = 0
    
    display_table(new_matrice)

    # Iterate until we reach the last row or column
    while row_index < max_rows and col_index < max_columns:
        # Find the minimum between supply and demand
        min_value = min(table_data[row_index][-1], table_data[-1][col_index])

        # Allocate the minimum value to the current cell
        new_matrice[row_index][col_index] = min_value

        # Update supply and demand
        new_matrice[row_index][-1] -= min_value
        new_matrice[-1][col_index] -= min_value

        # Move to the next row or column if supply or demand becomes zero
        if new_matrice[row_index][-1] == 0:
            row_index += 1
        else:
            col_index += 1

        # Display the updated table
        display_table(new_matrice)

    # Return the updated matrix
    return new_matrice

def max_column(table_data):
    max_columns = min(len(table_data[0]) - 1, 13)  # Exclude the last column (Provision)
    max_colum = []
    for i in range(max_columns):
        max_value = float('-inf')  
        for row in table_data[:-1]:
            if row[i] > max_value:
                max_value = row[i]
        max_colum.append(max_value)
    return max_colum

def mx_row(table_data):
    max_rows = min(len(table_data) - 1, 21)  # Exclude the last row (Orders)
    max_row = []
    for i in range(max_rows):
        max_value = float('-inf')  
        for column in table_data[i][:-1]:
            if column > max_value:
                max_value = column
        max_row.append(max_value)
    return max_row

def mini_col(table_data):
    max_columns = min(len(table_data[0]) - 1, 13)  # Exclude the last column (Provision)
    min_colum = []
    for i in range(max_columns):
        min_value = float('inf')  
        for row in table_data[:-1]:
            if row[i] < min_value:
                min_value = row[i]
        min_colum.append(min_value)
    return min_colum

def mini_row(table_data):
    max_rows = min(len(table_data) - 1, 21)  # Exclude the last row (Orders)
    min_row = []
    for i in range(max_rows):
        min_value = float('inf')  
        for column in table_data[i][:-1]:
            if column < min_value:
                min_value = column
        min_row.append(min_value)
    return min_row

def vogels_approximation_method(table_data):
    max_rows = min(len(table_data) - 1, 21)  # Exclude the last row (Orders)
    max_columns = min(len(table_data[0]) - 1, 13)  # Exclude the last column (Provision)
    difference_colum = []
    difference_row = []
    
    
    max_colum = max_column(table_data)
    max_row = mx_row(table_data)
    min_colum = mini_col(table_data)
    min_row = mini_row(table_data)

    # Calculate the differences between the maximum and minimum values in each column
    difference_colum = [max_colum[i] - min_colum[i] for i in range(max_columns)]
    
    # Calculate the differences between the maximum and minimum values in each row
    difference_row = [max_row[i] - min_row[i] for i in range(max_rows)]

    # Find the maximum value from both the difference columns and difference rows
    max_diff = max(max(difference_colum), max(difference_row))
    
    print("Maximum difference in columns and rows:", max_diff)


